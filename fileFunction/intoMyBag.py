def intoMyBag(bag, limitBag):
    placeRestant = limitBag - len(bag)
    returned = "vous avez dans votre sac ["
    for index in bag:
        if index == bag[len(bag) - 1]:
            returned = returned + index + "] "
        else:
            returned = returned + index + ", "
    returned = returned + ". Il vous reste " + str(placeRestant) + " de places dans votre sac"
    print(returned)
