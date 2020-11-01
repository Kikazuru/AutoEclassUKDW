import Module.jadwal as jadwal
import Module.presensi as presensi
import getpass

jadwal = jadwal.Jadwal()
jadwalHariIni = jadwal.hari_ini()
        
if jadwalHariIni:
    matkulHariIni = jadwal.matkul()
    
    if matkulHariIni:
        data = jadwal.loadProfile()
        
        if data:
            username, password = data
        else:
            username = input("Username : ")
            
            password = getpass.getpass(prompt='Password : ')
            
            if input("Remember (y/n)? : ") in "yY":
                jadwal.saveProfile(username,password)
            
        harris = presensi.PresensiEclass(username, password)
        harris.login(matkulHariIni)
        if not harris.presensi():
            print("presensi belum dibuka!")
        harris.closeBrowser()
    else:
        print("Saat ini belum ada kuliah")
else:
    print("Hari ini anda tidak ada kuliah :))")