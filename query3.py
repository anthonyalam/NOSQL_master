import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient( "mongodb+srv://isaac:alpesco22@cluster0.x48qi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    con = db.continents
    #     #  / Send back the fourth countries of a continent by alphabetic order
    continents = con.find({},{'Name':1, 'countries':{'$slice':4}}).sort("Name")
    for FourCountry in continents:
        print(FourCountry)


if __name__ == '__main__':
        connectdb()