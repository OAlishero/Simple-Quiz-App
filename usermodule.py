from threading import Thread 
import time 
from os import system, name 
###################################################################################################
#Lists
##################################################################################################
answers= ["1","2","3","4","1","baton","usain bolt","jim ryun","110h","1"]

questions= ["Who won the 2019 World Championship 100m final? \n (1) Christian Coleman    (2) Justin Gatlin   (3) Noah Lyles  (4) Usain Bolt ", 
"What is the longest running event in olympics? \n (1) 10,000m     (2) Marathon    (3) 30 miles    (4) Ultra-marathon ", 
"A ________________ relay is when there are 4 members in each lane and each person runs one whole lap.\n (1) 800m    (2) 1000m     (3) 1600m     (4) 400m ", 
"Which country won the most olympic medals? \n (1) France    (2) Russia     (3) China     (4) United States ", 
"What is considered by many the hardest event in track? \n (1) 800m    (2) marathon     (3) 100m     (4) ultra-marathon ", 
"What do you call a device that you pass on to your teammate during a relay? (type lowercase) ", 
"Which man's world records in 100m and 200m still hold today?(type all lowercase)", 
"Who was the first high school runner to run a mile under 4 minutes?(type all lowercase)", 
"What is the shortest hurdling event? (add h after the number)",  
"What place did Brooklyn Tech Track Team come in outdoor season of 2019?"]

user_answers= ["0","0","0","0","0","0","0","0","0","0",] 

wrong= []
s=[" ,"]

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

o = 0 
def check():
    time.sleep(5)
    if o != 0:
        return 
    else: 
        timeover()
 
######################################################################
#INTRODUCTION
######################################################################
def intro():
    print("Hello! Do you wish to participate in trackacademics? A quiz that tests your knowledge \nin history and basics of Track and Field? (yes/no)\n")
    ans= input() 
    print()
    if ans=="yes" or "Yes" or "YES": 
        print("Awesome! we will begine sortly after we give you an overview. First 5 questions will be \nmultiple choice, you only have to type in the number. (E.g. input '1' to pick the first \nchoice). The rest will be open ended questions, make sure not to make spelling mitakes!\nYou'll have 60 seconds to answer all 10 questions.\n") 
        print("How to type names: 'donald trump' how to type hurdle events: '200h' '300h'\n \n")
    else: 
        print("Oh well! Cya later then.")
        quit() 
    print("Type ready to start!")
    rdy= input() 
    if rdy=="ready" or "Ready":
        clear() 
        print("START!")
        print()


######################################################################
#ASKING QUESTIONS 
######################################################################
def quiz():  
    n=0
    while n<10:
        Thread(target = check).start()
        print("\nQuestion " +str(n+1)+":") 
        print(questions[n]) 
        o = input()
        user_answers.append(o) 
        n+=1         
######################################################################
#GRADING
######################################################################
    if user_answers==answers: 
        print("You got all the questions right! NERD!")
    else: 
        for i in range (0,10):
            if user_answers[i]!=answers[i]:
                i+=1 
                wrong.append(str(i))
            else: 
                i+=1 
        if len(wrong)==1 : 
            print("Your response to question: "+ ", ".join(wrong)+" is incorrect.")
            print("Your total score is: "+str((10-len(wrong))*100/10.0)+"/100.0") 
        else: 
            print("Your responses to questions: "+ ", ".join(wrong)+" are incorrect.") 
            print("Your total score is: "+str(len(wrong)*100/10.0)) 


def quiz2():
    n=0 
    quiz() 
    return 

def timeover(): 
    print("Time over. You weren't FAST enough!\nDo you wish to try again?(yes/no)")
    again= input() 
    if again=="yes" or "Yes" or "YES":
        clear() 
        quiz2() 
    else:
        print("\nAlright, Cya later") 
        quit()

def quizprogram(): 
    intro() 
    quiz()     

###########################################################    
quizprogram() 