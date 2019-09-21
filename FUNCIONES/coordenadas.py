#Funcion para calcular la longitud

def get_lon(x): 
    try: 
        return float(x['offices'][0]['longitude'])
    except: 
        return None

#funcion para calcular la latitud

def get_lat(x): 
    try: 
        return float(x['offices'][0]['latitude'])
    except: 
        return None

