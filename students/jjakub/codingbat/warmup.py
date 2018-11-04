def sleep_in(weekday, vacation):
    if weekday == True and vacation == False:
        return False
    else:
        return True
    
# print(sleep_in(False, True))

def sleep_in02(weekday, vacation):
    return not (weekday == True and vacation == False)
# print(sleep_in02(False, True))

def sleep_in03(weekday,vacation):
    return (not weekday) or vacation
print(sleep_in03(False, True))