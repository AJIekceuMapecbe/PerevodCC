#!coding: UTF8
####      by vk.com/val0dko99     ####

#============#
#  A  |  10  #
#  B  |  11  #
#  C  |  12  #
#  D  |  13  #
#  E  |  14  #
#  F  |  15  #
#============#

import sys

#print("**************************")
#print("*********ВНИМАНИЕ*********")
#print("*Просмотр исходного кода**")
#print("*ведет к плачевным психи-*")
#print("*-ческим последствиям    *")
#print("****Будьте осторожны******")
#print("**Берегите своих близких**")
#print("**************************")
print("By val0dko99") 
print("")

vShestnadc = 0
flag = 0

ad = int(input("Введите число входной системы исчисления  "))

#Это говнокод потому что в python нет switch case
if ad==2:
    print("Выбранна двоичная")
else: 
    if ad==3:
        print("Выбрана троичная")
    else:
        if ad==8:
            print("Выбрана восьмиричная")
        else:
            if ad==10:
                print("Выбрана десятичная")
            else:
                if ad==16:
                    print("Выбранна шестнадцетиричная")
                    flag = 1
                    InChis = input("Введите шестнадцетиричное число: ")
                else:
                    print("-_-, сам считай")
                    sys.exit()


if flag == 0:
    InChis = int(input("Введите число "))

asd = int(input("Введите выходную систему счисления(число)  "))

if asd==2:
    print("Выбранна двоичная")
else: 
    if asd==3:
        print("Выбрана троичная")
    else:
        if asd==8:
            print("Выбрана восьмиричная")
        else:
            if asd==10:
                print("Выбрана десятичная")
            else:
                if asd==16:
                    print("Выбранна шестнадцетиричная")
                else:
                    print("-_-, сам считай")
                    sys.exit()

#################################### Это все из десятичной в другие системы
def perevod(chislo, sistema):   #Десятичная в восьмиричн троичн двоич
    dadVosmir = 1               #число которое будем все время делить
    dadOctatokVosm = 1          #остаток от деления
    vVosm = ""                  #результат 
    dadVosmir = chislo
    while True:  
        dadOctatokVosm = int(dadVosmir % int(sistema)) #с остатком
        dadVosmir = int(chislo / int(sistema))   #просто деление
        chislo = dadVosmir
        vVosm = vVosm + str(dadOctatokVosm)
        if dadVosmir == 0:
            return vVosm[::-1]
            break
#####################################
#####################################троичная двоичная восмиричная в десятичн ВРОДЕ ГОТОВО
def vDesyat(InChis, sistema):
    chisIn = InChis
    chisInInt = int(chisIn)
    chisInStr = str(chisInInt)
    inDlina = int(len(chisInStr))
    result = 0

    for ias in range(0,len(chisInStr)):
        inDlina = inDlina - 1
        result = result + (int(chisInStr[ias]) * (sistema ** inDlina))

    return result
#####################################

def shestnVdesya(InChis): #Шестнадцетричная в десятичн
    return(int(InChis, 16))

def vShestnad(chislo):     #десятичную в шестнадцетричную
    return hex(chislo)[2:] # return 2: означает вернуть переменную, но 
                           # возвращать все начиная со второй ячейки,т.е без 0x
                           


#ВОТ АНА РЫБА МЕЧТЫ
#ad -  входная
#asd - выходная
# vDesyat(InChis , n) где InChis входное число, n система которую преобразуем в десятичную
# perevod(chislo, sistema) где chislo это число которое преобразуем, sistema в которую переводим

#проверка введеных чисел на проверку нет ли там чего лишнего, например в двоичной только 1 и 0
daad = str(InChis)
if ad == 2:
    for isa in range(0,len(daad)):
        if daad[isa] != "1":
            if daad[isa] != "0":
                print("В введенной вами строкe присутствуют лишние цифры ")
                sys.exit()

