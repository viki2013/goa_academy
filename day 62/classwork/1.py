#1
viki =  lambda side1, side2:side1 * side2


print(viki)
print(viki(2, 3))      
print(viki(5, 4))      
print(viki(10, 0))     
print(viki(-3, 7))     
print(viki(1.5, 4))    


#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11 , 12 , 13, 14 , 15]
print(list(filter(lambda x: x % 2 == 0, numbers)))
