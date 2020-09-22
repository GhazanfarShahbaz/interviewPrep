"""Challenge : 1.6 String Compression
implement a method to perform a basic string compression using the counts of repeated characters for example the string aabcccccaa would become a2b1c5a3. If the compressed string would not become smaller than the original string your method should return the original string. You can assume the string has only uppercadse and lowecase letters"""
from one_one import testList 

def testList():
    """Genrates 255 random test strings"""
    testList = []
    for x in range(50):
        newString = ""
        for y in range(random.randint(0,50)):
            newLetter = ""

            if(random.randint(0,1) == 1):
                newLetter += chr(random.randint(97, 122))
            else:
                newLetter += chr(random.randint(65, 90))

            for z in range 
            
        testList.append(newString)
    return testList


    
def string_compression(string: str):
    parser = 0
    compressed_string = ""

    while(parser < len(string) and len(string) >= len(compressed_string)):

        currentLetter = string[parser]
        count = 1
        parser += 1

        # Gets the count of the current character
        for x in range(parser, len(string)):
            if(string[x] == currentLetter):
                count += 1
                parser += 1
            else:
                break

        compressed_string += currentLetter + str(count)

    if len(compressed_string) >= len(string):
        return string

    return compressed_string


if __name__ == "__main__":
    for x in testList():
        print(x, string_compression(x))
