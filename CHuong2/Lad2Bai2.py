a = input("Nhập số nguyên: ")
print("Số vừa nhập:", a)
b = input("Nhập số nguyên: ")
print("Số vừa nhập:", b)
c = input("Nhập số nguyên: ")
print("Số vừa nhập:", c)
if(int(a)+int(b))>int(c) and (int(a)+int(c))>int(b) and (int(b)+int(c))>int(a):
    print("3 số vừa nhập có thể tạo thành 1 tam giác")
else: print("3 số vừa nhập không thể tạo thành 1 tam giác")  
