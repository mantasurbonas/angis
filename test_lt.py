
rašyk("tikriname, ar interpretatorius korektiškai atpažįsta lietuviškus žodžius")


tai veikia(kas):
    rašyk('{:.<30}veikia gerai'.format(kas))

tai neveikia(kas):
    rašyk('{:.<30}NESUVEIKĖ'.format(kas))

jei 1 != 0:
    veikia("jei")

jei 1 != 1:
    tiekto
kituatveju:
    veikia("jei-kituatveju")

b = Tiesa

jei b == Tiesa:
    veikia("Tiesa")
kituatveju:
    neveikia("Tiesa")

jei b != Melas:
    veikia("Melas")
kituatveju:
    neveikia("Melas")


tai lyginiaiSk():
    imk sk iš intervalo(100):
        jei sk % 2 == 0:
            duok sk

iteracijųSk = 0

imk sk iš lyginiaiSk():
    iteracijųSk += 1
    nutrauk

jei iteracijųSk > 1:
    neveikia("nutrauk")
kituatveju:
    veikia("nutrauk")

n = 5

jei nėra (n == 4):
    veikia("nėra")
kituatveju:
    neveikia("nėra")

kol n>0:
    n = n - 1
    jei n > 3:
        tęsk
        neveikia("tęsk")
    kituatveju:
        nutrauk
        neveikia("nutrauk")

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

jei aš.metodas() == 42:
    veikia("metodai ir klasės")
kituatveju:
    neveikia("metodai ir klasės")

