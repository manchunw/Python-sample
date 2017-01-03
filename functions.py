# check whether x is even
def is_even(x):
    return x % 2 == 0

# check whether x is integer
def is_int(x):
    return isinstance(x, int) or x.is_integer()

# sum up all the digits
def digit_sum(n):
    ds = str(n)
    n = 0
    for s in ds:
        n = n + int(s)
    return n

# calculate factorial of n
def factorial(n):
    p = 1
    for a in range(n):
        p = p * (a+1)
    return p

# check whether x is prime
def is_prime(x):
    if x <= 1:
        return False
    for i in range(x-3):
        if x % (i+2) == 0:
            return False
    return True

# parse reverse of string
def reverse(text):
    s = ''
    for t in text:
        s = t + s
    return s

# remove char that contains vowels in string
def anti_vowel(text):
    vowels = ['a','e','i','o','u']
    s = ''
    for t in text:
        is_vowel = False
        for v in vowels:
            if t.lower() == v:
                is_vowel = True
        if is_vowel == False:
            s = s + t
    return s

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
# map char to value and sum up all the values
def scrabble_score(word):
    n = 0
    for w in word:
        n = n + score[w.lower()]
    return n

# censor the word and filter with astericks
def censor(text, word):
    tss = text.split()
    for i in range(len(tss)):
        if tss[i].lower() == word:
            l = len(word)
            tss[i] = "*" * l
    return " ".join(tss)

# count item appears how many times in the sequence
def count(sequence, item):
    cnt = 0
    for s in sequence:
        if s == item:
            cnt = cnt + 1
    return cnt

# remove odd numbers in an array
def purify(arr):
    ans = []
    for n in arr:
        if is_even(n):
            ans = ans + [n]
    return ans

# calculate product of array
def product(arr):
    ans = 1
    for a in arr:
        ans = ans * a
    return ans

# remove duplicates
def remove_duplicates(arr):
    ans = []
    for a in arr:
        unique = True
        for b in ans:
            if a == b:
                unique = False
        if unique:
            ans = ans + [a]
    return ans

# calculate median of array
def median(a):
    arr = sorted(a)
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr[0]
    else:
        val = len(arr) / 2
        if is_even(len(arr)):
            return (arr[val-1] + arr[val]) / 2.0
        else:
            return arr[val]