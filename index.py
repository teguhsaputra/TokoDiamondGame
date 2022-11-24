import os
import time
import pandas as pd
import numpy as np
from datetime import datetime

def clear_screen():
    _ = os.system('cls')


# def Login():
    
#     print('''
#              SELAMAT DATANG DI 
#         DIAMOND GAME STORE MURAH NAMPOL
#               SILAHKAN LOGIN
# ==============================================
# ''')
#     username = input("Masukkan Username : ")
#     password = input("Masukkan Password : ")
#     akses = 2

#     if(username == "member" and password == "member" and akses == 1):
#         Member()
#     elif(username == "admin" and password == "admin" and akses == 2):
#         Admin()
#     else:
#         print()
#         print("Password Salah, Silahkan Login kembali !")
#         time.sleep(3)
#         clear_screen()
#         Login()

# def Member():
#     print('''
# Pilih Game 
# 1. Mobile Legends
# 2. Free Fire
# 3. PUBG
# ==================
# ''')
#     keranjang = []
#     pilihgame = int(input("Masukkan Jenis Game : "))
#     keranjang.insert = [pilihgame]

#     idgame = input("Masukkan ID Game : ")
#     keranjang.insert = [idgame]

#     pilihdiamond = int(input("Masukkan Jumlah Diamond : "))
#     keranjang.insert = [pilihdiamond]
#     clear_screen()



# def Admin():
#     dataHarga = {
#         "Diamond" : [14,42,86,172,257,347,429],
#         "Harga" : [3999,10999,19999,39999,59999,80000,100000]
#     }
#     showData = pd.DataFrame(dataHarga)
#     print(showData)
#     print()
#     pilihdiamond = int(input("Pilih Diamond : "))
#     hargaDiamond = dataHarga["Harga"][pilihdiamond]
#     print("Harga Diamond : ",hargaDiamond)
#     jumlahBayar = int(input("Masukkan Jumlah Bayar : "))
#     total = jumlahBayar - hargaDiamond
#     print(50*"=")
#     print("Kembalian = ", total)
#     print("Terimakasih Telah Membeli Diamond Kami")
#Login()
# Admin()

df_login = pd.read_json('db_login.json')
df_game = pd.read_json('db_game.json')
df_diamond = pd.read_json('db_diamond.json')
cart = []
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print(df_login["Username"])
# temp_user = []
def check_login(username,password):
    for dts in range(0, df_login["Username"].size):
        if df_login["Username"].values[dts] == username and df_login["Password"].values[dts] == password:
            # temp_user.append([df_login["Username"][1],df_login["Password"][1],df_login["HakAkses"][1]])
            # print(temp_user)
            return True, df_login["HakAkses"].values[dts]
            break
    return False, 404

def check_kodegame(KodeGame):
    for kdg in range(0, df_game["KodeGame"].size):
        if df_game["KodeGame"].values[kdg] == KodeGame:
            # temp_user.append([df_login["Username"][1],df_login["Password"][1],df_login["HakAkses"][1]])
            # print(temp_user)
            return True, df_game["Game"].values[kdg]
            break
    return False, 404

def check_kodediamond(KodeDiamond):
    for kd in range(0, df_diamond["KodeDiamond"].size):
        if df_diamond["KodeDiamond"].values[kd] == KodeDiamond:
            # temp_user.append([df_login["Username"][1],df_login["Password"][1],df_login["HakAkses"][1]])
            # print(temp_user)
            return True, df_diamond["Diamond"].values[kd], df_diamond["Harga"].values[kd]
            break
    return False, 404, 0

def Print():
    print("Nama Game : ",cart[0])
    print("ID Game : ",cart[1])
    print("Diamond : ",cart[2])
    print("Harga : ",cart[3])
    print(35*"=")
    print("Uang Bayar : ", cart[4])
    print("Kembalian Anda : ", cart[5])
    print(35*"=")
    print("Terimakasih Telah Membeli Diamond")
    print("Di GAME STORE MURAH NAMPOL")

def Total_Def():
    print("Nama Game : ",cart[0])
    print("ID Game : ",cart[1])
    print("Diamond : ",cart[2])
    print("Harga : ",cart[3])
    print(35*"=")
    UangBayar = int(input("Uang Bayar : "))
    if UangBayar < cart[3]:
        print("Uang Bayar Kurang !")
        time.sleep(1)
        clear_screen()
        Total_Def()
    else:
        Kembalian = UangBayar - cart[3]
        cart.append(UangBayar)
        cart.append(Kembalian)
        print("Kembalian Anda : ", Kembalian)
        print(35*"=")
        print("Terimakasih Telah Membeli Diamond")
        print("Di GAME STORE MURAH NAMPOL")
        print(35*"=")
        lanjut = input("Apakan Anda ingin membeli lagi ? <y/n> ")
        if lanjut == "y":
            cart.clear()
            clear_screen()
            member()            
        else:
            clear_screen()
            login()
        


def Game_Def():
    print(df_game.to_string(index=False))
    print(50*"=")
    KodeGame = int(input("Masukkan KodeGame : "))
    ReturnKodeGame,Game = check_kodegame(KodeGame)

    if ReturnKodeGame == True:
        cart.append(Game)
        clear_screen()
        IdGame = int(input("Masukkan ID Game : "))
        cart.append(IdGame)
        clear_screen()
    else:
        print("KodeGame tidak ada !")
        time.sleep(1)
        clear_screen()
        Game_Def()

