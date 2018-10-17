# Van Huynh
# program determines whether an input year is a leap year

def leap():
    year = int(input('Please enter a year: '))
    
    if year % 4 == 0: # if year is divisible by 4
        if year % 100 == 0: # if divisible by 4, then evaluable if it's divisible by 100
            
            if year % 400 != 0: #if it is not divisible by 400, then it's not a leap year
                
                print(year, 'is not a leap year.') 
            else:
                print(year, 'is a leap year.') # if divisible by 400, then it is
        else:
            print(year, 'is a leap year.') 
    else:
        print(year, 'is not a leap year.') #if not divisible by 4 then it's not a leap year

leap()
