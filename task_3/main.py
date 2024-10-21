l_nv_card=[]
val_card=int(input ('Введите количество видеокарт'))
max_nv_card=0
nw_l_nv_card=[]

for i in range(val_card):
    print(i+1,end=' ')
    d=int(input (' видеокарта'))
    l_nv_card.append(d)
    if max_nv_card<l_nv_card[i]:
        max_nv_card=l_nv_card[i]

for i in range(len(l_nv_card)):
    if l_nv_card[i]!=max_nv_card:
        nw_l_nv_card.append(l_nv_card[i])

print(nw_l_nv_card)