def UnluHarfleriBul():
    unluler = ["a","e","i","ı","o","ö","u","ü","A","E","I","İ","U","Ü","O","Ö"]
    n = input("cümlenizi giriniz : ")
    sayac = 0
    for i in n:
        if i in unluler:
            sayac = sayac +1 
    return sayac



print(UnluHarfleriBul())