# Take an input string parameter and determine: 
# For all pairs of digits where there are exactly 3 question marks between them,
# do all pairings add up to 10.
# ("arrb6???4xxbl5???eee5", True),
# ("acc?7??sss?3rr1??????5", True),
# ("5??aaaaaaaaaaaaaaaaaaa?5?5", True),
# ("9???1???9???1???9", True),
# ("aa6?9", False),
# ("8???2???9", False),
# ("10???0???10", False),
# ("aa3??oiuqwer?7???2", False)

def solution(string):
    output = False
    count = 0
    lnum = None
    for i in string:
        if i.isdigit():
            if lnum:
                if count == 3:
                    if lnum + int(i) != 10:
                        return False
                    else:
                        output = True
            lnum = int(i)
            count = 0
        elif i == "?":
            count += 1
    return output