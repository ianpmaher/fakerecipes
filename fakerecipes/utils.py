from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ianpmaher:fL4Xvqy2Z4RkjVHu@cluster0.2rxzajw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
'''
mongodb+srv://ianpmaher:<password>@cluster0.2rxzajw.mongodb.net/
'''

def GetBody(request):
    # get the body of the request
    # body = request.body
    # # decode the body to a string
    # decoded_body = body.decode('utf-8')
    # turn the string into a dictionary
    return MongoClient(request.body)

def get_mongo_client():
    connection_string = uri
    return MongoClient(connection_string)