# --------------
def palindrome(num):
    while(1):
        num += 1
        if str(num) == str(num)[::-1]:
            return num


# --------------
#Code starts here
def a_scramble(str_1, str_2):
    a = str_1
    b = str_2
    count = 0
    for i in b.lower():
        if i in a.lower():
            count += 1
            d = a.index(i)
            a = a[:d]+a[d+1:]
    if count == len(b):
        return True
    return False


# --------------
#Code starts here
def check_fib(num):
    a = 0
    b = 1
    while(a <= num):
        if a == num:
            return True
        else:
            c = a
            a = a + b 
            b = c
    return False 


# --------------
#Code starts here
def compress(word):
    a = ''
    c = word[0].lower()
    count = 0
    for i in word.lower():
        if i not in c[-1]:
            a += c[-1] + str(count)
            c += i
            count = 1
        else:
            count += 1
    a += i + str(count)        
    return a


# --------------
#Code starts here
def k_distinct(string,k):
    b = set(string.lower())
    if len(b) == k:
        return True
    return False