if ad == 3:
    for isa in range(0,len(daad)):
        if daad[isa] != "0":
            if daad[isa] != "1":
                if daad[isa] != "2":
                    print("В введенной вами строкe присутствуют лишние цифры ")
                    sys.exit()

if ad == 8:
    for isa in range(0,len(daad)):
        if daad[isa] != "0":
            if daad[isa] != "1":
                if daad[isa] != "2":
                    if daad[isa] != "3":
                        if daad[isa] != "4":
                            if daad[isa] != "5":
                                if daad[isa] != "6":
                                    if daad[isa] != "7":
                                        if daad[isa] != "9":
                                            print("В введенной вами строкe присутствуют лишние цифры ")
                                            sys.exit()

################################# Конец проверки


if ad == 2:#входная двоичная
    if asd == 2:
        print("Ацаца ")

    if asd == 3:
        print("В троичной", perevod(vDesyat(InChis, 2), 3))
    
    if asd == 8:
        print("В восьмиричной", perevod(vDesyat(InChis, 2), 8))

    if asd == 10:
        print("В десятичной ", vDesyat(InChis, 2))

    if asd == 16:
        print("В шестнадцетиричной", vShestnad(int(vDesyat(InChis, 2))))

if ad == 3:#троичная вход
    if asd == 2:#двоичн выход
        print("В двоичной ", perevod(vDesyat(InChis, 3), 2))

    if asd == 3:
        print("Ацаца")

    if asd == 8:#восьмиринч выход
        print("В восьмиричной", perevod(vDesyat(InChis, 3), 8))

    if asd == 10:#десятичн выход
        print("В десятичной", vDesyat(InChis, 3))
    
    if asd == 16:#шестнадц выход
        print("В шестнадцетричной", vShestnad(int(vDesyat(InChis, 3))))


if ad == 8:#восьмиричн вход
    if asd == 2:#двоичн выход
        print("В двоичной ",perevod(vDesyat(InChis, 8), 2))

    if asd == 3: #
        print("В троичной ",vTroich(vDesyat(InChis, 8), 3))

    if asd == 8:#восьмиринч выход
        print("Ацаца")

    if asd == 10:#десятичн выход
        print("В десятичной ", vDesyat(InChis, 8)) 
    
    if asd == 16:#шестнадц выход
        print("В шестнадцетиричной ",vShestnad(int(vDesyat(InChis, 8)))) #вот так вот)

if ad == 10: #Десятичн в другие
    if asd == 2:
        print("В двоичной ", perevod(InChis, 2))
    
    if asd == 3:
        print("В троичной ", perevod(InChis, 3))
    
    if asd == 8:
        print("В восьмиричной ", perevod(InChis, 8))
    
    if asd == 10:
        print("Ацаца ")

    if asd == 16:
        print("В шестнадцетиричной", vShestnad(InChis))

if ad == 16: #шестнадц в другие
    if asd == 2: #в двоичную
        print("В двоичной", perevod(shestnVdesya(InChis), 2))
    
    if asd == 3:#шестнадц в десятич и в троичн
       print("В троичной ", perevod(shestnVdesya(InChis), 3))

    if asd == 8:
       print("В восьмиричн ", perevod(shestnVdesya(InChis), 8))

    if asd == 10:
       print("В десятичной ", shestnVdesya(InChis))

    if asd == 16:
        print("Ацаца ")   

#  из десятичной в другие
#perevod(InChis, 2) # Из десятичной в двоичную
#perevod(InChis, 3)  # В троичную
#perevod(InChis, 8)    #В восьмиричн
#vShestnad(InChis) #В шестнадцетиричную

# из двоичн троич восьмирич в десятичн
#lib.dvoichVdesyat(InChis)  #Двоичн в десятичн
#lib.troichnVdesyat(InChis) #Троичн в десятичн
#lib.vosmVdesyat(InChis)    #Восьмиричн в дестичн
#lib.shestnVdesya(InChis)   #шестнадцетиричн в десятичн

