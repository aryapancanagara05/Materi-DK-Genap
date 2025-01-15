#membuat program untuk menentukan hadiah dengan menerima inputan pelanggan

print("program bonus toko")

nilai=int(input("masukan nilai pembelian pelanggan :"))

if nilai > 1500000 and nilai <= 5000000 :
    print("anda mendapatkan TV Bracket")
elif nilai >= 5000000:
    print("anda mendapatkan Sound Bar")
else:
    print("tidak ada bonus")