"""We, as a group, divided the problems up amongst ourselves. We collaborated
on a couple problems with members of group B as well for their insight
I'm still working on this..."""


"""Homework Problem number 1

The purpose of this program is calculate the nth term of the
Fibonacci sequence. What is the index of the first term in
the Fibonacci sequence to contain 100 digits?"""


def Fibonacci_sequence(digit_length): #Here we difine the function Fibonacci_sequence and give it the parameter digit_length
    x = {}  #Here we define x to be an empty set
    x[0] = 1    #Here we define the index of 0 to be 1 in the list x
    x[1] = 1    #Here we define the index of 1 to be 1 in the list x
    for i in range(0,10 ** 100): 
        x[i + 2] = x[i + 1] + x[i] 
        if len(str(x[i + 2])) >= digit_length : 
            break 
# The actual subscript should be the index plus one, i.e., (i+2)+1. 
    return i + 3 
    
print('The {}th Fibonacci number is the first term in the sequence to contain {} digits.'\
.format(Fibonacci_sequence(100), 100))


"""Homework Problem 2
The purpose of this program is to find the maximum total
from top to bottom of a trianglar pyramid of numbers."""

def max_sum(pyramid):     #Here we define the function max_sum and assign it the parameter pyramid
    for i in range(1,len(pyramid)): #We create a loop to and try to find the length of the list of numbers in each line
    # Add the right-most numbers from top to bottom. 
        pyramid[i][i] += pyramid[i - 1][i - 1]  
    # Add the left-most from top to bottom. 
        pyramid[i][0] += pyramid[i - 1][0] 
    
    # Add the numbers in the middle of the pyramid. 
    for a in range(1,len(pyramid)): 
        for b in range(1, a):  
            pyramid[a][b] += max(pyramid[a - 1][b - 1], pyramid[a - 1][b]) 
    # Return a maxium value of the last line 
        return max(pyramid[len(pyramid) - 1]) 

#Here we create both pyramids:     
pyramid1 =  [[3], 
            [7, 4], 
            [2, 4, 6], 
            [8, 5, 9, 3]] 
 
 
pyramid2 =  [[75], 
            [95, 64], 
            [17, 47, 82], 
            [18, 35, 87, 10], 
            [20,  4, 82, 47, 65], 
            [19,  1, 23, 75,  3, 34], 
            [88,  2, 77, 73,  7, 63, 67], 
            [99, 65,  4, 28,  6, 16, 70, 92], 
            [41, 41, 26, 56, 83, 40, 80, 70, 33], 
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], 
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]    
              
print(max_sum(pyramid1)) 
print(max_sum(pyramid2)) 


"""Problem 3 
The purpose of this program is to create Collatz Chain for a given integer. 
We will also find which number, under an upper bound, produces the longest chain 
"""

def max_chain_length(upper_bound):  #Here we define the fuction max_chain_length and assign it the parameter upper_bound
    max_length = 1 
    max_num = 0 
    for num in range(2, upper_bound + 1): 
        length = chain_length(num) 
        if length > max_length: 
            max_length = length 
            max_num = num 
# Return the number that has the maximun length, and the corresponding length. 
    return max_num, max_length 
 
 
def chain_length(num): 
    count = 0     
    while num != 1: 
        count += 1 
        if num % 2 == 0: #This is using the % to see if the remainder is zero, then the number is even  
            num /= 2 
        else: #If there is a remainder, then the number is odd and we perform the following calculation:
            num = num * 3 + 1    
        return count + 1 

 
print(chain_length(50)) #Here is an example to test the program
print(max_chain_length(1000)) 

"""Homework Problem 4"""

from decimal import * 
167 getcontext().prec = 2000 #set longer decimal place for calculation 
168 def recur_cycle(value): 
169     """ 
170     the function calculates the length of the recurring cycle for the reciporal of  
171     an integer in the decimal representation. Then it finds the number that produces the  
172     longest length 
173      
174     parameters: 
175     value: is a arbitary number 
176      
177     return :the length of recurring cycle 
178     """ 
179     tem = Decimal(1)/Decimal(value) #get the decimal numbers 
180     deci=list(str(tem)) #trasfer the decimal to a list for convenient of later comparison 
181     if len(deci)<999: 
182         return 0 # check to see if the decimal places is finite, if so the length of recursion cycle is 0 
183     else: 
184         n=1 #counter of the length 
185         while True:     
186             if deci[10]==deci[10+n]: #compare value from 10th term because some cycles are not start from beginning, so we define the start from 10th value, if some value is same as the start, turn into next comparison  
187                 z=1 # z is a stop indicator, if n is cycle length, then z=1, otherwise z=0 
188                 for i in range(0,n):    #checks the value from the previous digits to see if they cycles 
189                     if deci[10+i]==deci[10+n+i]:# if one value is the same at the beginning, then compare the every values after that position 
190                         continue 
191                     else: 
192                         z=0 # if z =0, n is not cycle length 
193                         break 
194                 if z==1: 
195                     return n  #if z =1, the range up to n is a cycle, the return the cycle length n 
196                 else: 
197                     n=n+1 # if n is not cycle length, increment n to check for recurring cycle  
198                     continue 
199             else:    
200                 n=n+1 
201                 continue 
202              
203 def main(): 
204     ''' 
205     Use the function, recur_cycle(), to find the value of d < 500 for which 1/d  
206     contains the longest recurring cycle in its decimal fraction part 
207     ''' 
208     value=2 
209     max=recur_cycle(1)   #initialize the max length 1 
210     for i in range(2,500): #checks the number from 2 to 500 
211         if recur_cycle(i)>max:  # if current length of the cycle is longer than max, update it as max 
212             max=recur_cycle(i)  
213             value=i         #store the length in the variable value 
214         else: 
215             continue             
216     print('the number', value, 'have the longest recurring cycle with cycle length: ',max) #max is the maximum length of recursion cycle and 'value' is its corresponding value 
217 main() 


