def ves(x):
    if x < 1 or x > 200:
        print('Вес > 200')
        return False
    else:
        return True

conteyner = int(input('Количество контейнеров: '))
a, i =[],0
while i < conteyner:
    ves = int(input('Введите вес контейнера: '))
    if ves(ves):
        a.append(ves)
        i += 1

while True:
    new_conteyner = int(input('Введите вес нового контейнера: '))

    for i in range(conteyner):
        if new_conteyner >= a[i]:
            print(i+1)
            break
