#Password Generator ver 0.0.1 by Edo Spigel-Emmerich
import random
uppercase = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
lowercase = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numbers = ["0","9","8","7","6","5","4","3","2","1"]
special_characters = ["`","~" ,"@" ,"#" ,"%", "^", "&","*", "(", ")", "-", "_", "=","+", "[", "]", "{", "}", ".", ","]



# print len(uppercase) # 26
# print len(lowercase) # 26
# print len(numbers)   # 10
# print len(special_characters) # 20


def password_maker(length, uppercase_first=True):
    global uppercase, lowercase, numbers, special_charecters
    password = []
    if length < 6:
        print "Error, password to short"
        exit()
    if length > 12:
        print "Error, password to long"
        exit()

    if length == 6:
        password = []
        for x in range(2):
            password.extend(uppercase[random.randrange(26)])

        for x in range(2):
            password.extend(lowercase[random.randrange(26)])

        for x in range(1):
            password.extend(numbers[random.randrange(10)])
            password.extend(special_characters[random.randrange(20)])

    

        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "


    if length == 7:
        password = []
        for x in range(2):
            password.extend(uppercase[random.randrange(26)])

        for x in range(2):
            password.extend(lowercase[random.randrange(26)])
            password.extend(numbers[random.randrange(10)])
        for x in range(1):
            
            password.extend(special_characters[random.randrange(20)])

        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "

    if length == 8:
        password = []
        for x in range(3):
            password.extend(lowercase[random.randrange(26)])
        for x in range(2):
            password.extend(uppercase[random.randrange(26)])
            password.extend(numbers[random.randrange(10)])
        for x in range(1):
            
            password.extend(special_characters[random.randrange(20)])

        
        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "

    if length == 9:
        password = []
        for x in range(3):
            password.extend(lowercase[random.randrange(26)])
        for x in range(2):
            password.extend(uppercase[random.randrange(26)])
            password.extend(numbers[random.randrange(10)])
            password.extend(special_characters[random.randrange(20)])

        
        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "
    
    if length == 10:
        password = []
        for x in range(3):
            password.extend(lowercase[random.randrange(26)])
            password.extend(numbers[random.randrange(10)])
        for x in range(2):
            password.extend(uppercase[random.randrange(26)])
            password.extend(special_characters[random.randrange(20)])

        
        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "

    if length == 11:
        password = []
        for x in range(3):
            password.extend(lowercase[random.randrange(26)])
            password.extend(numbers[random.randrange(10)])
            password.extend(uppercase[random.randrange(26)])
        for x in range(2):
            password.extend(special_characters[random.randrange(20)])

        
        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "

    if length == 12:
        password = []
        for x in range(3):
            password.extend(lowercase[random.randrange(26)])
            password.extend(numbers[random.randrange(10)])
            password.extend(uppercase[random.randrange(26)])
            password.extend(special_characters[random.randrange(20)])
        
            

        
        print "Your unshuffled password is:"
        print( " ".join( str(x) for x in password ) )
        random.shuffle(password)
        print "Your shuffled password is:"
        print( " ".join( str(x) for x in password ) )
        print " "

# here create your password:
# Please note that passwords shorter than 6 and longer than 12 are invalid, and kill the program

# Syntax:
#        password_maker(6)
#        ^               ^
#         This creates a
#           password 6
#         characters long


#for x in range(6,13):
    #password_maker(x)

