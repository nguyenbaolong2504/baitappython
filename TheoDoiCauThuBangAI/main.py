import cv2
import numpy as np
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
from math import sqrt

# 1. Tải model - Sử dụng bản 'n' (nano) để đạt tốc độ nhanh nhất
model = YOLO("yolov8n.pt")

# 2. Cấu hình Tracker - Tăng max_age để giữ ID khi cầu thủ bị che khuất
tracker = DeepSort(max_age=50, n_init=3)

cap = cv2.VideoCapture("match.mp4")

# Lấy thông tin video để tính toán chính xác hơn
fps = cap.get(cv2.CAP_PROP_FRAME_COUNT)
if fps == 0: fps = 30 

player_team = {}
player_positions = {}
player_speed = {}
player_distance = {}
touches = {}
prev_ball_center = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    mid_x = width // 2

    # 3. Dự đoán với YOLO (Chỉ lọc lớp Người:0 và Bóng:32)
    # stream=True giúp tiết kiệm bộ nhớ
    results = model(frame, verbose=False)[0]

    detections = []
    ball_center = None

    for r in results.boxes:
        cls = int(r.cls[0])
        conf = float(r.conf[0])
        x1, y1, x2, y2 = map(int, r.xyxy[0])

        if cls == 0 and conf > 0.4:  # Cầu thủ
            w, h = x2 - x1, y2 - y1
            detections.append(([x1, y1, w, h], conf, 'person'))
        
        if cls == 32 and conf > 0.2:  # Bóng (giảm conf vì bóng nhỏ, khó bắt)
            ball_center = ((x1 + x2) // 2, (y1 + y2) // 2)
            cv2.circle(frame, ball_center, 8, (0, 255, 255), -1)

    # 4. Cập nhật Tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())
        cx, cy = (l + r) // 2, (b) // 2  # Lấy điểm ở chân cầu thủ để chính xác hơn

        # Phân đội đơn giản theo vị trí xuất phát
        if track_id not in player_team:
            player_team[track_id] = "Left" if cx < mid_x else "Right"
            player_distance[track_id] = 0
            touches[track_id] = 0
            player_positions[track_id] = []

        team = player_team[track_id]
        player_positions[track_id].append((cx, cy))

        # Tính quãng đường và vận tốc
        if len(player_positions[track_id]) > 1:
            prev_x, prev_y = player_positions[track_id][-2]
            dist = sqrt((cx - prev_x)**2 + (cy - prev_y)**2)
            player_distance[track_id] += dist
            player_speed[track_id] = dist * 0.5 # Hệ số điều chỉnh tùy độ phân giải

        # 5. Logic chạm bóng (Cải tiến)
        if ball_center:
            dist_to_ball = sqrt((cx - ball_center[0])**2 + (cy - ball_center[1])**2)
            # Nếu bóng gần chân cầu thủ (< 40px) và bóng đang di chuyển
            if dist_to_ball < 45:
                if prev_ball_center:
                    ball_move = sqrt((ball_center[0]-prev_ball_center[0])**2 + 
                                     (ball_center[1]-prev_ball_center[1])**2)
                    if ball_move > 3:
                        touches[track_id] += 1

        # Vẽ giao diện
        color = (255, 0, 0) if team == "Left" else (0, 255, 0)
        cv2.rectangle(frame, (l, t), (r, b), color, 2)
        
        display_text = f"ID:{track_id} {team} | T:{touches[track_id]}"
        cv2.putText(frame, display_text, (l, t - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    prev_ball_center = ball_center
    
    # Hiển thị
    cv2.line(frame, (mid_x, 0), (mid_x, height), (0, 0, 255), 1)
    cv2.imshow("Football Analysis", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# --- HEATMAP (Giữ nguyên logic của bạn nhưng thêm kiểm tra) ---
if player_positions:
    heatmap = np.zeros((height, width), dtype=np.float32)
    for pid in player_positions:
        for (x, y) in player_positions[pid]:
            if 0 <= x < width and 0 <= y < height:
                heatmap[y, x] += 1
    
    heatmap = cv2.GaussianBlur(heatmap, (51, 51), 0)
    heatmap_norm = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    heatmap_color = cv2.applyColorMap(heatmap_norm, cv2.COLORMAP_JET)
    
    cv2.imshow("Final Heatmap", heatmap_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()