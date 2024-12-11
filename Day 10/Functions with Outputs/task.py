# def format_name(f_name, l_name):
#     output = f"{f_name.title()} {l_name.title()}"
#     return output
#
# print(format_name("carlos", "nascimento"))

def is_leap_year(year):
    leaps = []
    divisible_by_4 = year % 4
    divisible_by_100 = year % 100
    divisible_by_400 = year % 400

    if divisible_by_4 == 0:
        leaps.append("leap")
    else:
        leaps.append("not leap")

    if divisible_by_100 == 0:
        leaps.append("not leap")
    else:
        leaps.append("leap")

    if divisible_by_400 == 0:
        leaps.append("leap")
    else:
        leaps.append("not leap")

    if leaps[0] == "leap" and leaps[2] == "leap":
        return True
    elif leaps[0] == "leap" and leaps[1] == "leap":
        return True
    elif leaps[0] == "not leap" or leaps[2] == "not leap":
        return False

    return leaps


print(is_leap_year(2100))
