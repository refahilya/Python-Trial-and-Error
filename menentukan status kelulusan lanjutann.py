
ha = False

while ha == False:
    bi = int(input("Masukkan nilai Bahasa Indonesia: "))
    ma = int(input("Masukkan nilai Matematika: "))
    ip = int(input("Masukkan nilai IPA: "))

    if bi < 0 or ma < 0 or ip < 0:
        print("Maaf input ada yang tidak valid")
    elif bi > 100 or ma > 100 or ip > 100:
        print("Maaf input ada yang tidak valid")
    else:
        if bi >= 60 and ma >= 60 and ip >= 60:
            ha = "LULUS"
            if ma <= 70:
                ha = "TIDAK LULUS"
            else:
                ha = "LULUS"
        else:
            ha = "TIDAK LULUS"
        print("Status kelulusan: ", ha)

if bi < 60:
    print("Nilai Bahasa Indonesia kurang dari 60")
if ip < 60:
    print("Nilai IPA kurang dari 60")
if ma < 70:
    print("Nilai Matematika kurang dari 70")
        
