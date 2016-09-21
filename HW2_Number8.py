""" 
3 Spyder Editor 
4  
5 This is a temporary script file. 
6 """ 
 
 
def calculation(x,n): 
    e1 = x 
    e2 = x 
    e3 = x 
    i  = 0 
    while i < n: 
        e1 = 3.95*e1*(1-e1) 
        e2 = 3.95*e2-3.95*e2**2 
        e3 = 3.95*(e3-e3**2) 
        print(e1,e2,e3) 
        i += 1 
          
calculation(.9,100) 
