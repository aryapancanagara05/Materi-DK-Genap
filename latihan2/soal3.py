#program membuat game tebak angka

angka=int(input("masukan angka yang ingin ditebak dari 0 - 20: "))
tebak_angka= 17
if angka == tebak_angka:
    print("tselamat anda memenangkan hadiah utama")
else:
    print("anda kalah, angka yang benar adalah",tebak_angka)

