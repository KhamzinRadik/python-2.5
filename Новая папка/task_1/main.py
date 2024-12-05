namber=int(input("Enter your namber: "))
lst_namber=[]
for i in range(1,namber+1):
    if i%2!=0:
        lst_namber.append(i)
print(lst_namber)
