"""Olvassunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.  Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?"""
def main():
    print("Adj meg egész számokat (a 0 a bevitel végét jelzi):")

    # Számok bekérése a billentyűzetről
    numbers = []
    while True:
        try:
            num = int(input())
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Érvénytelen szám, próbáld újra!")

    # 1. Feladat: Volt-e -10 és -15 közé eső szám a beírtak között?
    print("1. Volt-e -10 és -15 közé eső szám a beírtak között?")
    found = any(-15 < num < -10 for num in numbers)
    print("Igen" if found else "Nem")

    # 2. Feladat: Az utolsó 2-vel és 5-tel osztható szám indexe
    print("2. Az utolsó 2-vel és 5-tel osztható szám indexe:")
    indices = [i for i, num in enumerate(numbers) if num % 2 == 0 and num % 5 == 0]
    if indices:
        print(indices[-1])
    else:
        print("Nincs ilyen szám.")

    # 3. Feladat: Hány darab 20-nál nagyobb számot írtak be?
    print("3. Hány darab 20-nál nagyobb számot írtak be?")
    count = sum(1 for num in numbers if num > 20)
    print(count)

    # 4. Feladat: Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
    print("4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?")
    positive_numbers = [(i, num) for i, num in enumerate(numbers) if num > 0]
    if positive_numbers:
        min_index, min_value = min(positive_numbers, key=lambda x: x[1])
        print(f"A legkisebb pozitív szám: {min_value}, indexe: {min_index}")
    else:
        print("Nincs pozitív szám a listában.")

    # 5. Feladat: Negatív számok átlaga
    print("5. Mennyi a negatív számok átlaga?")
    negative_numbers = [num for num in numbers if num < 0]
    if negative_numbers:
        average = sum(negative_numbers) / len(negative_numbers)
        print(f"Átlag: {average:.2f}")
    else:
        print("Nincsenek negatív számok a listában.")

if __name__ == "__main__":
    main()

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