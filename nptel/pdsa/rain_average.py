def rainaverage(l):
    rain_dict = dict()
    for pair in l:
        city, rain = pair
        tup  = rain_dict.get(city, (0, 0))
        rain_dict[city] = (tup[0]+rain, tup[1]+1)
    ret = list()
    for city in rain_dict:
        ret.append( (city, rain_dict[city][0]/rain_dict[city][1]) )
    return ret
        
