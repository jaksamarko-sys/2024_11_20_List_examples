import random
import math

# 50 véletlen szám generálása -60 és 100 között
random_numbers = [random.randint(-60, 100) for _ in range(50)]
print("A random generált számok a következőek:", random_numbers)

# 1. feladat: A számok szorzata
print("1. Mennyi a sorozatban található számok szorzata?")
product = math.prod(random_numbers)
print(product)

# 2. feladat: Az utolsó 5-tel vagy 7-tel osztható szám indexei
print("\n2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!")
for index, number in enumerate(random_numbers):
    if number % 5 == 0 or number % 7 == 0:
        print(f"Index: {index}, Number: {number}")

# 3. feladat: Az első 3-mal és 7-tel osztható szám indexei
print("\n3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!")
count = 0
for index, number in enumerate(random_numbers):
    if number % 3 == 0 and number % 7 == 0:
        print(f"Index: {index}, Number: {number}")
        count += 1
    if count >= 1:
        break

# 4. feladat: Igaz-e, hogy minden szám negatív?
print("\n4. Igaz-e, hogy minden szám negatív?")
all_negative = all(num < 0 for num in random_numbers)
print(all_negative)

# 5. feladat: Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
print("\n5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?")
exists_in_range = any(1 <= num <= 10 for num in random_numbers)
print(exists_in_range)

# 6. feladat: Hány 18-cal osztható szám található a sorozatban?
print("\n6. Hány 18-cal osztható szám található a sorozatban?")
count_divisible_by_18 = sum(1 for num in random_numbers if num % 18 == 0)
print(count_divisible_by_18)

# 7. feladat: Mennyi a sorozatban található egyik legkisebb szám indexe?
print("\n7. Mennyi a sorozatban található egyik legkisebb szám indexe?")
min_value = min(random_numbers)
min_index = random_numbers.index(min_value)
print(f"Legkisebb szám: {min_value}, Index: {min_index}")

# 8. feladat: Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
print("\n8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!")
for number in random_numbers:
    if number % 17 == 0 or number % 18 == 0:
        print(f"Number: {number}, Square: {number ** 2}")

# 9. feladat: Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
print("\n9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?")
has_negative_with_positive_neighbors = False
for i in range(1, len(random_numbers) - 1):
    if random_numbers[i] < 0 and random_numbers[i - 1] > 0 and random_numbers[i + 1] > 0:
        has_negative_with_positive_neighbors = True
        break
print(has_negative_with_positive_neighbors)

# 10. feladat: Igaz-e, hogy a sorozat szigorúan monoton növekvő?
print("\n10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?")
is_strictly_increasing = all(random_numbers[i] < random_numbers[i + 1] for i in range(len(random_numbers) - 1))
print(is_strictly_increasing)

# 11. feladat: Válogassuk ki két listába a páros és a páratlan számokat!
print("\n11. Válogassuk ki két listába a páros és a páratlan számokat!")
even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]
print(f"Páros számok: {even_numbers}")
print(f"Páratlan számok: {odd_numbers}")
