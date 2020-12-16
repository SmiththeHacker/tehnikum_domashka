
print('Здравствуйте, я программа, которая умеет считать сумму списка')
print()
print('Давайте для начала добавим данные в список. Введите "0", когда решите остановиться')
base = []
while True:
    x = int(input())
    base.append(x)
    print(base)
    print('Добавим что-то еще?')
    if x == 0:
        break
print()
print('Это ваша база')
print(base)
print('А это её сумма')
print(sum(base))
