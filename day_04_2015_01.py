import hashlib
i = 0
while True:
    i += 1
    test_val = 'ckczppom' + str(i)
    hash_data = hashlib.md5(test_val).hexdigest()
    #if hash_data[:5] == '00000':
    if hash_data[:6] == '000000':
        print 'Hurrah Got It... ' + str(i)
        break