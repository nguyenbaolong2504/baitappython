import math

# 1. Tính tổng 2 số
def tong_2_so(a, b):
    return a + b

# 2. Tính tổng n số (1 -> n)
def tong_n_so(n):
    return sum(range(1, n + 1))

# 3. Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm số nguyên tố trong [a, b]
def tim_so_nguyen_to(a, b):
    print("Các số nguyên tố:", end=" ")
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

# 5. Kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong == n

# 6. Tìm số hoàn hảo trong [a, b]
def tim_so_hoan_hao(a, b):
    print("Các số hoàn hảo:", end=" ")
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()

# 7. Menu
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng n số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong [a, b]")
        print("0. Thoát")

        choice = int(input("Chọn chức năng: "))

        if choice == 1:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Kết quả:", tong_2_so(a, b))

        elif choice == 2:
            n = int(input("Nhập n: "))
            print("Kết quả:", tong_n_so(n))

        elif choice == 3:
            n = int(input("Nhập n: "))
            if la_so_nguyen_to(n):
                print("Là số nguyên tố")
            else:
                print("Không phải số nguyên tố")

        elif choice == 4:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            tim_so_nguyen_to(a, b)

        elif choice == 5:
            n = int(input("Nhập n: "))
            if la_so_hoan_hao(n):
                print("Là số hoàn hảo")
            else:
                print("Không phải số hoàn hảo")

        elif choice == 6:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            tim_so_hoan_hao(a, b)

        elif choice == 0:
            print("Thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình
menu()