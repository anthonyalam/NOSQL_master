import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient( "mongodb+srv://isaac:alpesco22@cluster0.x48qi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents

    # 6/ Get all the countries order by number of people first the less populated and last the most populated
    def orderbypopulation():
        for countries in col.find({}).sort("Population"):
            print(countries['Name'], countries['Population'])
    orderbypopulation()

if __name__ == '__main__':
    connectdb()