
rašyk("tikriname, ar interpretatorius korektiškai atpažįsta lietuviškus žodžius")


tai veikia(kas):
    rašyk('{:.<30}veikia gerai'.format(kas))

tai neveikia(kas):
    rašyk('{:.<30}NESUVEIKĖ'.format(kas))

tai turiveikt(kas, rezultatas):
    jei rezultatas:
        veikia(kas)
    kituatveju:
        neveikia(kas)

jei1 = Melas
jei2 = Melas
jei3 = Melas

jei 1 != 0:
    jei1 = Tiesa
kituatveju:
    jei1 = Melas

jei 1 != 1:
    jei1 = jei2 = Melas
kituatveju:
    jei2 = Tiesa

jei 1!=1:
    jei1 = jei2 = jei3 = Melas
ojei 2!=2:
    jei3 = Melas
kituatveju:
    jei3 = Tiesa

   
turiveikt("jei", jei1)
turiveikt("jei-kituatveju", jei2)
turiveikt("jei-ojei-kituatveju", jei3)


b = Tiesa

jei b == Tiesa:
    veikia("Tiesa")
kituatveju:
    neveikia("Tiesa")

jei b != Melas:
    veikia("Melas")
kituatveju:
    neveikia("Melas")

l1 = Melas
l1 = Melas ir Tiesa

turiveikt("ir", l1 == Melas)

l1 = Melas
l1 = Melas arba Tiesa

turiveikt("arba", l1 == Tiesa)

l1 = Melas
l1 = nėra l1

turiveikt("nėra", l1)

l1 = Tiesa == True
turiveikt("Tiesa == True", l1)

l1 = Melas == False
turiveikt("Melas == False", l1)

tai lyginiaiSk():
    imk sk iš intervalo(100):
        jei sk % 2 == 0:
            duok sk

iteracijųSk = 0

imk sk iš lyginiaiSk():
    iteracijųSk += 1
    nutrauk

jei iteracijųSk > 1:
    neveikia("imk-nutrauk")
kituatveju:
    veikia("imk-nutrauk")

n = 5

jei nėra (n == 4):
    veikia("jei-nėra")
kituatveju:
    neveikia("jei-nėra")

tęskVeikia = Tiesa
nutraukVeikia = Tiesa
kol n>0:
    n = n - 1
    jei n > 3:
        tęsk
        tęskVeikia = Melas
    kituatveju:
        nutrauk
        nutraukVeikia = Melas

turiveikt("tęsk", tęskVeikia)
turiveikt("nutrauk", nutraukVeikia)

bandyk:
    rašyk(sk[-100])
    neveikia("klaidos gaudymas")
pagavęs Exception pavadink e:
    veikia("klaidos pagavimas")
galiausiai:
    veikia("bandyk-galiausiai")


klasė Aš:
    tai metodas(self):
        grąžink 42

aš = Aš()

turiveikt("metodai ir klasės", aš.metodas() == 42)

