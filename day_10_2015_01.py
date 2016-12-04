def cal_elves_say(input_str,no_of_times):
    final_say = input_str
    for i in range(no_of_times):
        input_str = final_say
        length = len(input_str)
        elves_say = []
        ctr = 0
        for i in range(len(input_str)-1):
            ctr += 1
            if input_str[i] != input_str[i+1]:
                elves_say.append(str(ctr))
                elves_say.append(input_str[i])
                ctr = 0
        if input_str[length-1] == input_str[length-2]:
            ctr += 1
            elves_say.append(str(ctr))
            elves_say.append(input_str[length-1])
        else:
            elves_say.append(str(1))
            elves_say.append(input_str[length-1])
        final_say = "".join(elves_say)
        print final_say
        print len(elves_say)

cal_elves_say("1113222113",50)

