from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re

def read_file(path):
    if not os.path.exists(path):
        print("❌ Không tìm thấy file:", path)
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)  # thay bằng space
    return text.strip()

def compare_report(file1, file2):
    t1 = clean_text(read_file(file1))
    t2 = clean_text(read_file(file2))

    # 🚨 Fix lỗi rỗng
    if not t1 or not t2:
        print("⚠️ Một trong hai file rỗng!")
        return 0

    vectorizer = TfidfVectorizer()

    try:
        tfidf = vectorizer.fit_transform([t1, t2])
    except ValueError:
        print("⚠️ Dữ liệu không hợp lệ để vector hóa!")
        return 0

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(similarity[0][0] * 100, 2)

# TEST
f1 = r"D:\python\Sosanhfilenangcao\report1.txt"
f2 = r"D:\python\Sosanhfilenangcao\report2.txt"

print("📄 Độ giống báo cáo:", compare_report(f1, f2), "%")