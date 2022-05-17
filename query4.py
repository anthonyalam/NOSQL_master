import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient( "mongodb+srv://isaac:alpesco22@cluster0.x48qi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db.countries
    con = db.continents
    #     #     5/ Add new attributes inside countries which is number of people (find it on wikipedia)
    col.update_one({'Name': 'USA'}, {'$set': {'Population': 332915073}})
    col.update_one({'Name': 'Australia'}, {'$set': {'Population':25987867}})
    col.update_one({'Name': 'Sweden'}, {'$set': {'Population': 10203324}})
    col.update_one({'Name': 'Morocco'}, {'$set': {'Population': 37632126}})
    col.update_one({'Name': 'India'}, {'$set': {'Population': 1402420930}})
    col.update_one({'Name': 'china'}, {'$set': {'Population': 14485086609}})
    col.update_one({'Name': 'France'}, {'$set': {'Population': 65512203 }})
    col.update_one({'Name': 'Germany'}, {'$set': {'Population': 84225935 }})
    col.update_one({'Name': 'Nigeria'}, {'$set': {'Population': 214545286 }})
    col.update_one({'Name': 'Canada'}, {'$set': {'Population': 38288018}})





if __name__ == '__main__':
    connectdb()
