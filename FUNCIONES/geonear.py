#Sacar el geopoint

def geonear(geopoint, maxdistance=1000):
   return db.limpiado.find({
       "position":{
           "$near":{
               "$geometry":geopoint,
               "$maxDistance":maxdistance
           }}})