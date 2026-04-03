# B5
with open("D:\\python\\Chuong5NguyenBaoLong20230519\\demo_file2.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Tách từ
words = text.split()

# Đếm
result = {}
for word in words:
    word = word.strip(".,!?")  # loại dấu câu
    result[word] = result.get(word, 0) + 1

print("Kết quả:", result)