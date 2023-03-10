# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2 S = x + y / P = x * y
# 5 6 -> 2 3 S = x + y / P = x * y

import math
S = int(input("Введите сумму чисел : "))
P = int(input("Введите произведение чисел : ")) 
# для вычисления данной задачи воспользуемся сделющими знаниями
# составим систему уравнений в виде : x + y = S и x * y = P
# далее выражаем x через y или наоборот и получаем квадратное уравнение вида:
# x**2 - S * x + P = 0 и y**2 - S * y + P = 0
# берем любое из них, вычисляем дискриминант квадратного уравнения
# и далее следую условиям решаем его с помощью программы =)
Discriminant = S ** 2 - 4 * P
if Discriminant < 0:
    print("нет решения для данных чисел")
elif Discriminant == 0:
    x = S / 2
    print(f"для данного условия есть только один корень = {int(x)}")
elif Discriminant > 0: 
    # так как здесь по формуле считается x1 и x2, и далее находим по формуле y = S - x
    # так как оба решения будут зеркальными,опускаем этот момент и заменяем сразу x2 на y
    x = (S + math.sqrt(Discriminant)) / 2 # x1 = x
    y = (S - math.sqrt(Discriminant)) / 2 # x2 = y
    print(f"решение найдено и оно равно числам : {int(x)} и {int(y)}")