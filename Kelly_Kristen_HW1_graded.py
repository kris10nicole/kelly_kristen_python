#Stuart- Excellent documentation in general, but as part of your documentation you should include the purpose (in the help format) and inputs to
#each of the major functions that you write (~one per problem) you include the information, just not inside your functions
#Stuart- Any points lost due to lack of documentation or using script instead of functions
# can be regained if the issues are corrected. Please email me once you have corrected the issue
# and I will check your code.
"""
Created on Wed Sep 14 23:38:54 2016

@author: Kristen N. Kelly, Group A
We collaborate with a group and also sought outside tutors who are more familiar with the subject matter of Python
"""
"""We divided the problems up in the group. Each team memeber was responsible for three problems"""


"""Number 1
The purpose of this program is to have the user input a text file, read the file, and output any palindromes within the file"""

#Stuart- The problem asks for a function that takes a file name. So the entire
#last step should be wrapped by a function definition.

#Below, I defined the function reverse, which will reverse the line
def revers(line):
   return line[::-1] #This reverses the letters in the line and returns it

#Below, I defined the function is_palindrome, which will produce 'True' if the line is a palindrome and 'False' if it is not
def is_palindrome(line):   #Here I define the function with the parameter line
   return line==reverse(line) #Here we check to see if the reverse of the line is equal to the line (aka if it is a palindrome)

f=open(input('Enter a file name: '),'r')  #Here I am prompting the user's input of the name of a txt file.
for line in f:
   line=line[0:-1]   #Here is the line is the same as the line in reverse order...
   if is_palindrome(line): #...we run the is_palindrome function
      print (line)   #...and we return the line
   else: #If it is not a palindrome...
      print('')   #...it will print a blank space


"""Number 2
A semordnilap is a word or phrase that spells a different word or phrase backwards.
The purpose of this program is to read a text file and ouput any pairs of words that produce semordnilaps"""

#Stuart- You've hard coded 'untitled1.txt' into your function. Whatever file you pass
#to the function is overwritten by the file=..., and if you do not a have 'untitled1.txt' it will
#give you an error.

def semordnilap(file):                       #Here we define the function semordinlap with the parameter file, since we want to look for semordinlaps in a text file
    file = open ('untitled1.txt').read()     #This line opens the file and tells Python to read it 
    words = file.split()                     #This line creates the variable word and formats it by removing this last '\n' character from each line
    results = []                             #This line tells python that the result from the split should be no space at the end of each line
    for word_1 in words:                     #This is a for loop, which will look at the first word in the line
        for word_2 in words:                 #This is a second for loop; we previously told python to look at the first word in the line, and now we are telling it to look at the second word in the line
            if word_1 == word_2[::-1]:       #This is an if statement stating that if the first word is the the reverse spelling of the second word...
                results.append(word_1)       #...then the result will be the second word and we call the append function to place the first word after the second word
    return results
if semordnilap('untitled1.txt'):             #This line is stating that if there is a semordnilap in the text file...
    print("Yes, it is a semordnilap")        #...then we print 'Yes, it is a semordinlap'
    print(semordnilap('untitled1.txt'))      #and we print the words by calling the semordnilap function
else:
    print("No, it is not a semordnilap ")    #If it is not a semornilap, then we print 'No, it is not a semornilap' and we stop

    
    
"""Number 3
The purpose of this program is to accept a file named 'untitled.txt' from the user, build a frequency table of the character used in the file, and sort the table nicely
"""
#Stuart- You've hard coded 'untitled1.txt' into your function. Whatever file you pass
#to the function is overwritten by the file=..., and if you do not a have 'untitled1.txt' it will
#give you an error.

def displaycft(cft):                         #Here we create the function displaycft with the paramter named cft (or character frequency table)
    for a, b in sorted(cft.items()):         #This line creates a for loop looking for letters a and b within the character frequency table. We use the function sorted to tell Python to sort the cft. Items lets us know what in the cft
        print(a, b)                          #Now we print a and b 
        
def char_freq_table(file):                   #Here we create the function char_freq_table with the parameter file so Python knows we are looking for a file in this function
    file = open('untitled1.txt').read()      #this line tells Python to open and read the file named 'untitled.txt'
    return displaycft({letter:file.count(letter) for letter in file})   #This line tells Python to use the displaycft function to count the frequency of each letter in the file return it to the screen and exit the function

