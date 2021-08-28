"""
Using Stack DataStructure(before we coded) Convert integer to Binary

Ex : 242

242 / 2 =121--> 0
121 /2 =60 --> 1 #floor division
60 / 2 = 30 --> 0
30 / 2 = 15 --> 0
15 / 2 = 7 --> 1
7 / 2 = 3 --> 1
3 / 2  = 1 --> 1
1 / 2  = 0 --> 1
int('11110010', 2)--> gives us real number
"""

from stack_lucidProg import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num >0:
        remainder = dec_num %2
        s.push(remainder)
        dec_num = dec_num // 2
        print(s.get_stack())

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_2(243))
