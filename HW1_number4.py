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
               os.system('say ' + d[char.lower()]) #Here we use the os library to prob
               time.sleep(0.1)
               time.sleep(1)

speak_icao("Hi,I am a student")
