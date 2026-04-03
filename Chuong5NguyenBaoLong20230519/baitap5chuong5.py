def count_words_in_file():
    # Tạo file mẫu demo_file2.txt để test
    sample_content = "Dem so luong tu xuat hien abc abc abc 12 12 it it eaut"
    with open('D:\python\Chuong5NguyenBaoLong20230519demo_file2.txt', 'w', encoding='utf-8') as f:
        f.write(sample_content)

    # Bắt đầu đếm
    word_count = {}
    try:
        with open('D:\\python\\Chuong5NguyenBaoLong20230519\\demo_file2.txt', 'r', encoding='utf-8') as f:
            # Đọc file và tách các từ dựa trên khoảng trắng
            words = f.read().split()
            
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        
        print("Kết quả trả về:")
        print(word_count)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file demo_file2.txt")

