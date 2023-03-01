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
    """
    Eğer dosya konsoldan açıldıysa konsolla alakalı yazıların ekrandan silinmeisini sağlar.
    Ekranın sadece oyun ile alakalı olmasını istiyorum.
    """

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
"""
adim değişkeni sayseinde kaç adet sağa gittiğimi ölçüyorum ki programa sola git dediğimde sağa gittiğim kadar da sola gitsin.
ekran_silme değişkenini sıfır yaptım ki ekran silme koşulu çalışmasın.
oyuncu oyuna baştan başlamak istediği zaman ekran_silme = 1 oluyor ve koşul sağlanıyor ve hemen ardından geri 0 oluyor.	
		
"""

while True:
    if ekran_silme == 1:
        baslangic()
        ekran_silme = 0
        adim = 0

    tus = readchar.readkey()
    """
    readkey() ile istedim ki ekrana D harfi basılmasın.
    """

    if tus == 'd' or tus == 'D':
        
        if adim < 19: # ok sayısını 19 ile sınırlayan kod
            print("--> ", end='', flush=True)
            """
            ekrana "-->" stringini bas ama varsayılan olarak satır atlama
            yani boş karakter bas ve ekrana ne basacaksan anında bas (flush=True)
            """
            adim += 1 # her sağa gittiğimizde adim 1 artıyor

        else:
            birsey_yapma()
            # ok sınırıda rağmen hala sağa gidilmeye çalışılıyorsa sistem uyarı sesi verecek

    elif tus == 'a' or tus == 'A':

        if adim > 0: # eğer sağa gittiysek

            print("\n<--", end = '', flush=True)

            for i in range(adim,1,-1):
                """
                for döngüsü sayesinde sağa gittiğimiz adim sayisi kadar
				sola gidebiliyoruz.
				"""
                print(" <--", end='')
            
            print("\n") # sola gittikten sonra 2 satır aşağı atlıyoruz.

            adim = 0
            """
            Sola gittikten sonra adimi sıfırlıyoruz
			Sıfırlamazsak sola gitme tuşuna bastığımızda, eski sağ adim sayisi kadar sola gideriz.
			"""

        elif adim == 0: # // sola gitme tuşuna bastık evet ama eğer hiç sağa gitmemişsek...?
            birsey_yapma() # ...o zaman hiçbir şey yapmıyoruz ve sistem uyarı sesi çıkarıp
            continue # while döngüsünün başına dönüyoruz.

    elif tus == 'x' or tus == 'X':
        ekranTemizle()
        break

    elif tus == 'R' or tus == 'r':
        yeniden_Baslangic()
        continue

    else:
        continue # A - D  tuşlarına basılmadıysa hiçbirşey yapılmıyor ve while döngüsünün başına dönüyoruz
