from datetime import datetime, timedelta

# Khởi tạo danh sách các bàn billiards
tables = {i: None for i in range(1, 11)}  # Giả sử có 10 bàn, tất cả đều trống

# Tỷ lệ giá theo giờ
price_per_hour = 50000  # 50,000 VND mỗi giờ

# Hàm hiển thị trạng thái các bàn
def display_table_status():
    print("\nTrạng thái bàn:")
    for table, status in tables.items():
        if status is None:
            print(f"Bàn {table}: Trống")
        else:
            print(f"Bàn {table}: Đang sử dụng bởi {status['customer']} (bắt đầu lúc {status['start_time'].strftime('%H:%M:%S')})")

# Hàm đặt bàn
def book_table(table_number, customer_name):
    if tables[table_number] is None:
        start_time = datetime.now()
        tables[table_number] = {'customer': customer_name, 'start_time': start_time}
        print(f"Bàn {table_number} đã được đặt bởi {customer_name} lúc {start_time.strftime('%H:%M:%S')}.")
    else:
        print(f"Bàn {table_number} đang được sử dụng. Vui lòng chọn bàn khác.")

# Hàm trả bàn và tính tiền
def release_table(table_number):
    if tables[table_number] is not None:
        end_time = datetime.now()
        booking_info = tables[table_number]
        start_time = booking_info['start_time']
        duration = end_time - start_time
        hours = duration.total_seconds() / 3600
        cost = round(hours * price_per_hour)
        print(f"\nKhách hàng {booking_info['customer']} đã chơi {duration} giờ.")
        print(f"Tổng chi phí: {cost} VND.")
        tables[table_number] = None
    else:
        print(f"Bàn {table_number} hiện đang trống.")

# Hàm tính toán doanh thu trong ngày (giả định doanh thu lưu trữ trong danh sách)
revenue_today = []

def add_revenue(amount):
    revenue_today.append(amount)

def display_revenue():
    total_revenue = sum(revenue_today)
    print(f"\nDoanh thu hôm nay: {total_revenue} VND.")

# Hàm chính
def main():
    while True:
        print("\n=== Quản lý quán billiards ===")
        print("1. Xem trạng thái bàn")
        print("2. Đặt bàn")
        print("3. Trả bàn và tính tiền")
        print("4. Xem doanh thu hôm nay")
        print("5. Thoát")
        
        choice = input("Chọn một chức năng (1-5): ")
        
        if choice == '1':
            display_table_status()
        elif choice == '2':
            table_number = int(input("Nhập số bàn muốn đặt (1-10): "))
            customer_name = input("Nhập tên khách hàng: ")
            book_table(table_number, customer_name)
        elif choice == '3':
            table_number = int(input("Nhập số bàn muốn trả (1-10): "))
            release_table(table_number)
            cost = int(input("Nhập số tiền cần thêm vào doanh thu: "))
            add_revenue(cost)
        elif choice == '4':
            display_revenue()
        elif choice == '5':
            print("Thoát chương trình. Chúc bạn một ngày tốt lành!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
