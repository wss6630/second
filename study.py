_list=[2,5,4,5,3,3,3,3,3,]
count = len(_list)
t=0
y=0
#for i in range (count):
#    if  _list.count(_list[i]) == 1:
#        t += 1
#        print (_list[i])
#print (t)        
            
    
    

#print (Str_[1:])

#s = '4 4 34 34 434 3242342342'
for i in range (count):
    p = _list.count(_list[i])
    if p > t:
       t=p
       y = _list[i]
       
print (y)

    