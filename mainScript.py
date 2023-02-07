import pymongo
import os
import json
from dotenv import load_dotenv

load_dotenv()

password = os.getenv('MONGODB_PASSWORD')
clusterName = os.getenv('MONGO_DB')
db_Name = os.getenv("DB_NAME")
collectionName = os.getenv("COLLECTION_NAME")

client = pymongo.MongoClient("mongodb+srv://marc:" + password + "@" + clusterName + ".caingxo.mongodb.net/?retryWrites=true&w=majority")
db = client[db_Name]
activities = db[collectionName]

folder = "jsons"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    if os.path.isfile(file_path):
        with open(file_path) as file:
            # Do something with the file
            content = file.read()
            data = json.loads(content)
            print(f"File: {filename}")

            for obj in data:
               post_id = activities.insert_one(obj).inserted_id
               print("Inserted post with ID:", str(post_id))
            #print(f"Content: {data}")
            #break
