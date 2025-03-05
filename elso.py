with open('./proba.txt', 'r', encoding='utf-8') as proba, \
    open('proba_masolat.txt', 'w', encoding='utf-8') as fajl:
    for par in proba:
        print(par.strip(), file=fajl)
