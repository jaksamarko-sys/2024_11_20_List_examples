"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

szamok = [5, 8, 12, 15, 22]
#print(len(szamok))

hossz = 0
for szamok in szamok:
    hossz = hossz + 1
    print(hossz)