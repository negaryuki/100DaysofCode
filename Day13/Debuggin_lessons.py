# Debug the below codes:

#def my_function():
#    for i in range(1,20):
#        if i ==20:
#            print("you got it")
#            
            
#my_function()


# Explaining the problem: since "i" will loop through 1 to 19 => i = 20 will never occur

def my_function():
    for i in range(1,21):
        if i ==20:
            print("you got it")
            
            
my_function()

#-------------------------------------------------------------------------------------------
# Reproducing buggs 



#from random import randint 
#dice_imgs =["1", "2" , "3" , "4", "5" , "6"]
#dice_num = randint(1,6)
#print(dice_imgs[dice_num])


# The bug is that occasionally there might be an error and it's because list index starts from 0 => in this example the index range is from 0,5 

from random import randint 
dice_imgs =["1", "2" , "3" , "4", "5" , "6"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

#-------------------------------------------------------------------------------------------
#Play Computer

#year = int(input("what is your year of Birth?"))

#if year > 1980 and year < 1994:
#    print("you are a millenial.")
#elif year >= 1994:
#    print(" you are Gen Z")
    
    
    



year = int(input("what is your year of Birth?"))

if year > 1980 and year < 1994:
    print("you are a millenial.")
elif year >= 1994:
    print(" you are Gen Z")
    
#-------------------------------------------------------------------------------------------

# Print is your Friend. use it to debug the codes

#pages = 0
#word_per_page = 0
#pages = int (input("number of pages: "))
#word_per_page == int(input("number of words per pages"))
#total_words = pages * word_per_page
#print(total_words)



pages = 0
word_per_page = 0
pages = int(input("number of pages: "))
word_per_page = int(input("number of words per pages"))
total_words = pages * word_per_page
print(total_words)
