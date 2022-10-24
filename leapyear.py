import time

tahun = int(input("input tahun: "))

time.sleep(3)

if (tahun %400 == 0) and (tahun %100 == 0):
	print("{0} adalah tahun kabisat".format(tahun))
elif (tahun %4 == 0) and (tahun %100 != 0):
	print("{0} adalah tahun kabisat :)".format(tahun))
else: print("{0} bukanlah tahun kabisat :(".format(tahun))

time.sleep(3)

