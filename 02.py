# 02
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("------------------------------------------------------------------------")
print("  X\t\t  Y\t\t  Z\t|   ¬(X ⋁ Y ⋁ Z)     ¬X ⋀ ¬Y ⋀ ¬Z")
print("------------------------------------------------------------------------")
result = True
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            a = not (x or y or z)
            b = not (x) and not(y) and not(z)
            if a != b:
                result = False
            print(f"{x}\t\t{y}\t\t{z}\t|\t{a}\t\t{b}")
            
print("Результат сравнения двух выражений = ", result)
