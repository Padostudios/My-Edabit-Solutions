import time
import datetime 

print("Lütfen 3 saniye sonra yazinizi yaziniz")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("GO!")
time.sleep(0.2)

önceki = datetime.datetime.now()
yazi = input("Ne yazmak istiyorsun üstad ? ")
sonraki = datetime.datetime.now()

hiz = sonraki-önceki
hizsaniye = round(hiz.total_seconds(),2)
saniye_basina_harf = round(len(yazi)/hizsaniye,1)

print("{} saniyede yazinizi yazdiniz".format(hizsaniye))
print("Saniye basina {} harf yazdiniz".format(saniye_basina_harf))
