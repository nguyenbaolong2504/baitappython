from git import Repo
import os
from datetime import datetime

# Đường dẫn tới folder project
repo_path = r"D:\python\Baitap_NopThay\auto-code-python"

repo = Repo(repo_path)

# Add tất cả file
repo.git.add(all=True)

# Commit với thời gian
commit_message = "Auto commit: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
repo.index.commit(commit_message)

# Push lên GitHub
origin = repo.remote(name='origin')
origin.push()

print("✅ Đã push code lên GitHub!")