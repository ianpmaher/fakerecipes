
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import dns

uri = "mongodb+srv://ianpmaher:SealPup401@cluster0.2rxzajw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri)
db = client.fakerecipes

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)