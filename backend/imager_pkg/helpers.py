import yaml
import pymongo

#-Global Vars-------------------------------------


#-------------------------------------------------

def create_mongo_con():
  flObj = open('config.yaml', "r")
  confObj = yaml.load(flObj, Loader=yaml.FullLoader)
  mongoHost = confObj["mongohost"]
  mongoPort = confObj["mongoport"]
  mongoDb = confObj["mongodb"]
  
  try:
    mongoCli = pymongo.MongoClient("mongodb://%s:%s/" %(mongoHost, mongoPort))
    mongoCon = mongoCli[mongoDb]
    return mongoCon
  except Exception as e:
    print(e)
    return False

#-------------------------------------------------
