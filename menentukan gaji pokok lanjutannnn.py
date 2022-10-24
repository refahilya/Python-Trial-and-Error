#input duluu
code = input("Masukkan kode karyawan: ")
name = input("Masukkan nama karyawan: ")
gol = str(input("Masukkan golongan: "))
stat = input("Masukkan status(1: menikah, 2: belum menikah): ")
if stat == "1":
        anak = input("Masukkan jumlah anak: ")

#garis2
s = "=" * 35
t = "-" * 35

#pilgan ygy
if stat == "1":
        stat = "Menikah"
else:
        stat = "Belum Menikah"

#ini awalan struknya ges
print(s) 
print("STRUK RINCIAN GAJI KARYAWAN")
print(t)
print("Nama Karyawan : ", name, "(Kode : ", code, ")")
print("Golongan : ", gol)
print("Status Menikah : ", stat)
if stat == "Menikah":
        print("Jumlah Anak : ", anak)
print(t)

#conditionalnya nih kk
if gol == "A":
        gp = int(10000000)
        pot = float(2.5)
if gol == "B":
        gp = int(8500000)
        pot = float(2.0)
if gol == "C":
        gp = int(7000000)
        pot = float(1.5)
if gol == "D":
        gp = int(5500000)
        pot = float(1.0)

#hitung dulu gaji2nya
potx = (pot / 100) * gp
tp = 0.1 * gp
if stat == "Menikah":
        ta = 0.05 * gp
if stat == "Menikah":
        gk = gp + tp + (ta * int(anak))
else:
        gk = gp + tp
gb = gk - potx

#nah ini baru struk gaji
print("Gaji Pokok : Rp", gp)
print("Tunjangan Istri/Suami : Rp", int(tp))
if stat == "Menikah":
        print("Tunjangan Anak : Rp", int(ta)* int(anak))
print(t)
print("Gaji Kotor : Rp", int(gk))
print("Potongan (", pot, "%) : Rp", int(potx))
print(t)
print("Gaji Bersih : Rp", int(gb))
