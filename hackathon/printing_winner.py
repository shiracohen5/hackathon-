players_and_points={
    "shira":20,
    "ronny":25,
    "sarit":10,
    "matan":40,
    "gal":15
}

time_in_loop=0
while len(players_and_points.values()) > 0:
    list_votes=players_and_points.values()
    max_points=max(list_votes)
    max_key = max(players_and_points, key=players_and_points.get)
    if time_in_loop==0:
        print("The Winner is:",max_key, "with a total of:",max_points,"points!")
        players_and_points.pop(max_key)
    else:
        print(max_key,max_points)
        players_and_points.pop(max_key)
    time_in_loop+=1

new_players_and_points= {
    "shira":20,
    "ronny":25,
    "sarit":10,
    "matan":40,
    "gal":15
}

PRIZES={
    "get 20% off your next aroma":20,
    "'save the planet' bracelet":10,
    "picture of a turtle":10,
    "free small drink in Rebar":25,
    "green globe shirt":15,
    "beach towel":30,
    "1+1 to the movies":50,
    "get 10% in Zara":45,
    "ocean jewelry set":60,
    "free ticket to Bruno Mars":120
}

what_can_buy=[]
names=new_players_and_points.keys()
for name in names:
    num_points_player = int(new_players_and_points.get(name))
    keys=list(PRIZES.keys())
    for j in range (len(PRIZES)):
        curr_value=int(PRIZES.get(keys[j]))
        if curr_value<=num_points_player:
            if keys[j] not in what_can_buy:
                what_can_buy.append(keys[j])
    print(name,"you can buy:",what_can_buy)
    what_can_buy.clear()
