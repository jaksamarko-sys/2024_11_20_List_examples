"""Olvassunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.  Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?"""


thelist = []
szam = input("Írj be egy egész számot: ")
folytat = True

while folytat:
    if szam == 0:
        folytat = False
    thelist.append(szam)
    szam = int(input("Írj be egy egész számot: "))

print(thelist)
    
print("1.feladat") 
number_between = any(-10 <= szam <= -15 for szam in thelist)
print("5. Van-e szám -10 és -15 között: ",number_between)