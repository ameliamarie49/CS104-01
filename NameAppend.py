names = ["Dana","Nina","Tatiana","Matt","Sam","Shannon","Dahlia","Jack","Cole","Steve"]
for x in range (0,10): #Accepts first ten names in the keyboard (0-10)
    aname=input("Enter a name:")
    names.append(aname)
    endloop= False
while endloop==False:
    search=input("Enter a search name or End:")
    if search in names:
        print("Name found")
    else:
        print("Not found")
    if search == 'End':
        endloop = True
