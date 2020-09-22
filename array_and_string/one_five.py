"""Challenge : 1.5 One Away
Description : There are three types of edits that can be performed on strings, insert a charachter remove a character or replace a character, Given two strings write a function to check if they are one edit or zero eidts away"""


def one_away(strOne: str, strTwo: str):
    if strOne == strTwo:
            return True
    if len(strOne)-1 > len(strTwo):    # This means that the string it too long that an insertion or deletion will not make a difference
        return False
    
    sameChars = 0
    leftCarry = 0
    rightCarry = 0
    
    for x in range(len(strOne)):
        if x + rightCarry > len(strTwo)-1 or leftCarry+x > len(strOne)-1:
            break
        if strOne[x+leftCarry] == strTwo[x+rightCarry]:
            sameChars += 1
        elif x+1+rightCarry < len(strTwo) and strOne[x+leftCarry] == strTwo[x+rightCarry+1]:
            rightCarry += 1 
            sameChars += 1
        elif x+1+leftCarry < len(strOne) and strOne[x+leftCarry+1] == strTwo[x+rightCarry]:
            sameChars += 1
            leftCarry += 1
    return sameChars + 1 == len(strOne)


if __name__ == "__main__":
    print(one_away('pale', 'bale'))
    print(one_away('pales', 'baled'))
    print(one_away("al", "fa"))
    print(one_away('p', ''))
    print(one_away('ab', 'b'))