print(char_freq_table('untitled1.txt'))      #This line prints the frequecny table to the screen so you can see the results



"""Number 4
The purpose of this function is to translate any text (i.e. any string) into spoken ICAO words using the ICAO dictionary
"""
#In the line below, we import the os and time libraries
import os, time
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''   #This line defines a string of punctuations that Python will need to recognize

#Below we define the ICAO dictionary in a list and assign it to the variable d
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
	 'z':'zulu'} 

def speak_icao(str):          #Here we define a function speak_icao and give it the parameter str so Python knows to expect a string
    words = str.split()       #Here we assign the word to a string and remove ending spaces by using the split function
    for word in words:        #We are creating a for loop to look for words
        for char in word:     #We are creating another for loop to look for characters in a word
            if char not in punctuations:  #If the character doesnt have punctiation
               os.system('say ' + d[char.lower()]) #Here we use the os library to produce the text say and use the defined list of words in d. We use the char.low() function so Python knows these are all lowercase
               time.sleep(0.1)   #We use the time library and the sleep function to define the 0.1 second pause between letters
               time.sleep(1)     #We use the time library and the sleep function to define the 1.0 second pause between words

speak_icao("Hi,I am a student")  #Here is a an example to test the program


"""Number 5
The purpose of this function to return all its hapaxes in a given file
"""
#Stuart- Nice use of a dictionary. When reading a file with multiple lines (made by pressing ENTER)
# extra characters '\n' are added where the line break occurs. if you do text.split() this will remove those as well as ' '.
#Try it with your code and see how it works. 

def hapax(file_name):
    """
    Here we want to construct a dictionary that saves each word of text as its keys and the counts of the words as its values.
    We want to construct a list that returns a word which occurs only once, named hapax list.
    """
    count_dict = {}  #We define the variable count_dict
    hapax_list = []  #We define the variable hapax_list
    
    f = open(file_name,'r')   #Here we use the open function to open a file name 
    text = f.read()           #Here we read the contents of the file
    
    # Here we remove the blank spaces between each word
    for word in text.split(' '):
        # The function below tells Python to recognize the text as lowercase letters
        word = word.lower()
        # The function below checks the occurence of each word in the file
        if word in count_dict:      
           count_dict[word] = count_dict[word] + 1       #If the word appears more than once, add one to the number of times it occurs
        else:
            count_dict[word] = 1 #If the word appears once, assign it the value of 1
     
    # Here we tell Python to definge 'word' as dictionary keys and 'count' as dictionary values
    for word,count in count_dict.items():
        if count == 1:     #Here is the count is only once then...
            hapax_list.append(word)    #...we want to create a put the word within the hapax_list
    
    return hapax_list      #This returns the results of the function
        
print(hapax('sample_input.txt')) #Here we use the file named sample_input.txt to test the program and print the results


"""Number 6
The purpose of this program is: given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n 
"""
def text_lines(in_file_name, out_file_name): #Here we define the function text_lines with the parameters in_file_name and out_file_name
    in_file = open(in_file_name,'r')      #We tell Python to open the file and read it
    out_file = open(out_file_name,'w')    #We tell Python to open a new file and write to it
    line_number = 1                       #We define the variable line_number and assign it a beginning value of 1
    for line in in_file:                  #For every line in the file...
        out_file.write('{}: {}'.format(line_number, line))  #We output the same line in a new file and add a line_number at the beginning
        line_number = line_number + 1     #We start with 1 and add one for each consecutive line

text_lines('sample_input.txt','sample_output.txt') #Here we use the files named 'sample_input.txt' and 'sample_output.txt' to test the program


"""Number 7
The purpose of this program is to calculate the average word length of a text stored in a file. 
"""
#Below we call the regular expression library
import re


def avg_word_length(filepath):      #Here we define the function names avg_word_length with the parameter filepath
    file = open(filepath)           #Here we open the parameter filepath and assign it to the variable file
    words = re.findall('\w+', file.read())   #Here we want to find all words in the file...the '\w' will recognize all characters
    return sum([len(word) for word in words]) / len(words) #Here we want to return the sum of the length of the words divided by the length of the word to find the average


if __name__ == "__main__":    #This sets the special _name_ variable to have a value of "_main_" and will execute the block of code above
    avg_word_length("stored_file.txt") #Here we reach from the sample text file named 'stored_file.txt'
    

