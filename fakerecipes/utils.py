from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# import dotenv
# import os
from dotenv import load_dotenv
import os

load_dotenv()

# get the URI from the environment
uri = os.getenv('MONGO_URI')

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# def GetBody(request):
#     # get the body of the request
#     # body = request.body
#     # # decode the body to a string
#     # decoded_body = body.decode('utf-8')
#     # turn the string into a dictionary
#     return MongoClient(request.body)

# def get_mongo_client():
#     connection_string = uri
#     return MongoClient(connection_string)