import os
from getch import getch

ekran_silme = 0

def ekranTemizle():
    os.system('clear')

def baslangic():
    ekranTemizle()

    print("OBO PY Edition 0.1 Beta - https://github.com/furcanomer/obo-py\n--------------------------------------------------------------------------------")
    print("Saga gitmek icin 'D' tusuna basin.\tYeniden baslamak icin 'R' tusuna basin.\n")
    print("Sola gitmek icin 'A' tusuna basin.\tOyunu kapatmak icin 'X' tusuna basin")
    print("--------------------------------------------------------------------------------\n")

def yeniden_Baslangic():
    global ekran_silme
    ekran_silme = 1


baslangic()

adim = 0

while True:
    if ekran_silme == 1:
        baslangic()
        ekran_silme = 0
        adim = 0

    tus = getch()

    if tus == 'd' or tus == 'D':
        
        if adim < 19:
            print("--> ", end='')
            adim += 1

        else:
            print("\a")

    elif tus == 'a' or tus == 'A':

        if adim > 0:

            print("\n<--", end = '')

            for i in range(adim,1,-1):
                print(" <--", end='')
            
            print("\n")

            adim = 0

        elif adim == 0:
            print("\a")
            continue

    elif tus == 'x' or tus == 'X':
        ekranTemizle()
        break

    elif tus == 'R' or tus == 'r':
        yeniden_Baslangic()
        continue

    else:
        continue