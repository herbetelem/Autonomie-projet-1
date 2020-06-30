def intoMyBag(bag, limitBag):
    placeRestant = limitBag - len(bag)
    returned = "vous avez dans votre sac ["
    for index in bag:
        if index == bag[len(bag) - 1]:
            if isinstance(index, list):
                returned = f"{returned} {index[0]}"
            else:    
                returned = f"{returned} {index}"
        else:
            returned = returned + index + "], ["
    returned = f"{returned} ]. Il vous reste {placeRestant} de places dans votre sac"
    print(returned)
