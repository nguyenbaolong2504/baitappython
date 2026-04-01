from git import Repo
from datetime import datetime
import os

repo_path = r"D:\python"

repo = Repo(repo_path)

repo.git.add(all=True)

# commit
if repo.head.is_valid():
    repo.index.commit("Auto commit " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
else:
    repo.index.commit("First commit")

# remote
try:
    origin = repo.remote(name='origin')
except:
    origin = repo.create_remote('origin', 'https://github.com/nguyenbaolong2504/baitappython.git')

# push
try:
    origin.push()
except:
    repo.git.push("--set-upstream", "origin", "main")

print("✅ Đã push thành công!")