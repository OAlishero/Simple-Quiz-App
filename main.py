from threading import Thread 
import time 
from os import system, name 
from termcolor import colored
import json 
import urllib.request

############################################################################################
#Dictionaries
#Lowercase
#File.io 
def clean(string): #Make inputs insensitive to lowercase/uppercase, unnecessary spaces, and phone number formatting  
  string=str(string) 
  string=string.casefold() 
  string=string.strip() 
  return string

############################################################################################
#Load Files 
##################################################################################################
with open("questions.json", "r") as read: 
    questions = json.load(read)
with open("answers.json", "r") as read: 
    answers = json.load(read)


user_answers= [] 

wrong= []
s=[" ,"]

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

o = 0 
 
######################################################################
#INTRODUCTION
######################################################################
def intro():
    print("Hello! Do you wish to participate in trackacademics? A quiz that tests your knowledge \nin history and basics of Track and Field? (yes/no)\n")
    ans= input() 
    print()
    if ans=="yes": 
        print("Awesome! we will begin shortly after we give you an overview. First 5 questions will be \nmultiple choice, you only have to type in the number. (E.g. input '1' to pick the first \nchoice). The rest will be open ended questions, make sure not to make spelling mitakes!\nYou'll have 10 seconds to answer each question.\n") 
        print("How to type names: 'donald trump' how to type hurdle events: '200h' '300h'\n \n")
    if ans=="no": 
        print("Oh well! Cya later then.")
        quit()   
    print("Type anything to start!")
    rdy= input() 
    if rdy!= None:
        clear() 
        print("START!")
        print()    


######################################################################
#ASKING QUESTIONS 
######################################################################
def quiz(t):  
    n=0
    while n<10:
        timeStart = time.time()
        print("\nQuestion " +str(n+1)+":") 
        print(questions[str(n+1)]) 
        o = clean(input())
        if time.time() - timeStart >= t:
            timeover(t)
        else:
            user_answers.append(o)
        n+=1
######################################################################
#GRADING
###################################################################### 
    for i in range (0,10):
        if user_answers[i]!=answers[str(i+1)]:
            i+=1 
            wrong.append(str(i))
        else: 
            i+=1 
    if len(wrong)==0 : 
        print(colored("\nYou got all the questions right! NERD!", "blue"))
        print(colored("Your total score is: "+str((10-len(wrong))*100/10.0)+"/100.0", "green"))
        quit() 
    if len(wrong)==1 : 
        print(colored("Your response to question: "+ ", ".join(wrong)+" is incorrect.", "red"))
        print(colored("Your total score is: "+str((10-len(wrong))*100/10.0)+"/100.0", "green"))
    else: 
        print(colored("Your responses to questions: "+ ", ".join(wrong)+" are incorrect.", "red"))  
        print(colored("Your total score is: "+str(((10-len(wrong))*100)/10.0), "green"))
    return  



def timeover(t): 
    print("Didn't answer in time. \nDo you wish to try again?(yes/no)\n(Less time will be given)")
    again= input() 
    if again=="yes" or "Yes" or "YES":
        clear() 
        quiz(t*3/4) 
    else:
        print("\nAlright, Cya later") 
        quit()

def quizprogram(t): 
    intro() 
    quiz(t)     

###########################################################    
quizprogram(30) 