# Van Huynh
# Program asks the user for a string and a shift amount and then display the ciphered string

my_str = input('Please enter a string to be ciphered: ')

# validate_shift ensures the input for shift is between 0-25 and an integer
def validate_shift():
    shift = input('Please enter a shift amount between 0 and 25: ')
    if shift.isdigit():
        if int(shift) >= 0 and int(shift) < 25:
            return shift
    else:
        return None

# if input (shift) doesn't meet the condition, program will ask again
shift = None

while shift == None:
    shift = validate_shift()


def shift_back(z_num, cap_or_no, new_word):
    global shift3
    shift1 = z_num - ord(letter)  # ensure this shift to z
    shift2 = int(shift) - shift1
    shift3 = ord(cap_or_no) + shift2 - 1  # shift the left overs shift after shifting to 
    new_word += chr(shift3)
    return new_word


new_word = ''

num = ''

for letter in my_str:
            
    z_shift = (ord(letter)+ int(shift))

    # if it's not a number or a alphabet, don't shift and put it back into the word
    if letter.isdigit() or letter.isalpha() == False:  
        num = letter
        new_word += num

    # if the range is between 97 and 127 and the letter itself is more than 97, then use this condition ('a' - 'z')
    # range from 65 and 91 is for capital letters
    
    elif (z_shift in range(97,123) and ord(letter) >= 97) or z_shift in range(65,91):
        new_word += chr(ord(letter) + int(shift))

    # if it's more than 122, which is after z, then program know that it needs to shift back bc it's more than z
    elif z_shift > 122:
        new_word = shift_back(122, 'a', new_word)
    
    # this is for capital letters shift back
    else:
        new_word = shift_back(90, 'A', new_word)
    
print(new_word)



            

    
