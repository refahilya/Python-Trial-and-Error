try:
    file = open("d:/myfile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Maaf, file tidak ditemukan")
