text = input("Nhập đoạn văn: ")

with open("D:\\python\\Chuong5NguyenBaoLong20230519\\output.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("D:\\python\\Chuong5NguyenBaoLong20230519\\output.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:")
    print(f.read())