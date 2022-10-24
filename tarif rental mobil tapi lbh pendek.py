masuk = float(input("jam masuk: "))
keluar = float(input("jam keluar: "))

waktu = keluar - masuk
tarif = 200000

tarif = tarif + 10000 * (waktu - 12)
print(int(tarif))
