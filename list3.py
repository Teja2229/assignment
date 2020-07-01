list3 = [1,12,22,30,29,12,29,30] 
print ("The original list is : " +  str(list3)) 
res = [] 
for i in list3: 
    if i not in res: 
        res.append(i)  
print ("The list after removing duplicates:",str(res))