import os
import readchar

ekran_silme = 0

def ekranTemizle():
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    ekran temizlemek için 
    eğer sistem ismi 'nt' (yani windows) ise "cls" kullan
    eğer sistem ismi 'nt' (yani windows) değilse
    yani unix benzeri bir sistemse "clear" kullan
    """

def baslangic():
    ekranTemizle()

    print("OBO PY Edition 1.0.1 - https://github.com/furcanomer/obo-py\n--------------------------------------------------------------------------------")
    print("Saga gitmek icin 'D' tusuna basin.\tYeniden baslamak icin 'R' tusuna basin.\n")
    print("Sola gitmek icin 'A' tusuna basin.\tOyunu kapatmak icin 'X' tusuna basin")
    print("--------------------------------------------------------------------------------\n")

def yeniden_Baslangic():
    global ekran_silme
    ekran_silme = 1

def birsey_yapma():
    print("\a", end='', flush=True)

baslangic()

adim = 0

while True:
    if ekran_silme == 1:
        baslangic()
        ekran_silme = 0
        adim = 0

    tus = readchar.readkey()

    if tus == 'd' or tus == 'D':
        
        if adim < 19:
            print("--> ", end='', flush=True)
            """
            ekrana "-->" stringini bas ama varsayılan olarak satır atlama
            yani boş karakter bas ve ekrana ne basacaksan anında bas (flush=True)
            """
            adim += 1

        else:
            birsey_yapma()

    elif tus == 'a' or tus == 'A':

        if adim > 0:

            print("\n<--", end = '', flush=True)

            for i in range(adim,1,-1):
                print(" <--", end='')
            
            print("\n")

            adim = 0

        elif adim == 0:
            birsey_yapma()
            continue

    elif tus == 'x' or tus == 'X':
        ekranTemizle()
        break

    elif tus == 'R' or tus == 'r':
        yeniden_Baslangic()
        continue

    else:
        continue
