from sys import exit 
import random


objets = {'cart' : False, 'money' : False, 'eggs' : False, 'water' : False}

def where_now():
    print('Where to now? type "options" if you do not remember')
    while True:
        choice = input('>')
        if 'aisle one' in choice:
            aisle_one()
        elif 'aisle two' in choice:
            aisle_two()
        elif 'back room' in choice:
            checkout()
        elif 'start' in choice:
            start_room()
        else :
            print('You have to type aisle one, aisle two, backroom, or start to get to the main pub.')


def egg_choice():

    print('now do you pick up the eggs your mom asks for?')
    while True:
        choice = input(">")

        if 'yes' in choice:
            egg = True
            print('Now where would you like to go? Type options if you want to see your choices again.')
            print('hint: The aisle has access to another room ;)')
            while True:
                choice = input('>')
                if 'aisle one' in choice:
                    aisle_one()
                elif 'aisle two' in choice:
                    aisle_two()
                elif 'back room' in choice:
                    back_room()
                elif 'start' in choice:
                    start_room()
                else :
                    print('You have to type aisle one, aisle two, backroom, or start to get to the main pub')

        elif 'no' in choice:
            print('God! What a risk taker! Always living on the edge I love it')
            print('But will your mother love it...')
            print('Now where would you like to go? Type options if you want to see your choices again.')
            print('hint: The aisle has access to another room ;)')
            while True:
                choice = input('>')
                if 'aisle one' in choice:
                    aisle_one()
                elif 'aisle two' in choice:
                    aisle_two()
                elif 'back room' in choice:
                    back_room()
                elif 'start' in choice:
                    start_room()
                else :
                    print('You have to type aisle one, aisle two, backroom, or start to get to the main pub')
        else:
            print('type yes or no')


def intro_room():
    print('Your mother sends you to the store to buy a few things for her.')
    print('Because no matter what age you are,what mom says goes(ugh)you walk to the store.')
    print('Once you get there you have to choose whether or not you want a shopping cart  to take inside.')
    print('Do you want a shopping cart?')
    while True:
        choice = input("> ")
        if "yes" in choice:
            print('I mean of course you need a cart. Smart choice y/n. You take the cart and go inside.')
            objects['cart'] = True 
            start_room()

            
        elif "no" in choice:
            print("it was not really a choice...how are you going shopping without a cart?! you take the cart anyways and go inside")
            objects['cart'] = True 
            start_room()
            
        else:
           print('I will be gracious and let you try again...try typing yes or no genius ;)')
       
       
def start_room():
    
    print('You walk into your local bodega...Something seems off..')
    print('You put your hand in your pocket and realize your money is gone!!!Mom is gonna kill you.')
    print('Anyways, you walk in and see two aisles (aisle one and aisle two) ')
    print('and the checkout if you ever want to go to checkout you notice you have to come back to this pub')
    print('Where do you want to go?')
    while True:
        choice = input("> ")

        if 'aisle one' in choice:
            aisle_one()
        elif 'aisle two' in choice:
            aisle_two()
        elif 'checkout' in choice:
            checkout()
        else :
            print('You have to type aisle one, aisle two, or checkout ')
           

