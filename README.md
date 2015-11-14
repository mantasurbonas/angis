# angis
Bandymas pridėti lietuvybes pitonui, pirmas dublis

## Pavyzdys
``` 
reikalinga programa # import programa

pieštuk = programa.Pieštukas()

tai kvadratas(ilgis):
    kartok 4:
        pieštuk.pirmyn(ilgis)
        pieštuk.kairėn(90)

tai gėlytė(lapeliųSk):
   kampas = 360 / lapeliųSk
   kartok lapeliųSk:
        kvadratas(100)
        pieštuk.kairėn(kampas)

gėlytė(10)
```

## Kam to reikia?

Nes Komenskio Logo lietuviškas vertimas padėjo daugybei vaikų susidomėti programavimu. Lietuviška Pitono versija - tikiuosi - būtų net lengvesnė mokymo priemonė:
* tradicinė programavimo sintaksė. Tarkim, a = b + c arba tekstas = "koks nors tekstas" yra daug suprantamiau nei tai, ką bando naudoti Logo.
* sakiniai rašomi iš naujos eilutės, sakinių blokai grupuojami pagal tai, kiek jie atitraukti nuo krašto - sukurtą programą įmanoma perskaityti net ir po savaitės nuo užrašymo!
* visiškai suderinama su Pitonu. Tai yra, 
  * galima importuoti angliško Pitono .py failus, 
  * galima tiesiog įterpti angliško Pitono kodą (tarkim, internete rastą algoritmą), 
  * ir netgi standartinio Pitono interpretatorius nesiskųsdamas teisingai vykdys lietuviško Pitono/Angies .pyc failus. Pavyzdžiui, jeigu robotą galima programuoti anglišku Pitonu, tai galima ir lietuvišku Angimi.
* jokių kliūčių mokytis objektinio programavimo. 
* visas kodas yra atviras. Norint galima modifikuoti sintaksę, pridėti savo žodžių, konstrukcijų ir t.t.


## Daugiau informacijos

Tai ne programavimo kalba, tai tik Python kalbos dialektas (viršaibė) - standartinio 3.5.0 Pitono sintaksė praturtinta papildomais lietuviškais sinonimais. Taigi, viename faile galima kaip tik nori maišyti if ... ir jeigu ... , taip pat importuoti .py modulius ir t.t.

Štai kai kurie iš sinonimų (pilną sintaksę žr žemiau):

``` 
jei / jeigu  - sinonimas if
tai - sinonimas def
rašyk - sinonimas print
paklausk - sinonimas input
grąžink / grįžk - sinonimas return
klasė - sinonimas class
reikalingas / reikalinga - sinonimas import
``` 

Be sinonimų, kompiliatoriui taip pat pridėta ir viena nauja, Python'e nesanti kalbos konstrukcija - 'kartok N:'

``` 
kartok 10:
    rašyk("pirk dramblį")
``` 

Ši konstrukcija pridėta tam, kad vaikams lengviau būtų mokytis ciklo sąvokos. Tai - vienintelis sintaktinis skirtumas nuo standartinio Python 3.5.0, tačiau Angies sugeneruotas baitkodas visiškai suderinamas su standartiniu pitonu (t.y., pakeitimas vien tik kompiliatoriuje, ne virtualioje mašinoje).

### Pilna sintaksė

TBD