"""Number 8
This is a guess the number game.
"""
#Below we want to import the modules random and randrange
from random import randrange

#Below we define the function gtn
def gtn():
	print("Hello! What is your name?")   #This is the initial prompt we print
	gamer_name = input()     #Here we define the variable gamer_name as an input from the user

	print('Well, %s, I am thinking of a number between 1 and 20.' % gamer_name) #Here we tellt the user that Python is thinking of a number between 1 and 20 by calling the user by name
	
	my_number = randrange(1,21) #We assign the variable my_number to a range of 1 and 21 so that 20 will be included
	tries = 0 #We assign the variable tries to zero as the initial time the user guesses

	while True:  #Here we create a while loop for the game
		print('Take a guess.') #we prompt an ititial guess from the user

		gamer_guess = int(input()) #Here we convert the user's input into an integer and assign it to the variable gamer_guess
		tries += 1           #Now we assign the variables tries to a postive one as this is the first try

		if gamer_guess == my_number: #If the gamer guesses the correct number...
			print('Good job, %s! You guessed my number in %d guesses!' % (gamer_name, tries))   #...print the text string listed
			break    #End the program since the user guessed the number correctly
		elif gamer_guess < my_number:   #Else if the guess is less than the true number...
			print('Your guess is too low.')  #...then print the text listed
		else:                           #Else if the the guess is too high...
			print('Your guess is too high.')    #...Print the text listed. This loop will continue until the user guesses the correct number since the field of choices will be narrowed down 

gtn() #Here is a test of the program



"""Number 9
The purpose of this program is too 1) randomly pick a word from given list of words, 2) randomly permutes the word (thus creating an anagram of the word), 3) presents the anagram to the user,
and 4) create n interactive loop in which the user is invited to guess the original word. 
"""
#Below we import the modules random and itertools (which is used for permutations)
import random
import itertools

#Here we use colors as the list of words and assign it to the variable words
words ={"red","orange","yellow","green","blue","purple","black"}
word=random.sample(words,1)[0]   #Here we use the random sample function to take a random sample from the list of words and index it into the first spot

x=list(itertools.permutations(word))   #Here we use the permutation function to permute the word and assign it to the variable x
str1=''.join(x[1])   #Here we joing the string with the index of the permutation of x and assign it to the variable str1 
print(str1)    #We print string one

print("Color word anagram:  ")   #Here we print the prompt for the anagram of the color
wordinput=input("Enter a color as a guess: ")  #Here we ask for a user import to guess the color
while wordinput!=word:  #For every instance the user's input color does not equal the correct color that was randomly selected, print the text shown below
    print("your guess is incorrect")
    wordinput=input("Enter a color as a guess: ")  #If the user's input color equals, the correct color selected print the text below
print("your guess is correct")


"""Number 10
The purpose of this program is to play the game of lingo. The program will take an input from the user and use parantheses to indicate a letter is correct
but in the wrong place, while square brackets indicate both a correct letter and correct placement.
The program will continue until the user guesses the correct word, which in this example will be the word tiger
"""

#Here we define the variable word to consist of the list of letters in the word tiger
word = list("tiger")
print("import lingo") #Here we print the text to indicate to the user that we are playing a the lingo game
guess = [] #This creates the variable guess
while True:
    guess = list(input("Please enter your guess: "))  #This prompts the user to enter a guess
    if guess == word:   #If the user's guess is the chose word (in this case tiger), then we print the text below
        print("You guessed the right word!")
        break  #Here we break the loop when the correct word is entered
    else:   #For every instance the word entered is incorrect...
        firstclue = guess #We assign the variable firstclue to a guess
        for i in range(0, len(word)):  
            if guess[i] == word[i]: #if a particular letter in the guess is equal to one of the letters in the chosen word and is in the correct position...   
                firstclue[i] = "[" + guess[i] + "]"  #...then print that letter with square brackets around it within the same place of the guessed word
        for i in range(0, len(word)):  #...  
            for j in range(0, len(word)): #Here is a for loop to look at the letters in the word from range zero to the length of the word
                if guess[i] == word[j]:   #if the particular letter in the guess is equal to one of the letters in the chosen word and is NOT in the correct position
                    firstclue[i] = "(" + guess[i] + ")"  #...then print that letter with paranthese around it within the same place of the guessed word
        clue = "".join(firstclue) #Here we create the variable clue which joins the letters of the first clue with appropriate brackets and parantheses (if applicable)
        print("Clue: " + clue) #Here we print the word text clue followed by the clue with appropriate brackets and parantheses (if applicable). This will continue until the user guesses the correct word, which in this case is tiger



