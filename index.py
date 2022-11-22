import os
import time
import pandas as pd
import numpy as np

diamond = [14,"14(13+1) Diamonds", 3999     ],
[14,"42(38+4) Diamonds",           10999    ],
[86,"86(78+8) Diamonds",           19999    ],
[172,"172(156+16) Diamonds",       39999    ],
[257,"257(234+23) Diamonds",       59999    ],
[344, "344(312+32) Diamonds",      80000    ],
[429, "429(384+46) Diamonds",      100000   ]

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
cart = []
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

def tes():
    print(cart)

def member():
    print(df_game.to_string(index=False))
    print(50*"=")
    KodeGame = int(input("Masukkan KodeGame : "))
    Return,Game = check_kodegame(KodeGame)

    if Return == True:
        cart.append(Game)
        cart.append(111111)
        cart.append(222222)
        cart.append(1000000)
        clear_screen()
        tes()
    else:
        print("KodeGame tidak ada !")
        time.sleep(1)
        clear_screen()
        member()



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
member()


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