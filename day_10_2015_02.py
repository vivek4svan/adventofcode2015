def next_password_calculator(old_password):
    new_pass = []
    for i in range(len(old_password)-1,-1,-1):
        if old_password[i] == "z":
            new_pass.append("a")
            continue
        else:
            new_pass.append(chr(ord(old_password[i])+1))
            pos = i
            break
    for i in range(i-1,-1,-1):
        new_pass.append(old_password[i])
    new_pass.reverse()
    return "".join(new_pass)


def pass_test1(password):
    return not ("i" or "o" or "l") in password


def pass_test2(password):
    partitions = [password[i:i+2] for i in range(len(password))]
    print partitions
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
    to_ordinal = lambda x: map(ord, x)
    increasing = lambda x: x[0] == (x[1] - 1) == (x[2] - 2)
    partitions = [password[i:i+3] for i in range(len(password)-2)]
    ordinals = [to_ordinal(i) for i in partitions]
    test = [increasing(i) for i in ordinals]
    return any(test)


input_val = "abcdefgd"
password_ok = 0
while password_ok != 1:
    new_pass = next_password_calculator(input_val)
    print new_pass
    print pass_test1(new_pass)
    print pass_test3(new_pass)
    print pass_test2(new_pass)
    password_ok = 1
