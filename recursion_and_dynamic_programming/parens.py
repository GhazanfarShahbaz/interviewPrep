def generateParens(num: int) -> list:
    if num == 0:
        return []
    parentheses = set()
    generate("()", parentheses, num)
    return parentheses


def generate(string: str, arr, n):
    if(len(string) == n*2):
        arr.add(string)
    else:
        for x in range(len(string)-1):
            if (string[x] == "(" and string[x+1] == ")") or (string[x] == "(" and string[x+1] == "(") or (string[x] == ")" and string[x+1] == ")"):
                generate(string[:x+1] + "()" + string[x+1:], arr, n)
        generate(string + '()', arr, n)

if __name__ == "__main__":
    for x in generateParens(9):
        print(x)