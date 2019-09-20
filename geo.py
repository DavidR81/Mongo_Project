#Sacar columnas longitud y latitud

def createGeoJson(longitude,latitude):
    return {
        "type":"Point",
        "coordinates":[longitude,latitude]
    }


