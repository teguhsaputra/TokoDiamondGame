import os
import time
import pandas as pd
import numpy as np
from datetime import datetime
from tabulate import tabulate

def clear_screen():
    _ = os.system('cls')

df_login = pd.read_json('db_login.json')
df_game = pd.read_json('db_game.json')
df_diamond = pd.read_json('db_diamond.json')
df_penjualan = pd.read_csv("db_penjualan.csv")
cart = []
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
list_penjualan = []

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

def PrintStruk():
    lanjut = input("Apakan Anda ingin menyetak struk ? <y/n> ")
    if lanjut == "y" or lanjut == "Y":
        if os.path.isfile('struk.txt'):
            os.unlink('struk.txt')
        while 
        time.sleep(1)
        with open('struk.txt', 'w') as f:
            txt_print0 = '''
    DIAMOND GAME STORE MURAH NAMPOL
'''
            txt_print1 = 35*"="
            txt_print2 = "\nNama Game : {NameGame} \nID Game : {IdGame} \nDiamond : {Diamond} \nHarga : {Harga} \nUang Bayar : {UangBayar} \nUang Kembalian : {UangKembalian} \n".format(NameGame = cart[0], 
            IdGame = cart[1], Diamond = cart[2], Harga = cart[3], UangBayar = cart[4], UangKembalian = cart[5])
            txt_print3 = 35*"="
            txt_print4 = "\nTerimakasih Telah Membeli Diamond \nDi GAME STORE MURAH NAMPOL\n"
            txt_gabung = txt_print0+txt_print1+txt_print2+txt_print3+txt_print4
            f.write(txt_gabung)     
            print(txt_gabung)     
            # os.startfile("struk.txt", "print")
            Lanjut_Def()
    elif lanjut == "n" or lanjut == "N":
        Lanjut_Def()
    else:
        PrintStruk()
   

    # print("Nama Game : ",cart[0])
    # print("ID Game : ",cart[1])
    # print("Diamond : ",cart[2])
    # print("Harga : ",cart[3])
    # print(35*"=")
    # print("Uang Bayar : ", cart[4])
    # print("Kembalian Anda : ", cart[5])
    # print(35*"=")
    # print("Terimakasih Telah Membeli Diamond")
    # print("Di GAME STORE MURAH NAMPOL")

def Lanjut_Def():
    lanjut = input("Apakan Anda ingin membeli lagi ? <y/n> ")
    if lanjut == "y" or lanjut == "Y":
        cart.clear()
        clear_screen()
        member()            
    elif lanjut == "n" or lanjut == "N":
        clear_screen()
        login()
    else:
        Lanjut_Def()

def InputPenjualan():
    global df_penjualan

    list_penjualan = dict()

    list_penjualan["NameGame"] = [cart[0]]
    list_penjualan["IdGame"] = [cart[1]]
    list_penjualan["Diamond"] = [cart[2]]
    list_penjualan["Harga"] = [cart[3]]
    list_penjualan["TanggalBeli"] = [cart[4]]

    tmp = pd.DataFrame.from_dict(list_penjualan)

    df_penjualan = pd.concat([df_penjualan, tmp], ignore_index=True)
    df_penjualan.to_csv("db_penjualan.csv", index=False)

    # print(list_penjualan)
    # df_kirimdata = pd.DataFrame(list_penjualan)
    # df_kirimdata.to_csv('db_penjualan.csv')
    

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

        PrintStruk()

        # lanjut = input("Apakan Anda ingin cetak struk ? <y/n> ")
        # if lanjut == "y" or lanjut == "Y":
        #     # clear_screen()
        #     PrintStruk()            
        # elif lanjut == "n" or lanjut == "N":
        #     clear_screen()
        #     login()
        # else:
        #     Lanjut_Def()    

def Game_Def():
    data = pd.DataFrame(df_game)
    print(tabulate(data, headers='keys', tablefmt='psql',showindex=False))
    # print(df_game.to_string(index=False))
    # print(50*"=")
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
    data = pd.DataFrame(df_diamond)
    print(tabulate(data, headers='keys', tablefmt='psql', showindex=False))
    # print(df_diamond.to_string(index=False))
    # print(50*"=")
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

def print_penjualan():
    clear_screen()
    data = pd.DataFrame(df_penjualan)
    print(tabulate(data, headers='keys', tablefmt='psql'))
    print()
    print("{:>80}".format("Total Pendapatan : " + str(data['Harga'].sum())))
    print('''
Menu : 
[1] Cetak Laporan Keuangan
[2] Kembali Ke Menu
''')
    lanjut = int(input("Pilih menu <1/2> ?  "))
    if lanjut == 1:
        os.startfile("db_penjualan.csv", "print")
        print_penjualan()            
    elif lanjut == 2:
        clear_screen()
        admin()
    else:
        clear_screen()
        print_penjualan()

def admin():
    clear_screen()
    print('''
            SELAMAT DATANG 
                ADMIN
          SILAHKAN PILIH MENU
========================================
[1] Print Laporan Penjualan
[2] Logout
''')
    menu = int(input("Pilih Menu : "))
    if menu == 1:
        print_penjualan()
    elif menu  == 2:
        login()
    else:
        admin()
def login():
    clear_screen()
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

# print_penjualan()

# print_penjualan()
# InputPenjualan()