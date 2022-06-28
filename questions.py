def hello_name(user_name):
    print(f"hello_{user_name}!")



def first_odds():
    num = list(range(1,100))
    odd = num[0::2]
    print(odd)
    return "nothing"



def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num





def is_a_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f"{a_year} is a leap year")
    elif a_year % 400 == 0:
        print(f"{a_year} is a leapa year")
    else:
        a_year = False
        print(f"{a_year}")



def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
        print(status)



