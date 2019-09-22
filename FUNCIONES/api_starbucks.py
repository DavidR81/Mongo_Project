
#sacamos las posiciones de los starbucks cercanos

def starbucks(dictrandom):
   names=[]
   lats=[]
   long=[]
   for place in dictrandom["results"]:
       names.append(place["name"])
       lats.append(place["geometry"]["location"]["lat"])
       long.append(place["geometry"]["location"]["lng"])
   dictstarbucks = {"name":names, "latitude":lats, "longitude":long}
   return pd.DataFrame(dictstarbucks)
datastarbucks = starbucks(sb)
datastarbucks.head()