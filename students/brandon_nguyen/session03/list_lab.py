#!/usr/bin/env python3
#Week3 Excercise #2 list_lab
#Student: Brandon Nguyen - Au2018
 
"""
"""
def list_lab():
    Series1_lst=["Apples","Pears","Oranges","Peaches"]
 
    print(Series1_lst)
    print()
 
    fruitInput = input("Please enter another fruit and press enter >: ")
    print()
    Series1_lst.append(fruitInput)
    print(Series1_lst)
    print()
    #format on remving quote
    #print ('[%s]' % ', '.join(map(str,Series1_lst)))
 
    indexInput=input("Please enter the number that represents the fruit >: ")
 
    print("\nHere is your Number: \"{}\", and your fruit is: \"{}\"".format(indexInput,Series1_lst[int(indexInput)-1]))
    print()
 
    #add to list using +
    Series1_lst=['Grapes'] + Series1_lst
    print(Series1_lst)
    print()
 
    Series1_lst.insert(0,"Papaya")
    print(Series1_lst)
    print()
    
    #print list with p.
    newList=[]
    for item in Series1_lst:
        if item[0]=='P':
            newList.append(item)
    print(newList)
    print()
#SERIES 2 part
    Series2_lst=Series1_lst[:]
    print(Series2_lst)
    Series2_lst.pop()
    print(Series2_lst)
    fruitInputDel = input("Please enter another fruit to delete and press enter >: ")
  
    for name in Series2_lst:
        if name == fruitInputDel:
            Series2_lst.remove(fruitInputDel)
    print(Series2_lst)
    #TODO bonus when time permit
    print()
    Series3_lst=Series1_lst[:]
    for name in Series1_lst:
        while True:
            fruitInputSel= input("Do you like " + name + " yes/no?: ")
            if fruitInputSel.strip() =="yes" or fruitInputSel.strip()=="no":
                break
        if fruitInputSel.strip() == 'no':
            Series3_lst.remove(name)  
    print(Series3_lst)

    #Series 4 excersise
    Series4_lst=Series1_lst[:]
    
    listReverse = []
    for name in Series4_lst:
        listReverse.append(name[::-1])
    Series1_lst.pop()
    
    print()
    print(Series1_lst)
    print(listReverse)
         

