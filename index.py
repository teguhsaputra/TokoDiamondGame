import os
import time
import pandas as pd


diamond = [14,"14(13+1) Diamonds", 3999     ],
[14,"42(38+4) Diamonds",           10999    ],
[86,"86(78+8) Diamonds",           19999    ],
[172,"172(156+16) Diamonds",       39999    ],
[257,"257(234+23) Diamonds",       59999    ],
[344, "344(312+32) Diamonds",      80000    ],
[429, "429(384+46) Diamonds",      100000   ]

def clear_screen():
    _ = os.system('cls')


def Login():
    
    print('''
             SELAMAT DATANG DI 
        DIAMOND GAME STORE MURAH NAMPOL
              SILAHKAN LOGIN
==============================================
''')
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    akses = 2

    if(username == "member" and password == "member" and akses == 1):
        Member()
    elif(username == "admin" and password == "admin" and akses == 2):
        Admin()
    else:
        print()
        print("Password Salah, Silahkan Login kembali !")
        time.sleep(3)
        clear_screen()
        Login()

def Member():
    print('''
Pilih Game 
1. Mobile Legends
2. Free Fire
3. PUBG
==================
''')
    keranjang = []
    pilihgame = int(input("Masukkan Jenis Game : "))
    keranjang.insert = [pilihgame]

    idgame = input("Masukkan ID Game : ")
    keranjang.insert = [idgame]

    pilihdiamond = int(input("Masukkan Jumlah Diamond : "))
    keranjang.insert = [pilihdiamond]
    clear_screen()



def Admin():
    dataHarga = {
        "Diamond" : [14,42,86,172,257,347,429],
        "Harga" : [3999,10999,19999,39999,59999,80000,100000]
    }
    showData = pd.DataFrame(dataHarga)
    print(showData)
    print()
    pilihdiamond = int(input("Pilih Diamond : "))
    hargaDiamond = dataHarga["Harga"][pilihdiamond]
    print("Harga Diamond : ",hargaDiamond)
    jumlahBayar = int(input("Masukkan Jumlah Bayar : "))
    total = jumlahBayar - hargaDiamond
    print(50*"=")
    print("Kembalian = ", total)
    print("Terimakasih Telah Membeli Diamond Kami")
#Login()
Admin()

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