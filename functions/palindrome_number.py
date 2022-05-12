def palindrome_number(x):
    '''
    `palindrome_number` is a function which finds returns true if the given 
    number's digits can be reversed resulting in the same number.  For example
    121 is a palindrome number but 123 is not (321 != 123).
    '''
    temp = x
    reverse = 0
    while(x>0):
        dig = x%10
        reverse = reverse*10 + dig
        x = x//10

    if temp == reverse:
        return True
    else:
        return False



