import connectdb as connectdb
import pymongo as pymongo


def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def connectDB():
    client = pymongo.MongoClient( "mongodb+srv://isaac:alpesco22@cluster0.x48qi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db = client.test
    col = db.countries
    con = db.continents

    #  Send the list of continent with there number of countries
    def continents():
        agg_pipeline = [
            {
                '$project': {
                    'name': "$name",
                    'countries': {'$size': "$countries"}}
            }
        ]
        cont = con.aggregate(agg_pipeline)
        for continent in cont:
            print(continent)

    continents()


if __name__ == '__main__':
    connectdb()