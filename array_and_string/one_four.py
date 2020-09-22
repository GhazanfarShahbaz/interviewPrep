"""Challenge : Palindrome Permutation
Question : Given a string, write a dunctioon to check if it is a permutation of a palindrome. A palindrome is a word. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangment of letters. The palinfrome ddoes not need to ebe limited to just dictionary words."""


testList = ['ab', 'aab', 'that', 'not', 'Tact Coa']

def permute(a: int, leftBound: int, rightBound: int, permutations: list):
    if leftBound == rightBound: 
        string = "".join(a)                                     # turns the string a list
        permutations.append(string)                             # appends to the permutation list
    else: 
        for i in range(leftBound, rightBound+1):
            a[leftBound], a[i] = a[i], a[leftBound]             # shifts the character
            permute(a, leftBound+1, rightBound, permutations)   # uses a recursion to shift the next characters
            a[leftBound], a[i] = a[i], a[leftBound]             # changes to original


def isPalindromePermutation(string: str):
    if(len(string) <= 2):
        return True
    newString = ""
    for x in string:
        if not(ord(x) >= 32 and ord(x) <= 64): # replaces whitespace and punctuation
            newString += x.lower()
    permutations = []
    
    permute(list(newString), 0, len(newString)-1, permutations)   # lowercase because if one letter is capital and the other is not then that may cause a true permutation to return false

    # print(set(permutations))
    for x in set(permutations):
        if x == x[::-1]:
            return True
    return False

if __name__ == "__main__":
    for x in testList:
        print(isPalindromePermutation(x), x)