def aisle_one():

    print("Making your way down the dairy aile, walking fast, faces pass and you're food bound da da d-")
    print('OOFFF!! This kid bumps into you and says "watch out boomer". Shaking my head thats What happens when')
    print("you are born in 2011...kids these days. BUT WAIT, do not let him leave he has the envelope of money")
    print('your mother gave you. That sly kid probably found it on the ground.')
    print('You go up to the kid and say, "hey that is my money". The kid admits that it isnt his and he will only give you back')
    print('the money if you win in a game of rock, paper, scissors')
    print('Do you play?')
    while True:
        choice = input("> ")

        if 'yes' in choice:
            play = ["rock", "paper", "scissors"]

            kid = random.choice(play)
                
           
            YN = input("Hurry now! rock paper scissors SHOOT!")

            if YN == "rock":
                if kid == "paper":
                    print('you let a kid win...')
                    print( kid, "covers", YN)
                    egg_choice()
      
                else:
                    print("congrats no mad mom" )
                    print(YN, "crushes", kid)
                    objects['money'] = True 
                    egg_choice()
                    
            elif YN == "paper":
                if kid == "scissors":
                    print("you let a kid win..." )
                    print(kid, "cut", YN)
                    egg_choice()
                        

                else:
                    print("congrats no mad mom" )
                    print(YN, "covers", kid)
                    objects['money'] = True 
                    egg_choice()
                        

            elif YN == "scissors":
                if kid == "rock":
                    print("you let a kid win...")
                    print( kid, "crushes", YN)
                    egg_choice()

                else:
                    print("congrats no mad mom")
                    print( YN, "cuts", kid)
                    objects['money']= True
                    egg_choice()
                                

            else:
                print("I am pretty sure you have to say rock paper or scissors...try again bro")
                aisle_one()
               
        elif 'no' in choice:
            print('ok...maybe that was not smart but it is fine because #everyone makes mistakes')
            egg_choice()

def back_room():
    print('You walk to the back room and there is a freezer door, someone says it is a door to a eutopia.')
    print('Do you walk in?')
    while True:
        choice = input('>')
        
        if choice == 'yes' and money:

            dead('You died.You walk into the freezer and people take your money and lock you in there. This is America. There is no such thing as walking through doors.')

        elif choice == 'yes'  :
            print("It was a trick!! Elmo and Burt are tring to rob you but you dont have any money to give them.")
            print("For them to let you go you have to wear the red shirt Elmo gives you.")
            print("Do you wear the shirt or run?")
            while True:
                choice = input('>')

                if 'run' in choice:
                    print('Good job speedy....boy was that a nightmare on elm(o) street.')
                    where_now()

                elif 'wear the shirt' in choice:
                    dead('You round the corner to leave and the crips kill you for wearing red')
                else:
                    print(' say "run" or "wear the shirt"')
        elif 'no' in choice:
        where_now()
                
        else :
            print("PLEASE DEAR GOD SAY Run OR YES")
        
def aisle_two():   


    print('Your family runs through water bottles like crazy!! It might be because you have 1000 random water bottles in your room but it doesnt matter.')
    print('you mutter a faint "I hate this store" when you see a rainbow bear with sharp claws sitting near the cases of water as if it was guarding it.')
    print('"I wish this was the drugs" you hear an old man with a cane say to you. You ask "what am I supposed to do?" and he replies "eat it"')
    print('Do you eat the rainbow bear that has the most adorable big brown eyes you have ever seen or do you walk away without the water? hint:say eat it or walk away')
    while True:
        choice = input('>')
        if choice == 'eat it' and cart:
            water_cart = True 
            print('Your mother would be proud. You take the water case in the cart and go.')
            where_now()
                else :
                    print('You have to type aisle one, aisle two, backroom, or start to get to the main pub.')
                    

            

        elif 'walk away' in choice:
            print('You should listen to your mom but if the bear scares you its okay. ')
            where_now()
                


        else :
            print('How does a rabbi make coffee? Hebrews it!jokes, jokes but please type eat it or walk away')




def checkout():

    print('You made it to checkout!')
    print('As the cashier rings up what have or may not have you think about the time spent in the bodega..')
    print("'Is that all' she says. Exhausted you are ready to leave so you say...? hint: say yes or start to go back ...")
    while True:     
        choice = input('>')

        if choice == 'yes' and money and eggs and water:
            print('YOU DID IT! You did your time, you took your chances, you are just a man with a will to survive...')
            print('https://www.youtube.com/watch?v=btPJPFnesV4')
            exit()
        elif choice == 'start' :
            start_room()
        else :
            dead('You failed...you either dont have money eggs or the water so moms gonna be mad OooOOoOoOoooo')

intro_room()

