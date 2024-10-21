def shift(lst, position):
    for _ in range(position):
        last = lst.pop()
        lst.insert(0, last)

lst = [1, 2, 3, 4, 5]
position=int(input('здвиг : '))
shift(lst, position)
print(lst)