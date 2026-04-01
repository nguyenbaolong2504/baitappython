n = int(input("Nhập số nguyên dương: "))

if n>=20:
    print("nhap lai so nguyen!")
else:
    for i in range(1,n+1):
        if i%5==0 or i%7==0:
         print(i)
