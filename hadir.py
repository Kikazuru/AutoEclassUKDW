import jadwal
import presensi

jadwalHariIni = jadwal.Jadwal().hari_ini()

if jadwalHariIni:
    matkulHariIni = jadwal.matkul()
    if matkulHariIni:
        harris = presensi.PresensiEclass("NIM", "password")
        harris.login(matkulHariIni)
        harris.presensi()
        harris.closeBrowser()
    else:
        print("Saat ini belum ada kuliah / presensi belum dibuka!")
else:
    print("Hari ini anda tidak ada kuliah :))")