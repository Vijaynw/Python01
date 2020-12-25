''''
                                           Python Exercise 1 - Apni Dictionary
Problem Statement:
So, in this tutorial i.e. Python exercise 1 tutorial, what we have to do is to create a dictionary, similar to the real-world dictionary. There is no limit to the definition you provide to any word as this exercise is just for your practice.

The details and functionalities that are essential and must be present are:

User will give a word as an input. Suppose that the word is present in your dictionary along with its definition or meaning.
The program will print the meaning or definition of that word.'''


dict= {"ignore":"refuse to take notice of or acknowledge", "abandon":"cease to support or look after",
            "exaggerate":"enlarged or altered beyond normal proportions", "prejudice":"preconceived opinion that is not based on reason or actual experience"}
print('enter the word')

i=input()
print(i,'means', dict[i])


