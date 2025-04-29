import random
import time
#This function is called randomly in game as a proposal from banker
def banker_calls_f():
    print("ring ring !!")
    print("Oh !! it's seems that we have a proposal from the banker")
    print('...')
    time.sleep(1)

#This function calculate the banker's offer
def banker_offer(x):
    s=0
    for i in range(len(x)):
        s+=x[i]

    return s/len(x)

print("Welcome to deal or no deal !!")
username=input('What is your name ?: ')
prizes=[0.01,1,10,50,75,100,500,1000,5000,10000,30000]
available_prizes=[0.01,1,10,50,75,100,500,1000,5000,10000,30000]
available_packs=[1,2,3,4,5,6,7,8,9,10,11]
list1=[] #The list1 is for the next loop and helps to not put an element in 
packs=[] #This list helps to input the elements in a random sequence 
i=0
#The loop that makes prizes in packs's list, randomly. 
while i<11:
    skr=random.randint(0,10)
    if skr not in list1: 
        list1.append(skr)
        packs.append(prizes[skr])
        i+=1

print("Ok",username)
print("You have these packs available: ",available_packs)
user_choice=int(input("which pack you want ?: "))
user_pick=packs[user_choice-1] #player's pick
packs.remove(packs[user_choice-1])
available_packs.remove(user_choice)
print("Great !! you chose the pack",user_choice,". So the available packs are: ",available_packs)
print("Let's start")
banker_calls=[]
calls=random.randint(1,3) # The times that banker want to call. The banker must to call maximum 3 times.

#This loop contains the calls of banker in the rounds
for i in range(1,calls+1):
    p=random.randint(4,10)
    banker_calls.append(p)

rounds=1
done='false'
#This loop is the main game
while rounds<=10 and done=='false':
    print("Round",rounds)
    if rounds in banker_calls:
        banker_calls_f()
        offer=banker_offer(packs)
        print("The Banker's offer is",round(offer,2),"$")
        agree=input("Do you want to deal ? (yes/no)")
        if agree=="yes":
            print("You accepted the Banker's offer. But the pack",user_choice,"that you had, what cost had ? Let's see.")
            print("...")
            time.sleep(1)
            print(user_pick,"$")
            done='true'
            players_prize=offer

    if done=='false' and rounds<=9:
        print("AVAILABLE PACKS: ",available_packs)
        print("AVAILABLE PRIZES: ",available_prizes)
        #print("The real packs of the game",packs)
        option=int(input("Which pack you want to remove ?: "))
        while option not in available_packs:
            
            if option==user_choice:
                option=int(input("This pack is already removed. Try with a pack from AVAILABLE PACKS: "))
        
        print("You removed..")
        time.sleep(1.5)
        index1=available_packs.index(option) #index1 variable helps to find the position of the option and after to delete it from available_packs's list
        index2=available_prizes.index(packs[index1])
        #print("The element ",option,"is in",index1,"position.")
        #print("The packs[index1] is",packs[index1])
        #print("The packs[index2] is",available_prizes[index2])
        print(packs[index1],"$")
        packs.remove(packs[index1])
        available_packs.pop(index1)
        available_prizes.pop(index2)
    if rounds==10 and done=='false':
        print("We are in the last round. We have the pack, that you chose at start, and a last one pack, in game.")
        print("YOU HAVE PACK NUMBER ",user_choice,"AND THE PACK NUMBER ",available_packs[0])
        print("AVAILABLE PRIZES: ",available_prizes)
        x=input("Do you want to swap the packs, or to keep the pack that you have ? (keep/swap): ")
        while x!='swap' and x!='keep':
            print("Wrong input try again.")
            x=input("Do you want to swap the packs, or to keep the pack that you have ? (keep/swap): ")
        
        if x=='swap':
            temp=user_pick
            players_prize=packs[0]
        else:
            players_prize=user_pick
            temp=packs[0]
    rounds+=1

if done=='false':
        print("You won ",players_prize,"$")
        if x=='swap':
            print("The pack that you had first, had",temp,"$")
        else:
            print('The last one pack of the game, had',temp,"$")
else:
    print("You lost",user_pick,"$",", but you won ",round(players_prize,2),"$")
