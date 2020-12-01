# Project 4: Security System
# This exercise is to fully utilize boolean, string etc..


# Database of users

usersList = ['Martin' , 'Julie' , 'Pranav' , 'Jess' , 'Joy']

# User input
while True:
    user = input('''Hello my name is Jarvis, please login so I can help you.
    Name: ''').strip().capitalize()

# Compare user input with database

    if user in usersList:
        print('Hello, {}! How can I help you?'.format(user)) 
        userRemove = input('''Would you like to remove your name?
        Yes type keyboard "y"
        No type keyboard "n": ''')
        
        if userRemove == 'y':
            newLst = usersList.remove(user)
            print('New List: ', usersList)
        elif userRemove == 'n':
            print('Good, glad you are staying.')
            
    else:
        newUserRespond = input('''Sorry {}, you are not registered.
        Would you like to register? 
        Yes, type keyboard "y"
        No, type keyboard "n": '''.format(user)).strip().lower()
    
        if newUserRespond == 'y':
            print('Old List: ', usersList)
            newList = usersList.append(user)
            #print('Old list: ', usersList)
            print('New List: ', usersList)
        elif newUserRespond == 'n':
            print('Okay, goodbye.')
               