"""Problem 5
The purpose of this function is to how many different ways £2 can be made using any number of coins
"""

 
def ways(sum): #First we define the function ways and assign it the parameter sum
# Here we want to set all the elemnts in the string to zero and then multiply it by the sum +1
    ways = [0] * (sum + 1) 
    ways[0] = 1 #Here we assign the index of the zero position to equal 1
# In each of the outter loop, take one additional type of coin t.   
# And for each sum number, now it can also be constructed by (sum-t) plus t, 
# so now we have ways[sum-x] additional ways to construct sum. 
    for t in [1,2,5,10,20,50,100,200]:   
    # For each sum, we want to update the number of ways 
        for i in range(t, sum + 1):   
            ways[i] += ways[i - t]  
        return ways[sum] 
     
print(ways(6)) #Here is an example      
print(ways(8)) #Here is another example
print(ways(150)) 


"""Problem 6
The purpose of this function is to take a positive integer and checks if it is prime
"""
#The following function does not use recursion:
import math  #We want to import the module math to be able to call math functions

def is_prime(num): #Here we define a function is_prime and assign it the parameter num
    if num == 1: #If the number equals 1...
        return False #...then we return a false since one is not considered a prime number
    if num == 2: #If the number equals 2...
        return True #...then we return a true since two is the first prime number

# 
# Take the square root of num to reduce iteration times. 
    for i in range(2, int(math.sqrt(num)) + 1): 
        if (num % i) == 0: 
            return False 
        return True 

#Here we print some examples 
print(is_prime(1)) 
print(is_prime(2))   
print(is_prime(9)) 
print(is_prime(15)) 
print(is_prime(37)) 

"""This part of the problem utilizes recursion"""

import math #We want to import the module math to be able to call math functions

def is_prime(num): #Here we define a function is_prime and assign it the parameter num
    return is_prime_recur(2, num) 
 
 
def is_prime_recur(divisor, num): #Here we define a function is_prime_recur and assign it the parameters divisor and num
    if num == 1: #If the number equals 1...
        return False #...then we return a false since one is not considered a prime number
    if num == 2: #If the number equals 2...
        return True #...then we return a true since two is the first prime number
         
# Now we want to check all the numbers greater than two:
# Take the square root of num to reduce iteration times. 
    if divisor > int(math.sqrt(num)): 
        return True  
         
    if num % divisor == 0: 
        return False 
    else: 
        return is_prime_recur(divisor + 1, num) 
#Here we print some examples      
print(is_prime(1)) 
print(is_prime(2))   
print(is_prime(9)) 
print(is_prime(15)) 
print(is_prime(37)) 


"""Problem 7
The purpose of this function is to accept a list of strings and uses recursion to return a sorted list.
Each step only modifies two elements of the list.
"""

 
def recur_sort(str_list): #Here we define a function recur_sort and assign it the parameter str_list
    swapped = False 
    for idx1 in range(len(str_list)): #We are creating a for loop to look for the index length of the variable str_list in a range...
        for idx2 in range(idx1): 
            if str_list[idx2] > str_list[idx2 + 1]: 
                temp = str_list[idx2] 
                str_list[idx2] = str_list[idx2 + 1] 
                str_list[idx2 + 1] = temp 
                swapped = True 
                    break # Exit inner loop after a swap. 
            if swapped: 
                break # Exit outter loop as well so that we swap only once in each recursion. 
        if swapped: # Recursively call function until no more elements are swapped. 
            recur_sort(str_list) 

 
str_list = ['Kristen','loves','her','Dog','Max'] #Here is an example
recur_sort(str_list) 
print(str_list) 


# hw2 problem 8 

def calculation(x, n): 
    e1 = x 
    e2 = x 
    e3 = x 
    i  = 0 
    while i < n: 
        e1 = 3.95 * e1 * (1 - e1) 
        e2 = 3.95 * e2 - 3.95 * e2 ** 2 
        e3 = 3.95 * (e3 - e3 ** 2) 
        print(e1, e2, e3) 
        i += 1

calculation(.9, 100) 

 
""" 
0.3554999999999999 0.3554999999999997 0.35549999999999987 
0.9050230125 0.9050230124999998 0.9050230124999998 
0.3395276194144283 0.33952761941442855 0.33952761941442877 
... 
0.8017824376001337 0.6298783813120168 0.6356515857217065 
0.6277630734066796 0.920869843967693 0.9148146568001868 
0.9230225584410336 0.28783086903250865 0.3078187619897856 
 
Top three lines are the results for n = 1,2,3 
Bottom three lines are the results for n = 98,99,100 
We can see that the difference are getting greater as n increases.  
The reason for this phonemena is that computers use only a limitted
(e.g., 32 or 64) bits of 1's or 0's to store numbers.  
Thus it cannot precisely represent decimals. 
""" 
