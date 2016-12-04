f = open("input_santa_orig.txt", "r")

h_move_santa = 0
v_move_santa = 0
v_move_robo = 0
h_move_robo = 0
ctr = 0
gift_given = {(0,0):1}

for i in f.read():
    if ctr%2 == 0:
        if(i == "<"):
            h_move_santa -= 1
            gift_given[(h_move_santa,v_move_santa)] = 1
        elif(i == ">"):
            h_move_santa += 1
            gift_given[(h_move_santa,v_move_santa)] = 1
        elif(i == "^"):
            v_move_santa += 1
            gift_given[(h_move_santa,v_move_santa)] = 1
        elif(i == "v"):
            v_move_santa -= 1
            gift_given[(h_move_santa,v_move_santa)] = 1
    else:
        if (i == "<"):
            h_move_robo -= 1
            gift_given[(h_move_robo, v_move_robo)] = 1
        elif (i == ">"):
            h_move_robo += 1
            gift_given[(h_move_robo, v_move_robo)] = 1
        elif (i == "^"):
            v_move_robo += 1
            gift_given[(h_move_robo, v_move_robo)] = 1
        elif (i == "v"):
            v_move_robo -= 1
            gift_given[(h_move_robo, v_move_robo)] = 1
    ctr += 1
f.close()

#print gift_given
print len(gift_given.keys())