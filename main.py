# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def check(a, b):

    if(sorted(a) == sorted(b)):

        print("True")

    else:

        print("False")
 

a = "TRIANGLE"
b = "INTEGRAL"
check(a, b)

