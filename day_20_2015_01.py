def calc_house_no(no_of_gifts, start_with):
    house_no = start_with
    while True:
        gifts = []
        for i in range(1, house_no + 1):
            if house_no % i == 0:
                gifts.append(i*10)
        print gifts
        if sum(gifts) == no_of_gifts:
            return house_no
        house_no += 1

gifts_required = 80
initial_house_no = 1
print "\nHouse no " + str(calc_house_no(gifts_required, initial_house_no)) + \
      " will get " + str(gifts_required) + " gifts."
