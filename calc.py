# S -> S*S | S + S | S / S | S - S| (S) | a
# T = {* / + - [0-9]*  ( )}
#
from os import O_TMPFILE


operators_1 = ["*", "/"]
operators_2 = ["-", "+"]
operators = ["*", "/", "-", "+"]
T = ["*", "/", "+", "-", "(", ")", "0", "1", "2", "3", "4", "5", "6", "7", "8" , "9", "."]
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def check(s):
    for i in s:
        if i not in T:
            print("символ не из алфавита: ", s[i])
            return False
    return True

def calc(string):
    # print(string)
    s_itog = 0
    i = 0
    f_operator = -1
    s_operator = -1
    llen = len(string)
    if(llen == 0):
        return 0

    while i != llen:
        if(string[i] in operators_1 and s_itog == 0):
            f_operator = i
        elif(string[i] in operators_2 and s_itog == 0):
            s_operator = i
        elif string[i] == '(':
            s_itog +=1
        elif string[i] == ')':
            s_itog -=1
        i +=1
    
    if(s_itog != 0):
        print("Незакрытая скобка: ", string)
        return None

    if f_operator != -1:
        i = f_operator
    if s_operator != -1:
        i = s_operator

    if i == llen:   # S -> (S) | a
        if is_number(string):
            return float(string)
        if(llen == 2):
            print("пустая скобка")
            return None
        return calc(string[1:-1])
    
    calc_1 = calc(string[:i])
    calc_2 = calc(string[i+1:])
    if calc_1 is None or calc_2 is None:
        return None
    elif (((i > 0) and string[i-1] in operators) or ((i < llen -1) and string[i+1] in operators)):
        print("ошибка с операторами в ", i, " позиции: ", string)
        return None
    elif string[i] == "*":
        return calc_1 * calc_2
    elif string[i] == "/":
        if (calc_2 != 0):
            return calc_1 / calc_2
        else:
            print("деление на ноль в: ",string[i+1:])
            return None
    elif string[i] == "-":
        return calc_1 - calc_2
    else:
        return calc_1 + calc_2
    
            

while True:
    ss = input().replace(' ', '')
    if check(ss):
        rez = calc(ss)
        if not rez is None:
            print(rez)