"""Number 11
The purpose of this program is to split combined lines of sentences into separate lines.
"""
#Stuart- Does this run for you or is there a typo in one of your line(s)? 

#Here we want to import the regular expression module
import re

def sentence_splitter(file_name):   #Here we define the function sentence_splitter with the variable file_name
    with open(file_name, 'r') as f: #Here we open the file, read it...
        file_contents = f.read()  #Here we assign the variable file_contents as what what was just read within the file

#Below, we want to remove all instances of spaces and new lines within the current file.
    sentence = re.sub(r'\n', '', file_content) #Stuart- You dropped an s here so this should have failed when you tested it. Be careful.

#Below we add a new line after each period only if that period is not preceded by a Salutation and is followed by an uppercase letter (rules of english)
    sentence = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentence)

#We also want to add a new line after punctuation ending in an exclamation point which is the code below
    sentence = re.sub(r'!\s', '!\n', sentence)

#Lastly, we want to add a new line after punctuation ending in a question mark which is the code below
    sentence = re.sub(r'\?\s', '?\n', sentence)

    print(sentence)

sentence_splitter('examplelinesplitter.txt') #This is an example text file to test the program


"""Number 12
The purpose of this program is the create an anagram based off a list of words by rearranging the letters within a given word. 
"""
#Stuart- Hard coded filepath over rides file sent to function
# Stuart- The problem asks for you to find the set that contains the most words
# you have a good bit of code for finding anagrams in the list, but you need
# to find the set that contains the most anagrams.

def  anagram(filepath): #Here we define the function and use the parameter filepath
     filepath= open ('anagram.txt').read()   #Here we open the anagram.txt file, read it, and assign it to the variable filepath
     words=filepath.split()   #Here we want to remove all trailing spaces on each line
     for word_anagram in words:  #for every word_anagram, which is the rearranged word, in the list of words...
         for word in words:   #We search for all words in the list of words...
             if set(word)==set(word_anagram): #The set function allows us to manipulate unordered collections of unique elements...in this case letters. In this case, we create a new empty set object called word_anagram
                 if len(word)==len(word_anagram):  #If the length of the word is the same as the length of the rearranged word...
                     print (word, word_anagram)    #...then we print the word and the anagram of the word
      
print(anagram('anagram.txt')) #Here we print the results of running the program using the anagram.txt file



"""Number 13
The purpose of this program is to generate a string of N open and N close brackets in some order and determine if they are balanced, i.e. [] balanced and [[][ unbalanced
This program was difficult so I had some help from a few work colleagues who are very familiar with Python...my original program did not shuffle the brackets
"""
#Below we want to import the random range function for the random module...we also import the regular expression module
from random import randrange
import re

#Stuart- I had to fix some indentation issues. Make sure to use consistent indentation. Also you do not define the variable result
# which leads to an additional error. you define brackets_str, but later call for bracket_str. Also you don't gurantee paired number
# of open and close brackets.

def brackets(N):  #Here we define the function called brackets with the parameter n since we want to generate a string of N brackets
    i=0   #We assign zero to the variable i
    output=''   #We assign a text string to the variable output
    brackets = '[]'  #We assign the text string of brackets to the variable brackets
    #Below, we want to create a loop for evaluating the choice of N
    while i < N*2: #If i is less than N*2...
        output += brackets[randrange(len(brackets))]  #...then output equals a random range of the length of the brackets...this allows us to shuffle the brackets
        i+=1 #Here i is able to increase be an increment of one

    brackets_str = output   #This assignes the output to a new variable brackets_str
    #Here we want to remove all pairs ([[ or ]])of brackets using regular expressions so that they don't mis-nest
    while len(re.findall(r'\[\]', output)) > 0: #Here we remove the pairs of brackets by using the find all function
        output = re.sub(r'\[\]', '', output) #Here we remove the brackets and concatenate it

    if len(result) > 0: #If there are still pairs of brackets after we remove them...
        print(bracket_str, 'Not OK')   #...then we know this string is unbalanced and we print Not OK
    else:
        print(bracket_str, 'OK')    #otherwise we pring OK

