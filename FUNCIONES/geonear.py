import pandas as pd
from pymongo import MongoClient
import re
import numpy as np

#Sacar el geopoint

def geonear(geopoint, maxdistance=1000):
   return db.limpiado.find({
       "position":{
           "$near":{
               "$geometry":geopoint,
               "$maxDistance":maxdistance
           }}})