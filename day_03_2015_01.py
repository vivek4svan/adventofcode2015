f = open("input_santa_orig.txt", "r")

h_move = 0
v_move = 0
ctr = 1

gift_given = {(0,0):1}

for i in f.read():
    if(i == "<"):
        h_move -= 1
        gift_given[(h_move,v_move)] = 1
    elif(i == ">"):
        h_move += 1
        gift_given[(h_move,v_move)] = 1
    elif(i == "^"):
        v_move += 1
        gift_given[(h_move,v_move)] = 1
    elif(i == "v"):
        v_move -= 1
        gift_given[(h_move,v_move)] = 1
f.close()

#print gift_given
print len(gift_given.keys())