#In this program, I used an example of N=10
brackets(10)



"""Pokemon - wasn't numbered
This program was extremely difficult, and I reached out to several people or guidence in creating this program.
"""

#Below we want to import the regular expressions module
import re

def pokemon_names(file_name): #Here we define the function pokemon_names
    with open(file_name, 'r') as f: #Here we open the file and read it and find all the names
        names = re.findall(r'\w+', f.read()) #Here we assign the variable names to all names with any character recognized and read them

#Here we create two lists names best_length and current_length
    best_length, current_length = [], []

#Here I was taught how to find the index of a word...in this case we want the index of the next word that begins with the last letter of the previous word
    def start_of_name(lastletter, names): #Here we create a function called start_of_name and assign the two variables lastletter and names
        for index, name in enumerate(names): #The enumerate function allows us to find the index of the letters in names
            if name.startswith(lastletter):  #If the name starts with the last letter of the next word, we index that letters spot and return it
                return index
        return False

    for name in names:  #For loop that looks at each name in the list of names
        current_name = name  #Here we assign the variable current_name to name
        current_length.append(current_name) #Here we want to add the add the current_name to the current_length of names

        namelist = names[:] #Here we can make a copy of the list of names
        namelist.pop(namelist.index(current_name)) #This was very tricky but the pop function (as I learned from others giving me examples) allows you to return the last item in the list which was were my main issue in this program lied

        index = name_starts_with(current_name[-1], namelist) #Now we want to get the index of the next name

        while index is not False:      #This will run as long as there is a name that starts with the last letter of the previous names
            current_name = namelist[index] #Here we are finding this name
            current_length.append(current_name) #Here we are appending the current_length by adding the name to it
            namelist.pop(index) #This allows us to remove it from the list (very tricky part)
            index = name_starts_with(current_name[-1], namelist) #Here we get the position of the next name by looking at the last letter

#Here is the current_length is greater than the best_length then we make a new best_length, which is equal to this current length of names
            if len(current_length) > len(best_length):
                best_length = current_length

                current_series = [] #This allows us to clear out the results for the next attempt at the loop
            else:
                break
        print(best_length) #Here we print the best_length or the longest length of names 

#This is an example to run the program...I copied the names and saved them to the file titled pokemon_names.txt. Again, I had to use many resources an people to help with this problem
#I knew how to index a list and find different positions of letters, reverse letters, and match letters.
#My problem was cycling through the names and removing them from the list, which is how I came accross the pop function
poke_names('pokemon_names.txt')



"""Number 14
The purpose of this program is to alternate between letters in a word to produce a set of new words.
This one was also very tricky for me and I had some help on this one from people who understand Python better. They introduced me to the "try, except, pass" sequence but I was able to implement it on my own
"""
#I was unable to open the words from the web browser...I tried many different ways and tried importing the web browser module, but it would not work for me.
#Therefore, I copied the list of words and saved them to a file names wordpuzzle.txt
f = open("wordpuzzle.txt",'r')  #Here we open the file named wordpuzzle.txt and read the contents
for line in f: #for each line in f...
    line = line.strip() #We want to strip the remaining '\n' on each line
    length = len(line)  #We assign the variable name length to the length of the line
    word_number_one = ""  #Here we assign word_number_one to a string
    word_number_two = ""  #Here we assign word_number_two to a string
    for i in range(0, length,2): #for i in a range of zero, the length of the word, and 2...
        word_number_one += line[i]   #Here word number one is equal to the index of line i. The next lines allow us to look for word number two 
        try:
            word_number_two += line[i+1]
        except:            #I was taught that the except pass allows us to avoid any signs of an error. I thought this was acceptable practice since 
            pass           #Not all the words in the list can create new words...and I wasn't sure if we needed to make an alternate for certain words or all words.
        word_number_one = word_number_one.strip()  #Here we remove trailing spaces
        word_number_two = word_number_two.strip()  #Here we remove trailing spaces
        print(word_number_one+" and "+word_number_two) #Here we print the newly created words. I checked through the list and noticed that some of the words didn't make sense...so I'm not sure if the whole "except pass" thing is good
