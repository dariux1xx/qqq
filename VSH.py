n = input()
if [1] == 'к' or 'и' or 'л':
    for i in range(0,len(n)-1,2):
        print(n[i])
else:
    for i in range(1,len(n),2):
        print(n[i])
     
