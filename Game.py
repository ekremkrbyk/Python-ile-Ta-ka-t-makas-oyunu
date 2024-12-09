import Classes as cs

class Game:
    print("Hoşgeldin Kapışmaya Hazırmısın ?")

    isim = input("İsminizi giriniz: ")
    strateji = input("Strateji seçiniz 1/Normal 2/Agresif : ")

    pc = cs.RandomComputerPlayer("PC 1",2)

    human = cs.HumanPlayer(isim,int(strateji))

    print(f"Rakibin: {pc.getIsim()}")

    print("Oyun Başaldı !")
    skor = [0,0]

    print(f"{skor}\n")

    while True:
        if skor [0] >= 3 or skor[1] >= 3:
            result = input("Devam etmek için 4 e basınız: ")
            if result != 4:
                print(f"{pc.getIsim()} {skor[0]} - {human.getIsim()} {skor[0]}")
                break
        secim = input("Seç 1/Taş 2/Kağıt 3/Makas : ")
        humanResult = human.Oyna(int(secim))
        pcResult = pc.Oyna()
        if pcResult != humanResult:
            match pcResult,humanResult:
                case 1,2:
                    print(f"{human.getIsim()} kazandı !")
                    skor[1] += 1
                    print(f"Skor: {skor}")
                case 2,3:
                    print(f"{human.getIsim()} kazandı !")
                    skor[1] += 1
                    print(f"Skor: {skor}")
                case 3,1:
                    print(f"{human.getIsim()} kazandı !")
                    skor[1] += 1
                    print(f"Skor: {skor}")
        else:
            print("Berabere")
    