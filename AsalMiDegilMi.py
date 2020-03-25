def asalBul():
    flag=0
    print("Lütfen asal olup olmadıgını bulmak istediginiz sayiyi giriniz : ")
    try:
        a=int(input("Sayi : "))
    except(ValueError):
        print("Lütfen sadece sayi degeri giriniz")
    for i in range(2,a):
        if a&i==0:
            flag=1
        break
    if flag==1:
        print("Sayi asal degildir")
    else:
        print("Sayi asaldir")


asalBul()
        



