import Module.jadwal as jadwal
import Module.presensi as presensi
import getpass
from os import system

jadwal = jadwal.Jadwal()


while True:
    system("cls")
    print("Menu Pilihan:")
    print("="*13)
    print("1.Presensi\n2.Buka Jadwal\n3.Tambah Jadwal\n4.Edit Jadwal\n5.Hapus Jadwal\n6.Keluar Program")
    print("="*13)
    pilih = input("Pilih: ")
    
    if pilih == "1":
        jadwalHariIni = jadwal.hari_ini()
        
        if jadwalHariIni:
            matkulHariIni = jadwal.matkulHariIni()
            
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
            
    elif pilih == "2":
        system("cls")
        jadwal.show_jadwal()
        
    elif pilih == "3":
        while True:
            system("cls")
            jadwal.show_jadwal()

            hari = input("Hari matakuliah\t: ")
            nama = input("Nama matakuliah\t: ")
            kode = input("Kode matakuliah\t: ")
            mulai = input("Waktu mulai\t: ")
            selesai = input("Waktu selesai\t: ")
            
            jadwal.tambah_jadwal(hari, kode, nama, mulai, selesai)
            if input("Tambah lagi? (y/n) : ") in "nN":
                break    
            
        
    elif pilih == "4":
        while True:
            system("cls")
            jadwal.show_jadwal()
            edit = input("Nama kode matakuliah yang akan diedit : ")

            cek = jadwal.hapus_jadwal(edit)
                
            if cek:
                print("Ubah menjadi: ")
                nama = input("Nama matakuliah\t: ")
                kode = input("Kode matakuliah\t: ")
                mulai = input("Waktu mulai\t: ")
                selesai = input("Waktu selesai\t: ")
                jadwal.tambah_jadwal(cek, kode, nama, mulai, selesai)
                print(f"Edit matakuliah Berhasil!")
            else:
                print(f"Kode tidak ada!")
               
            if input("Edit lagi? (y/n) : ") in "nN":
                break
            
            
    elif pilih == "5":
        while True:
            system("cls")
            jadwal.show_jadwal()
            
            edit = input("Nama kode matakuliah yang akan dihapus : ")
            
            if jadwal.hapus_jadwal(edit):
                print(f"Hapus matakuliah Berhasil!")
            else:
                print(f"Hapus matakuliah Gagal!")
            
            if input("Hapus lagi? (y/n) : ") in "nN":
                break
            
    elif pilih == "6":
        print("Goodbye :))")
        break
    
    input("press enter to continue...")
    
    
    