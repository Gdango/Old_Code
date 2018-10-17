# Van Huynh
# ask the user for a noun and prints out its plural form

def plural():
    word = input('Please enter a word: ')
    new_word = 'Not'
    # defining the condition when word end with f
    if word[-1] == 'f':
        word_temp = word[0:len(word)-1]
        new_word = word_temp+'ves' # word_temp = temperary variable for word
        print('The plural form of', word, 'is', new_word+'.')
        return new_word

    elif word[-2]+word[-1] == 'fe':
        
        word_temp = word[0:len(word)-2] # word_temp = temperary variable for word
        new_word = word_temp+'ves'
        print('The plural form of', word, 'is', new_word+'.')
        return new_word

    # putting es and ies conditions in the same for loop
    es_list = ['ch', 'sh', 's', 'x', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    
    for y in range(0,len(vowels)-1):
        # define conditions for es
        
        if y < 2:  # for first 2 items on the es_list so then I can use word[-2]
            # ch & sh have different lengths from s, x, z 
            if word[-2]+word[-1] == es_list[y]:
                new_word = word+'es'
                print('The plural form of', word, 'is', new_word+'.')
                return new_word
        if y >= 2:  
            if word[-1] == es_list[y]:
                new_word = word+'es'
                print('The plural form of', word ,'is', new_word+'.')
                return new_word
                
        # define conditions for s 
        if y < len(es_list):
            if word[-2] == vowels[y]:  #if the 2nd to last letter = vowels
                if word[-1] == 'y':
                    new_word = word+'s'
                    print('The plural form of', word,'is', new_word+'.')
                    return new_word
    #define conditions for 'ies'
        
    if word[-2] != 'o' or word[-2] != 'e' or word[-2] != 'i' or word[-2] != 'a' or word[-2] != 'u':
        if word[-1] == 'y':
            new_word = word.replace(word[-1], 'ies')
            print('The plural form of', word, 'is', new_word+'.')
            return new_word

    # if new_word didn't go through other ifs, it'll still equal to the pre-define...
    # ...word ('Not')
    if new_word == 'Not':  
        new_word = word+'s'
        print('The plural form of', word, 'is', new_word+'.')
        return new_word

plural()