def Diamond_Def():
    print(df_diamond.to_string(index=False))
    print(50*"=")
    KodeDiamond = int(input("Masukkan KodeDiamond : "))
    ReturnKodeDiamond,Diamond,Harga = check_kodediamond(KodeDiamond)
    if ReturnKodeDiamond == True:
        cart.append(Diamond)
        cart.append(Harga)
        cart.append(dt_string)
        clear_screen()
    else:
        print("KodeDiamond tidak ada !")
        time.sleep(1)
        clear_screen()
        Diamond_Def()


def member():
    Game_Def()
    Diamond_Def()
    Total_Def()

def admin():
    print("Ini halaman admin")

def login():
    print('''
             SELAMAT DATANG DI 
        DIAMOND GAME STORE MURAH NAMPOL
              SILAHKAN LOGIN
==============================================
''')
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    Return,HakAkses = check_login(username, password)
    
    if Return == True:
        if HakAkses == 0:
            print("Berhasil Login !")
            time.sleep(1)
            clear_screen()
            member()
        else:
            print("Berhasil Login !")
            time.sleep(1)
            clear_screen()
            admin()
    else:
        print("Username/Password Salah !")
        time.sleep(1)
        clear_screen()
        login()

            
clear_screen()
login()


# for dts in range(0, df_login["Username"].size):
#     if df_login["Username"].values[dts] != username or df_login["Password"].values[dts] == password:
#         print("Username / Password Salah")
#         break
#     elif df_login["Username"].values[dts] == username and df_login["Password"].values[dts] == password:
#         print("ada datanya")
#         if df_login["HakAkses"].values[dts] == 0:
#             print("Ini Halaman Member")
#             break
#             # Admin()
#         else:
#             # Member()
#             print("ini Halaman Admin")
#             break
#     else:
#         error = "Username/Password salah!"
# print(error)
    # print(df_login.values[dts])

#     def MobileLegends():
#         id_ml = int(input("Masukkan ID : "))
#         server_ml = int(input("Masukkan Server : "))
#         nominal_diamond =     

# print('''
#             SELAMAT DATANG DI 
#         DIAMOND GAME STORE MURAH NAMPOL
# ''')
# nama = input("MASUKAN NAMA : ")
# id_game=input("MASUKAN ID GAME :")
# saldo=int(input("MASUKAN UANG  :"))
# print('''
# ------------------------------------------
# NO |          GAME                       |
# ------------------------------------------
# 1  | MOBILE LEGEND                       |
# 2  | CLASH OF CLANS                      |
# 3  | FREE FIRE                           |
# ------------------------------------------''')
# def pembeliangame():
#   print(f'''
#   ------------------------------------------------------
#                         {namagame}                  |
#   ------------------------------------------------------
#   1 | 50  DIAMOND   `                    |  Rp.10.000  |
#   2 | 100 DIAMOND                        |  Rp.20.000  |
#   3 | 500 DIAMOND                        |  Rp.30.000  |
#   ------------------------------------------------------
#   ''')
  
#   diamond = int(input("[1/2/3] Silahkan pilih jumlah diamond: "))
#   if diamond == 1:
#     dm = 100
#     harga = 10000
#     sisa_saldo = saldo - harga
#     print('''
#     ---------------------------------------
#                 DATA PEMBELIAN
#     ---------------------------------------
#     ''')
#     print("     Nama pembeli       =",nama)
#     print("     Game               =",namagame)
#     print("     Jumlah diamond     =",dm)
#     print("     Harga total        = Rp.",harga)
#     print("     Saldo tersisa      = Rp.",sisa_saldo)
#   elif diamond == 2:
#     dm = 300
#     harga = 20000
#     sisa_saldo = saldo - harga
#     print('''
#     ---------------------------------------
#                 DATA PEMBELIAN
#     ---------------------------------------
#     ''')
#     print("     Nama pembeli       =",nama)
#     print("     Game               =",namagame)
#     print("     Jumlah diamond     =",dm)
#     print("     Harga total        = Rp.",harga)
#     print("     Saldo tersisa      = Rp.",sisa_saldo)
#   elif diamond == 3:
#     dm = 500
#     harga = 30000
#     sisa_saldo = saldo - harga
#     print('''
#     ---------------------------------------
#                 DATA PEMBELIAN
#     ---------------------------------------
#     ''')
#     print("     Nama pembeli       =",nama)
#     print("     Game               =",namagame)
#     print("     Jumlah diamond     =",dm)
#     print("     Harga total        = Rp.",harga)
#     print("     Saldo tersisa      = Rp.",sisa_saldo)
#   else:
#     print("\nError!!!")
#     print("\nJumlah diamond tidak ditemukan!")

# game = int(input("[1/2/3] SILAHKAN PILIH GAME : "))

# if game == 1:
#   namagame = "MOBILE LEGEND"
#   pembeliangame()
# elif game == 2:
#   namagame = "CLASH OF CLANS"
#   pembeliangame()
# elif game == 3:
#   namagame = "FREE FIRE"
#   pembeliangame()
# else:
#   print("\nError!!!")
#   print("Game tidak ditemukan!")