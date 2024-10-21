films = ['Крепкий орешек' ,'Назад в будущее',
         'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
val_cinema=int(input ('Сколько фильмов хотите добавить?'))
frend_list=[]

for i in range(val_cinema):
  cinima=(input('Введите название фильма: '))
  count_cinima=0
  for y in range (len(films )):

     if cinima==films[y]:
        count_cinima+=1
  if count_cinima==0:
    print('Ошибка: фильма', cinima, ' у нас нет')
  if count_cinima!=0:
   frend_list.append(cinima)


print('Ваш список любимых фильмов:',frend_list)