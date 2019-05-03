#waktu

import calendar
import datetime
import time


jam1 = time.localtime()
jam2 = datetime.datetime.now()

tanggal1 = datetime.datetime.now()
tanggal2 = datetime.date.today()

print("")
print("tanggal")
print("tanngal = ", tanggal1.day) 
print("bulan = ", tanggal1.month)
print("tahun = ", tanggal1.year)
print("")
print("")
print("jam = ", jam2.hour)
print("menit = ", jam2.minute)
print("detik = ", jam2.second)
