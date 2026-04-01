a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

# a) Tổng và tích
tong = a + b + c
tich = a * b * c
print("Tổng =", tong)
print("Tích =", tich)

# b) Hiệu (ví dụ a - b)
print("Hiệu a - b =", a - b)

# c) Chia a cho b
if b != 0:
    print("Chia nguyên a // b =", a // b)
    print("Phần dư a % b =", a % b)
    print("Chia chính xác a / b =", a / b)
else:
    print("Không thể chia cho 0")