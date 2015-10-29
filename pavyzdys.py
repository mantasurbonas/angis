reikalinga programa


pieštuk = programa.Pieštukas()

pieštuk.greitis(9)
pieštuk.pirmyn(50)

tai kvadratas(kraštinė):
    imk i iš intervalo(0, 4):
        pieštuk.pirmyn(kraštinė)
        pieštuk.kairėn(90)

tai gėlytė(lapeliųSk):
    posūkis = 360 / lapeliųSk 
    imk i iš intervalo(0, lapeliųSk):
        kvadratas(100)
        pieštuk.kairėn(posūkis)

gėlytė(lapeliųSk = 10)

programa.atia()
