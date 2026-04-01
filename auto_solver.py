import os
import re
from datetime import datetime

# ================== 1. GENERATE CODE ==================
def generate_code(problem_text):
    text = problem_text.lower()

    # Bài chia hết
    if "chia hết cho 2" in text or "chia hết cho 3" in text:
        return """n = int(input("Nhập số nguyên dương: "))

if n % 2 == 0 and n % 3 == 0:
    print("Chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Chia hết cho 2")
elif n % 3 == 0:
    print("Chia hết cho 3")
else:
    print("Không chia hết cho 2 hoặc 3")
"""

    # Phương trình bậc 2
    elif "phương trình bậc 2" in text:
        return """import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    print("Không phải phương trình bậc 2")
else:
    delta = b*b - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Nghiệm kép:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Hai nghiệm:", x1, x2)
"""

    return "# TODO: Chưa hỗ trợ dạng bài này\n"


# ================== 2. SPLIT PROBLEMS ==================
def split_problems(text):
    contents = re.split(r"Bài\s*\d+:", text)
    numbers = re.findall(r"Bài\s*(\d+):", text)

    return [(numbers[i], contents[i + 1].strip()) for i in range(len(numbers))]


# ================== 3. CREATE FILES ==================
def create_files(problems):
    for number, content in problems:
        filename = f"Bai{number}.py"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(generate_code(content))

        print(f"✔ Đã tạo {filename}")


# ================== 4. GIT ==================
def get_current_branch():
    branch = os.popen("git branch --show-current").read().strip()
    return branch if branch else "master"


def push_to_github():
    print("🚀 Đang push lên GitHub...")

    os.system("git add .")
    os.system(f'git commit -m "Auto code {datetime.now()}"')

    branch = get_current_branch()
    print(f"👉 Đang push branch: {branch}")

    os.system(f"git push origin {branch}")

    print("✅ Hoàn tất push")


# ================== MAIN ==================
if __name__ == "__main__":
    input_text = """
    Bài 4: Viết chương trình nhập một số nguyên dương và kiểm tra chia hết cho 2 hoặc 3.
    Bài 5: Viết chương trình giải phương trình bậc 2.
    """

    problems = split_problems(input_text)
    create_files(problems)

    if input("Push lên GitHub không? (y/n): ").lower() == "y":
        push_to_github()