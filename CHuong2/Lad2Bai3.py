import time 
x = time.localtime()
year = x[0]
s = input("Nhập năm sinh: ")    
tuoi = year - int(s)
print("Tuổi của bạn là:", tuoi)