def capicua(string):
    flag = True
    for i in range(len(string)//2):
        if string[(len(string)-1)-i]!=string[i]:
            flag=False
            break
    return flag

    
strg=input("Ingreso: ")
if capicua(strg)==True:
    print("Capicua")
else:
    print("No es capicua")