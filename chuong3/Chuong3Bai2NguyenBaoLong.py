n= int(input("Nhap n:"))
if(n>10):
    print("nhap vao so nho hon 10")
else:
    for i in range(1,n+1):
        if i %2==0:
            print(i)