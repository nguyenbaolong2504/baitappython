import difflib

def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def compare_code(file1, file2):
    code1 = read_file(file1)
    code2 = read_file(file2)

    similarity = difflib.SequenceMatcher(None, code1, code2).ratio()
    return round(similarity * 100, 2)

# TEST
f1 = "D:\\python\\Sosanhfilenangcao\\project1.txt"
f2 = "D:\\python\\Sosanhfilenangcao\\project2.txt"

print("Mức độ giống nhau:", compare_code(f1, f2), "%")