my_list = ["goa","programing", 3.734, 2.731,422,72,True,False,32.5,62,898,253,12.38[38723, 2.63, 3837],["goa", "best", "academy"]]


reversed_list = my_list[::-1]
print("შებრუნებული სია:")


sliced_list_1 = my_list[2:7] 
sliced_list_2 = my_list[:5]   
sliced_list_3 = my_list[5:10]
sliced_list_4 = my_list[10:]  
sliced_list_5 = my_list[3:12] 
print("slicing ორი ინდექსით:", sliced_list_1, sliced_list_2, sliced_list_3, sliced_list_4, sliced_list_5)


sliced_list_6 = my_list[1:10:2]  
sliced_list_7 = my_list[::3]     
sliced_list_8 = my_list[2:15:4]  
sliced_list_9 = my_list[5:0:-1]  
sliced_list_10 = my_list[-1:-10:-2] 
print("slicing ორი ინდექსით და ნაბიჯით:", sliced_list_6, sliced_list_7, sliced_list_8, sliced_list_9, sliced_list_10)


sliced_list_11 = my_list[5:]  
sliced_list_12 = my_list[:7] 
sliced_list_13 = my_list[3:]  
sliced_list_14 = my_list[:10] 
sliced_list_15 = my_list[8:] 
print("slicing ერთი ინდექსით და ორწერტილით:", sliced_list_11, sliced_list_12, sliced_list_13, sliced_list_14, sliced_list_15)
