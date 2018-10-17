# Van Huynh
# hangman.py

'''
This program allows the user to put in a secret word and another player make guesses until
the number of tries runs out
'''

################################ PRINT HANGMAN ###########################
def print_hangman(num):
    if num >= 0: print(' '+'|'+' ')
    if num >= 1: print(' '+'0'+' ')
    if num == 2: print(' '+'|'+' ')
    if num == 3: print('/'+'|')
    if num >= 4: print('/'+'|'+'\\')
    if num == 5: print('/')
    if num >= 6: print('/'+' '+'\\')
    print(' ')

############################### VERIFY WORD ##############################
'''ensure the secret word meets the conditions'''
def verify_word():
    user_guess = None
    
    while user_guess == None:
        word = input('Please enter a word to be guessed\n'
                           'that does not contain ? or white space: ')
        
        if (word.find(' ') != -1) or (word.find('?')!= -1): word = None
        else: return word
        
############################### VERIFY GUESS #############################
'''ensure the guess meets the conditions'''
def verify_guess(new_guess):
    user_guess = None
    while user_guess == None:
        user_guess = input('Please enter your next guess: ')
        if user_guess == ' '*len(user_guess):
            print('You must enter a guess.')
            user_guess = None
            continue
    
        if len(user_guess) != 1:
            print('You can only guess a single character.')
            user_guess = None
            continue
        if user_guess in new_guess:
            print('You already guessed the character:', user_guess)
            user_guess = None
        
    return user_guess

############################ CORRECT LETTERS #########################

'''check whether the letters are correct and replace ? with the correct letters
input is word, guess and ???? (unknown)'''
'''return is the new unknown with letters in'''

def correct_letters(word, guess, unknown):  
    
    for i, letters in enumerate(word):
        if letters.lower() == guess:
            unknown = list(unknown)
            
            if letters.isupper(): guess = letters  # turns guess to uppercase if needed
            
            unknown[i] = guess
            unknown = ''.join(unknown)
      
    return unknown  # return the unknown

############################## PRINT GUESS ###############################

### starting main fct###
def main():
    word = verify_word()
    print('\n'*30)

    ###'''PRINTING ???'''###
    word_len = len(word)  # printing ???
    unknown = '?'*word_len
    print(unknown)

    # initialize word have guessed
    print('So far you have guessed: ')
    new_guess = ''
    num = 0

    while num <= 6:

        ###'''CONFIRMING IF YOU HAVE GUESSED THE SECRET WORD'''###
        
        guess = verify_guess(new_guess)     # asking to enter next guess
        
        ##'''STARTING COMPARISON'''##
        if guess == new_guess:  # if letter is already guessed, skip the comparison
            continue
        
        if guess in word.lower():    
            unknown = correct_letters(word, guess, unknown)  # using a fct

        if unknown == word:
            print('You correctly guessed the secret word:', word)
            break
        
        print(' ')
            
        ###'''PRINTING LETTERS HAVE GUESSED'''###
        
        new_guess += guess
        have_guessed = ', '.join(sorted(list(new_guess)))
        
        if (guess in word.lower()) == False:
            
            print_hangman(num)
            num += 1
            if num == 7:
                print('You failed to guess the secret word:', word)
                break
        else:
            print_hangman(num - 1)
            
        print(unknown)
        print('So far you have guessed:', have_guessed)
    
main()    







    




    
        
