list7=[22,11,33,44,55]
print("original list:")
print(list7)
for i in list7: 
	if(i%2 == 0): 	 
		list7.remove(i) 
print("list after removing even numbers:")
print(list7)