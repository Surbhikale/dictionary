
#Writing code for Project On SPY_CHAT
#Date-1/07/2018
#Author-surbhi kale


#============================import files and library=========================================================
from steganography.steganography import Steganography      # import steganography library
import sys                                                 # import sys library for exit application
from default import spy,friend                             # import default.py file (default user info)
from default import Spy
import csv

#==================================start_chat()  function method==============================================================

def Start_chat(Spy):                                         # defination of start chat function
    current_status_msg = None                                # current status messages
    if spy.age > 12 and spy.age < 60:                        # validation for spy_age

        print("Authentication complete!\n Welcome\n %s\n age - %d and rating %.2f" %(spy.name,spy.age,spy.rating))

        show_menu = True                                      # status udate statement
        while show_menu == True:                              # adding a menu bar in chat function
            print("========MENU========\n")
            menu = """what do you want to do?
                    1. update a status
                    2. Add a new friend
                    3. Send a secrate message
                    4. Read a personal a meesage
                    5. Read chat from users
                    6. Load friends
                    0. exit"""

            menu_choice = input(menu)                        # choosing menu_choice
            menu_choice = int(menu_choice)                   # typecasting string to integer

            if menu_choice == 1:                                                # status update module
                current_status_msg = add_status(current_status_msg)             # current_status updated
                print("your current status is %s" %(current_status_msg))        # print updated status

            elif menu_choice == 2:                                              # add friend module
                print("add friend")
                add_your_friend = add_friend()
                print("YOUR FRIEND %s IS SUCCESSFULLY APPEND" %friend[0]['name'])
                print("YOU HAVE %d FRIEND NOW" %add_your_friend)

            elif menu_choice ==3:
                print("Send a secrate message")
                send_message()
#====================Send a secrate message=====================================
            elif menu_choice == 4:
                print("Read a personal a meesage")
                read_message()
#===================Read a personal message=====================================
            elif menu_choice == 5:                                              # Read chat from users
                print("Read chat from users")

            elif menu_choice == 6:
                print("load friends")

            elif  menu_choice == 0:
                show_menu = False
                sys.exit()                                                      # defalut statement
            else :
                print ("ooops! you have enter a wrong choice")
    else:
        print("Sorry! you don't have correct age to be an spy user")

#=================================Add_status() function method===========================================

def add_status(current_status_msg):
    if current_status_msg != None:
        print("your current status is %s" %(current_status_msg))
    else:
        print("you do not have any status right now")
        default = raw_input("Do you want to select status form your older status(y/n)?")
        if default.upper() == 'N':
            new_status_msg =raw_input("Add your new status?")
            if len(new_status_msg)>0:
                updated_status = new_status_msg
                STATUS_MESSAGE.append(new_status_msg)
            else:
                print("you have not enter any status\n please try again")
        elif default.upper() == "Y":
            iteam_pos = 1
            if STATUS_MESSAGE == []:
                print ("you don't have any older status message")
            else:
                for message in STATUS_MESSAGE:
                    print("%d , %s" %(iteam_pos,message))
                    iteam_pos = iteam_pos + 1

            while True:
                status_slection = int(raw_input("slect choice from above status"))
                if status_slection > len(STATUS_MESSAGE):
                    print("invalid choice\nplease try again")
                else:
                    updated_status = STATUS_MESSAGE[status_slection - 1]
                    break
        else:
            print("invalid entry\ntry again")
        return updated_status

#=========================(Fn for read the file)==========================

def load_friends():
    with open("db.csv",'rb') as friends_data:
        reader = csv.reader(friends_data)
        for row in reader:
            new_friend = {'name' : row[0],
                  'salutation' : row[1],
                  'age' :row[2],
                  'rating' : row[3],
                  'is_online' :row[4]
                 }

    friend.append(spy_friend)


#==============================add_friend() function=======================================================

def add_friend():
    new_friend = {'name' : " ",
                  'salutation' : " ",
                  'age' : 0,
                  'rating' : 0.0,
                  'is_online' : True
                 }
    new_friend['name']= raw_input("Enter a friend name ")
    new_salutation =raw_input ("what should call your friend(mr./miss.)? ")
    new_friend['name'] = new_salutation + " " +new_friend['name']
    new_friend['age'] = int(input("Enter your friend age "))
    new_friend['rating'] = float(raw_input("Enter your friend rating? "))


    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] < 60:
        friend.append(new_friend)
        with open("db.csv",'a') as friend_data:                                 # a append friends in a file
            writer = csv.writer(friend_data)
            writer.writerow([new_friend["name"],new_friend["salutation"],new_friend["age"],new_friend["rating"],new_friend["is_online"]])
    else:
        print("sorry! your friend does not must one invalid to be spy user")
    return len(friend)

#====================sending a secrate message to friend fn=====================

         #=============slect a friend from list =================

def slect_a_friend():
    friend_choice = 0
    for frnd in friend:
        print("%d  %s" %(friend_choice+1,frnd['name']))
        friend_choice += 1

    user_choice = input("slect a friend from the list :")
    choice = user_choice-1
    return choice

        #==============send a secrate message =====================
def send_message():
    frnd_choice = slect_a_friend()
    original_image = raw_input("enter the name of image:")
    output_image = "output.jpg"
    text = raw_input("enter the secrate message here:")
    Steganography.encode(original_image,output_image,text)
    print("your message is sent SUCCESSFULLY:")

def read_message():
    sender = slect_a_friend()
    output_path = raw_input("enter the name of image:")
    secrate_text = Steganography.decode(output_path)
    print("your secreate message is:%s" %secrate_text)

#===============================Main fn start_chat==============================


Question = "welcome to spychat /n are you an default user (y/n)?"               #asking a question from a user side
choice = raw_input(Question)
STATUS_MESSAGE = ['Busy' , 'At collage' , 'can not talk to me']                 #history previous status list

#=======================introduce friend function=============================

friend = []

if choice == "Y" or choice == "y":                                              #continue with defalut user information
    Start_chat(Spy)                                                             #start chat function

#=====================continue with new user information========================

elif choice == "N" or choice == "n":                                            #continue with default user info
    spy_name = raw_input("Tell me your Name first: ")
    if len(spy_name)>0:
        spy_salutation = raw_input("Welcome "+spy_name+ " What should I call you Mr./Miss.?")
        spy_name = spy_salutation+ "" +spy_name
        spy_age = raw_input("Ok " + spy_name +" Enter your age: ")
        spy_age = int(spy_age)
        if spy_age>12 and spy_age<60:
            spy_rating = raw_input("How much you like it ")
            spy_rating = float(spy_rating)                                      #typecasting from str to float
            if spy_rating>4.5:
                print("great you are an ace user")
            elif spy_rating<=4.5 and spy_rating>=3.5:
                print("good soon to be an ace")
            elif spy_rating<=3.5 and spy_rating>=2.5:
                print("you are doing good")
            else:
                print("true more u can do better")

                spy_is_online = True

#=============checking spy is online or not by define a boolean datatype========

                print("Welcome")
                print("%s age: %d and rating: %g We are proud to have you onboard" %(spy_name,spy_age,spy_rating))

#==========================use place holder %s,%d,%f============================
        else:
                print("Ooops! Sorry,you are not of correct age to be our spy")
    else:
        print("Sorry,you have entered an invalid Name!")
