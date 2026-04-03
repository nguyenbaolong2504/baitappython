import ast
import difflib
import os

# Đọc file an toàn
def read_file(path):
    if not os.path.exists(path):
        print("❌ Không tìm thấy file:", path)
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

# Lấy cấu trúc LOGIC quan trọng
def get_structure(code):
    try:
        tree = ast.parse(code)
    except:
        return []

    structure = []

    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            structure.append("FOR")
        elif isinstance(node, ast.While):
            structure.append("WHILE")
        elif isinstance(node, ast.If):
            structure.append("IF")
        elif isinstance(node, ast.FunctionDef):
            structure.append("FUNC")
        elif isinstance(node, ast.Call):
            structure.append("CALL")
        elif isinstance(node, ast.Assign):
            structure.append("ASSIGN")
        elif isinstance(node, ast.Return):
            structure.append("RETURN")

    return structure

# So sánh logic
def compare_structure(code1, code2):
    s1 = get_structure(code1)
    s2 = get_structure(code2)

    return difflib.SequenceMatcher(None, s1, s2).ratio()

# TEST
file1 = r"D:\python\Sosanhfilenangcao\phantramtrungnhau.py"
file2 = r"D:\python\Chuong5NguyenBaoLong20230519\baitap5chuong5.py"

code1 = read_file(file1)
code2 = read_file(file2)

score = compare_structure(code1, code2)

print("👉 Giống về logic:", round(score * 100, 2), "%")