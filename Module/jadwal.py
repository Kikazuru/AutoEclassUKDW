from datetime import datetime
from json import load, dump
import os


class Jadwal:
    script_dir = os.path.dirname(__file__)
    abs_path = os.path.join(script_dir, "../Data_File/")
    
    def __init__(self):
        self.days =["SENIN", "SELASA", "RABU", "KAMIS", 
                "JUMAT", "SABTU", "MINGGU"] 
        
        with open(self.abs_path + "jadwal.json", "r") as file_jadwal:
            try:
                self.jadwal = load(file_jadwal)
            except:
                self.jadwal = {}
    
    def isEmpty(self):
        return self.jadwal == {}
    
    def loadProfile(self):
        try:
            with open(self.abs_path + "profile.json", "r") as profile:
                data = load(profile)
                username = data["username"]
                password = data["password"]
                return (username,password)
        except:
            return False
    
    def saveProfile(self, username, password):
        with open(self.abs_path + "profile.json", "w") as profile:
            data = {"username":username, "password":password}
            dump(data, profile)
    
    def hari_ini(self):
        now = datetime.weekday(datetime.today())
        today = self.days[now]

        if today in self.jadwal:
            return self.jadwal[today]
        else:
            return False
        
    def matkulHariIni(self):
        jadwalHariIni = self.hari_ini()
        if jadwalHariIni:
            for kode, value in jadwalHariIni.items():
                mulai = value["mulai"]
                selesai = value["selesai"]
                
                waktu_mulai = datetime.strptime(mulai,'%H:%M').time()
                now = datetime.now().time()
                waktu_selesai = datetime.strptime(selesai,'%H:%M').time()
                
                if waktu_mulai < now < waktu_selesai:
                    return kode
            
        return False

            
    def show_jadwal(self):
        if self.jadwal:
            print("Jadwal Anda adalah : ")
            for hari in self.days:
                if hari in self.jadwal:
                    print(f"{hari}")
                    daftar = self.jadwal[hari]
                    for i, matkul in enumerate(daftar):
                        nama = daftar[matkul]['nama']
                        mulai = daftar[matkul]['mulai']
                        selesai = daftar[matkul]['selesai']
                        print(f"{i + 1}. {matkul} | {mulai}-{selesai} |  {nama} ")
        else:
            print("Jadwal kosong!")
        
        print("="*22)
            
            
    def tambah_jadwal(self, hari_matkul, kode_matkul, 
                    nama_matkul, mulai, selesai):
        with open(self.abs_path + "jadwal.json", "w") as file_jadwal:
            if hari_matkul in self.jadwal:
                self.jadwal[hari_matkul][kode_matkul] = {"nama":nama_matkul, "mulai":mulai, "selesai":selesai}
            else:
                self.jadwal[hari_matkul] = {kode_matkul : {"nama":nama_matkul, "mulai":mulai, "selesai":selesai}}  
                    
            dump(self.jadwal, file_jadwal)
        
    def hapus_jadwal(self, kode_hapus):
        with open(self.abs_path + "jadwal.json", "w") as file_jadwal:
            hari = None
            for hari in self.jadwal:
                if kode_hapus in self.jadwal[hari]:
                    break
                else:
                    hari = None
            if hari:
                if len(self.jadwal[hari]) == 1:
                    del self.jadwal[hari]
                else:
                    del self.jadwal[hari][kode_hapus]
            else:
                return False
            
            dump(self.jadwal, file_jadwal)
            return hari
    
    def build_jadwal(self, dict_jadwal):
        self.jadwal = dict_jadwal
        with open(self.abs_path + "jadwal.json", "w") as file_jadwal:
            dump(self.jadwal, file_jadwal)
