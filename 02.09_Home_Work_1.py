'''1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.'''

# duration = int(input('Type the duration: '))
# day = 86400
# hour = 3600
# minute = 60
# second = 1
#
# if duration >= day:
#     a = duration // day
#     b = (duration - (a * day)) // hour
#     c = ((duration - (a * day)) - (b * hour)) // minute
#     d = ((duration - (a * day)) - (b * hour)) - (c * minute)
#     print(f'{a}<d>, {b}<h>:{c}<m>:{d}<s>')
# elif hour <= duration < day:
#     a = duration // hour
#     b = (duration - (a * hour)) // minute
#     c = ((duration - (a * hour)) - (b * minute)) // second
#     print(f'{a}<h>:{b}<m>:{c}<s>')
# elif minute <= duration <= hour:
#     a = duration // minute
#     b = (duration - (a * minute)) // second
#     print(f'{a}<m>:{b}<s>')
# else:
#     print(f'{duration}<s>')

'''2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. * Решить задачу под пунктом b, не создавая новый список.'''

'''Part 1 (список нечетных чисел в кубе)'''
# degree_list = [i ** 3 for i in range(1, 1000, 2)]
# print(degree_list)
'''Part a (сумма чисел из списка degree_list, сумма цифр которых делится нацело на 7)'''
# sum_numbers = 0
# for el in degree_list:
#     el = str(el)
#     number = 0
#     for digit in el:
#         number += int(digit)
#     if number % 7 == 0:
#         sum_numbers += int(el)
# print(sum_numbers)
'''Part b (к каждому элементу списка добавить 17)'''
# degree_list[:] = [i + 17 for i in degree_list]
# print(degree_list)
'''(заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.)'''
# sum_numbers = 0
# for el in degree_list:
#     el = str(el)
#     number = 0
#     for digit in el:
#         number += int(digit)
#     if number % 7 == 0:
#         sum_numbers += int(el)
# print(sum_numbers)
'''Пример расчет суммы цифр числа без приведения к строке:'''
# a = 755415
# number_sum = 0
# while a != 0:
#     number_sum += a % 10
#     a = (a - (a % 10)) // 10
# print(number_sum)


'''3. Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100.'''
# basic_word = 'процент'
# exception_list = [*range(11, 15)]
# for percent in range(1, 101):
#     percent = str(percent)
#     if percent[-1] == '1' and int(percent) not in exception_list:
#         print(f'{percent} {basic_word}')
#     elif (percent[-1] == '2' or percent[-1] == '3' or percent[-1] == '4') and int(percent) not in exception_list:
#         print(f'{percent} {basic_word}a')
#     else:
#         print(f'{percent} {basic_word}ов')
