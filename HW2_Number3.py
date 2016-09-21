1 # -*- coding: utf-8 -*- 
2 """ 
3 Created on Thu Sep 15 19:08:25 2016 
4  
5 @author: 12072062 
6 """    
7 
 
8 """Homework Problem 3 
9 The purpose of this program is to create Collatz Chain for a given integer N. 
10 We will also find which number (N), under one thousand, produces the longest chain""" 
11 
 
12 #First we ask for the user to input a value for N 
13 
 
14 N=int(input('Guess the longest Collatz Chain by entering a value for N: ')) 
15 
 
16 #Next we define a function called CollatzChain 
17 def CollatzChain(N,count=1):    #We assign the parameter N to the functions 
18     while N!=1: 
19         print(N) 
20         count+=1 
21         if N %2==0: #This means that N is an even number since there is no remainder 
22             N=N//2 
23         else: 
24             N=N*3+1 #This is the formula when N is an odd number 
25     print(N,'\n') 
26      
27     return count-1 
28 
 
29 def ChainLength():     
30     print(CollatzChain(N))     
31     if N==97: 
32         print('This is the longest chain under one thousand!') 
33     else: 
34         print('This is not the longest chain under one thousand. Try again.') 
35 
 
36      
37 print(ChainLength()) 
