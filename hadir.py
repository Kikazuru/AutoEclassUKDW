import Module.jadwal as jadwal
import Module.presensi as presensi
import getpass

jadwal = jadwal.Jadwal()
jadwalHariIni = jadwal.hari_ini()

data = jadwal.loadProfile()
    
if data:
    username, password = data
else:
    username = input("Username : ")
    password = getpass.getpass(prompt='Password : ')
    
    if input("Remember (y/n)? : ") in "yY":
        jadwal.saveProfile(username,password)


if jadwal.isEmpty():
    user = presensi.Eclass(username, password)

    user.login()
    jadwal.build_jadwal(user.scrapJadwalEclass())

if jadwalHariIni:
    matkulHariIni = jadwal.matkulHariIni()
    
    if matkulHariIni:
        user = presensi.Eclass(username, password)
        user.login()
        if not user.presensi(matkulHariIni):
            print("presensi belum dibuka!")
        user.closeBrowser()
    else:
        print("Saat ini belum ada kuliah")
else:
    print("Hari ini anda tidak ada kuliah :))")