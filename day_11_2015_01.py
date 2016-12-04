def next_password_calculator(old_password):
    new_password = []
    new_flag = 0
    got_next = 0
    i = len(old_password) - 1
    while new_flag == 0:
        while got_next != 1 and i >= 0:
            if old_password[i] != 'z':
                new_password.append(chr(ord(old_password[i]) + 1))
                got_next = 1
            else:
                new_password.append("a")
                i -= 1
        new_flag = 1
    for remaining in range(i - 1, -1, -1):
        new_password.append(old_password[remaining])
    new_password.reverse()
    return "".join(new_password)


def pass_test1(password):
    return not ("i" or "o" or "l") in password


def pass_test2(password):
    pair = 0
    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            i += 2
            pair += 1
        else:
            i += 1
    if pair >= 2:
        return True
    else:
        return False


def pass_test3(password):
    i = 0
    while i < len(password) - 2:
        if ord(password[i]) == ord(password[i + 1]) - 1 and ord(password[i + 1]) == ord(password[i + 2]) - 1:
            print password[i] + password[i + 1] + password[i+2]
            return True
        else:
            i += 1
    return False


input_val = "vzbxxyzz"
password_ok = 0
while password_ok != 1:
    new_pass = next_password_calculator(input_val)
    print new_pass
    if pass_test1(new_pass) and pass_test2(new_pass) and pass_test3(new_pass):
        print "New Password Should be : " + new_pass
        password_ok = 1
    else:
        input_val = new_pass
