import subprocess

print("🚀 Đang khởi động quá trình đẩy code tự động...")

try:
    # 1. Gom tất cả các file thay đổi (Tương đương: git add .)
    print("-> Đang gom các file...")
    subprocess.run(["git", "add", "."], check=True)
    
    # 2. Lưu lại lịch sử (Tương đương: git commit -m "...")
    print("-> Đang tạo commit...")
    commit_message = "Hoàn thành các bài tập Python cơ bản"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    
    # 3. Đẩy lên GitHub (Tương đương: git push)
    print("-> Đang đẩy lên GitHub...")
    subprocess.run(["git", "push"], check=True)
    
    print("🎉 Tuyệt vời! Toàn bộ code đã được tự động đẩy lên GitHub thành công.")

except subprocess.CalledProcessError as e:
    # Bắt lỗi nếu lệnh Git chạy thất bại (ví dụ: chưa có gì thay đổi để push)
    print("\n⚠️ Có lỗi xảy ra hoặc không có thay đổi mới nào để đẩy lên.")
    print("Hãy chắc chắn rằng bạn đã khởi tạo Git và liên kết với GitHub.")