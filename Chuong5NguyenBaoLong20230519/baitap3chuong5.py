# B3
content = "Thực hành\nn voi n file\nIO\n"

# Tạo file
with open("D:\\python\\Chuong5NguyenBaoLong20230519\\demo_file1.txt", "w", encoding="utf-8") as f:
    f.write(content)

# a) In trên 1 dòng
with open("D:\\python\\Chuong5NguyenBaoLong20230519\\demo_file1.txt", "r", encoding="utf-8") as f:
    print("a) In trên 1 dòng:")
    print(f.read().replace("\n", " "))

# b) In từng dòng
with open("D:\\python\\Chuong5NguyenBaoLong20230519\\demo_file1.txt", "r", encoding="utf-8") as f:
    print("b) In từng dòng:")
    for line in f:
        print(line.strip())