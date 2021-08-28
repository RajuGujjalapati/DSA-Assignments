"""
Use a stack to check whether or not a string
has balanced usage of paranthesis.

Ex: (), ()(), (({[]})) <-- Balanced.
    ((), {{{)}],[][]]] <-- Not Balanced.

"""

def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

from stack_lucidProg import Stack

def is_balanced(paren_string):
    s= Stack()
    is_balanced = True #setting to true
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]# initializing parenthesis
        if paren in "({[":
            s.push(paren)#pushing to list
        else:
            if s.is_empty():# checking empty or noe
                is_balance = False
            else:#taking the last element
                top = s.pop()
                if not is_match(top, paren):#ifthe last element
                    is_balanced = False
        index += 1

    if s.is_empty and is_balanced:
        return True
    else:
        return False
    
print(is_balanced("([[]])"))
#first storing the ([{ then once ]}) comes, it is matching the last stack(or we can which was
#in first place(top), if not we are returning False([)[()
#return only True --> if {([])} #like specific format
