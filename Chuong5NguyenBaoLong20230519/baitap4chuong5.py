# B4
info = {
    "ten": input("Tên: "),
    "tuoi": input("Tuổi: "),
    "email": input("Email: "),
    "skype": input("Skype: "),
    "dia_chi": input("Địa chỉ: "),
    "noi_lam_viec": input("Nơi làm việc: ")
}

# a) Lưu vào file
with open("D:\\python\\Chuong5NguyenBaoLong20230519\\setInfo.txt", "w", encoding="utf-8") as f:
    for key, value in info.items():
        f.write(f"{key}: {value}\n")

# b) Đọc và hiển thị
print("\nThông tin từ file:")
with open("D:\\python\\Chuong5NguyenBaoLong20230519\\setInfo.txt", "r", encoding="utf-8") as f:
    print(f.read())