"""Challenge : 1.3 Urlify
Description: Write a method to replace all the spaces in the in a string with '%20'. You may assume that the string has sufficient space st the end to hold the additional characters, and that you are given the true length of the string."""


def urlify(string: str, length: int):
    newString = list(string.rstrip())
    print(len(string))
    for x in range(len(newString)):
        if newString[x] == " ":
            newString[x] = "%20"
    return "".join(newString).strip()


if __name__ == "__main__":
    test = "Mr John Smith"
    print(urlify(test,13), len(urlify(test,13))
