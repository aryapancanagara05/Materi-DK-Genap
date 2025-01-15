#membuat program menghitung nilai akhir

nilai_tugas=int(input("masukan nilai tugas: "))
nilai_UTS=int(input("masukan nilai UTS: "))
nilai_UAS=int(input("masukan nilai UAS: "))

nilai_akhir= 30/100* nilai_UTS + 50/100* nilai_UAS + 20/100* nilai_tugas

print("nilai akhir :",nilai_akhir)

