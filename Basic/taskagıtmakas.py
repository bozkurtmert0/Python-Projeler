from random import randint

print("""*********************************************************
Taşı seçmek için 1'i
Kağıt seçmek için 2'yi
Makası seçmek için 3'ü    giriniz.
*********************************************************
""")
bitis=int(input("Kaç olan kazansın ? :"))
ai_skor=0
p_skor=0
while True:
    print("""*********************************************************
    Taşı seçmek için 1'i
    Kağıt seçmek için 2'yi
    Makası seçmek için 3'ü    giriniz.
    *********************************************************
    """)
    secimin=int(input("Seçiminizi giriniz:"))
    ai_secimi = randint(1, 3)

    if ai_secimi==1 : #Bilgisayarın Taşı seçtiği koşul
        if secimin==1:
            print("Berabere.")
        elif secimin==2:
            print("Kazandınız.")
            p_skor+=1
        elif secimin==3:
            print("Kaybettiniz.")
            ai_skor+=1
        else:
            print("Geçerli bir değer giriniz")
    elif ai_secimi==2:  #Bilgisayarın kağıt seçtiği durum
        if secimin==2:
            print("Berabere.")
        elif secimin==3:
            print("Kazandınız.")
            p_skor+=1
        elif secimin==1:
            print("Kaybettiniz.")
            ai_skor+=1
        else:
            print("Geçerli bir değer giriniz")

    elif ai_secimi==3: #Bilgisayarın Makas seçtiği koşul
        if secimin==3:
            print("Berabere.")
        elif secimin==1:
            print("Kazandınız.")
            p_skor+=1
        elif secimin==2:
            print("Kaybettiniz.")
            ai_skor+=1
        else:
            print("Geçerli bir değer giriniz")

    if ai_skor >=bitis or p_skor >=bitis:
        break