import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://isaac:alpesco22@cluster0.x48qi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents
    # 7/ Get countrieswhich have a ‘u’ in their name and more 100 000 people inside
    def query7():
        for continents in col.find({
                    'Name':
                        {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
                }
        ).sort("population"):
            print( continents['Name'], continents['Population'])
    query7()

if __name__ == '__main__':
    connectdb()
