import csv
import os
from re import A 
import sys
import sqlite3

#Peminjaman dan pengembalian buku yang disewakan
#CREATE
print("Menu Pilih buat data")
while True:
    print("1. Buku Pelajaran")
    print("2. Komik")
    print("3. Novel")
    print("0. lanjut pinjam buku")

    pilihan = int(input("Pilih menu : "))
    if pilihan == 1:
        conn = sqlite3.connect('buku_pelajaran.db')
        a = """CREATE TABLE mahasiswa1(KODE INT NOT NULL, JUDUL TEXT NOT NULL, PENGARANG TEXT NOT NULL, TAHUN_TERBIT INT NOT NULL, TGL_PEMINJAMAN VARCHAR NOT NULL)"""
        conn.execute(a)
        conn.close()
        print("Success")
    elif pilihan == 2:
        conn = sqlite3.connect('komik.db')
        b = """CREATE TABLE mahasiswa2(KODE INT NOT NULL, JUDUL TEXT NOT NULL, PENGARANG TEXT NOT NULL, TAHUN_TERBIT INT NOT NULL, TGL_PEMINJAMAN VARCHAR NOT NULL)"""
        conn.execute(b)
        conn.close()
        print("Success")
    elif pilihan == 3:
        conn = sqlite3.connect('novel.db')
        c = """CREATE TABLE mahasiswa3(KODE INT NOT NULL, JUDUL TEXT NOT NULL, PENGARANG TEXT NOT NULL, TAHUN_TERBIT INT NOT NULL, TGL_PEMINJAMAN VARCHAR NOT NULL)"""
        conn.execute(c)
        conn.close()
        print("Success")

    else:
        pilihan == 0
        print("Menu Pilihan")
        while True:
            print("1. Buku Pelajaran")
            print("2. Komik")
            print("3. Novel")
            print("4. Mengembalikan buku")
            
            pilihan = int(input("Pilih menu : "))
            if pilihan == 1:
                lagi = "y"
                while lagi == "y":
                    print("1. 553 = Judul : Dasar-dasar Teknik Informatika, Pengarang : Novega Pratama Adiputra, Tahun Terbit : 2020")
                    print("2. 235 = Judul : Pengantar Teknologi Informasi, Pengarang : Buhori Muslim, Tahun Terbit : 2017")
                    print("3. 112 = Judul : Pengantar Teknologi Informatika dan Komunikasi Data, Pengarang : Bagaskoro, Tahun Terbit : 2019")
                    conn = sqlite3.connect("buku_pelajaran.db")
                    pilih = int(input("pilih menu : "))
                    if pilih == 1:
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")
                        print("Maksimal pengembalian 3 hari!")
                        a = ("""INSERT INTO mahasiswa1(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Dasar-dasar Teknik Informatika","Novega Pratama Adiputra",2020,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(a)
                        conn.commit()
        
                        cursor.execute("SELECT * FROM mahasiswa1")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break

                    elif pilih == 2:
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")
                        b = ("""INSERT INTO mahasiswa1(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Pengantar Teknologi Informasi","Buhori Muslim",2017,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(b)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa1")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break

                    elif pilih == 3: 
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")   
                        c = ("""INSERT INTO mahasiswa1(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Pengantar Teknologi Informatika dan Komunikasi Data","Bagaskoro",2019,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(c)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa1")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break
            elif pilihan == 2:
                lagi = "y"
                while lagi == "y":
                    print("1. 223 = Judul : Tokyo Ghoul, Pengarang : Sui Ishida, Tahun Terbit : 2014")
                    print("2. 529 = Judul : One Piece, Pengarang : Oda Eiichiro, Tahun Terbit : 1997")
                    print("3. 325 = Judul : Superman, Pengarang : DC Comics, Tahun Terbit : 1938")
                    conn = sqlite3.connect("komik.db")
                    pilih = int(input("pilih menu : "))
                    if pilih == 1:
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")
                        print("Maksimal pengembalian 3 hari!")
                        a = ("""INSERT INTO mahasiswa2(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Tokyo Ghoul","Sui Ishida",2014,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(a)
                        conn.commit()
        
                        cursor.execute("SELECT * FROM mahasiswa2")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break

                    elif pilih == 2:
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")
                        b = ("""INSERT INTO mahasiswa2(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"One Piece","Oda Eiichiro",1997,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(b)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa2")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break

                    elif pilih == 3: 
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")   
                        c = ("""INSERT INTO mahasiswa2(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Superman","DC Comics",1938,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(c)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa2")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break
            elif pilihan == 3:
                lagi = "y"
                while lagi == "y":
                    print("1. 123 = Judul : Lebih Senyap Dari Bisikan, Pengarang : Andina Dwifatma, Tahun Terbit : 2021")
                    print("2. 666 = Judul : Ziarah, Pengarang, Pengarang : Iwan Simatupang, Tahun Terbit : 1969")
                    print("3. 354 = Judul : Bumi Manusia , Pengarang : Pramoedya Ananta Toer, Tahun Terbit : 1980")
                    conn = sqlite3.connect("novel.db")
                    pilih = int(input("pilih menu : "))
                    if pilih == 1:
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")
                        print("Maksimal pengembalian 3 hari!")
                        a = ("""INSERT INTO mahasiswa3(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Lebih Senyap Dari Bisikan","Andina Dwifatma",2021,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(a)
                        conn.commit()
        
                        cursor.execute("SELECT * FROM mahasiswa3")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break

                    elif pilih == 2:
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")
                        b = ("""INSERT INTO mahasiswa3(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Ziarah","Iwan Simatupang",1969,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(b)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa3")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break

                    elif pilih == 3: 
                        kode_baru = input("Tambah kode : ")
                        peminjaman_baru = input("Tambah tanggal pinjam, contoh (23 mei 2022) : ")   
                        c = ("""INSERT INTO mahasiswa3(KODE,JUDUL, PENGARANG, TAHUN_TERBIT, TGL_PEMINJAMAN) VALUES ('{}',"Bumi Manusia","Pramoedya Ananta Toer",1980,'{}');""".format(kode_baru,peminjaman_baru))
                        cursor = conn.cursor()
                        cursor.execute(c)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa3")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break
            else:
                lagi = "y"
                while lagi == "y":
                    print("Menu Kembalikan")
                    print("1. Buku Pelajaran")
                    print("2. Komik")
                    print("3. Novel")
                    print("0. Keluar")
                    
                    pilihan = int(input("Pilih menu : "))
                    if pilihan == 1:
                        conn = sqlite3.connect("buku_pelajaran.db")
                        print("Kembalikan buku")
                        kode = int(input("masukkan kode: "))
                        a = ("""DELETE FROM mahasiswa1 where kode = '{}';""".format(kode))
                        cursor = conn.cursor()
                        cursor.execute(a)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa1")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break
                    elif pilihan == 2:
                        conn = sqlite3.connect("komik.db")
                        print("Kembalikan buku")
                        kode = int(input("masukkan kode: "))
                        b = ("""DELETE FROM mahasiswa2 where kode = '{}';""".format(kode))
                        cursor = conn.cursor()
                        cursor.execute(b)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa2")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break
                    elif pilihan == 3:
                        conn = sqlite3.connect("novel.db")
                        print("Kembalikan buku")
                        kode = int(input("masukkan kode: "))
                        c = ("""DELETE FROM mahasiswa3 where kode = '{}';""".format(kode))
                        cursor = conn.cursor()
                        cursor.execute(c)
                        conn.commit()

                        cursor.execute("SELECT * FROM mahasiswa3")
                        lagi = input("Input lagi (y/t) : ")
                        if lagi == 't':
                            print("Data sudah masuk")
                            for x in cursor.fetchall():
                                print(x)
                                break
                   
                
                        
    
        
        

