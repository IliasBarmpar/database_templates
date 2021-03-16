import pymongo

""" Create Database """
# In MongoDB, a database is not created until it gets content (create collection and create document)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

" Check if Database exists"
# print(myclient.list_database_names())
#
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#   print("The database exists.")


""" #Insert Into Collection """
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)


" Return the ID field "
# mydict = { "name": "Peter", "address": "Lowstreet 27" }
# x = mycol.insert_one(mydict)
# print(x.inserted_id)
#
# " Insert Multiple Documents "
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

" Insert Multiple Documents, with Specified IDs "
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

""" Find """
" Find One "
# x = mycol.find_one()
# print(x)

" Find All "
# [ print(x) for x in mycol.find()]

" Return Only Some Fields "
# [print(x) for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 })]
# [print(x) for x in mycol.find({},{ "address": 0 })]
# [ print(x) for x in mycol.find({},{ "name": 1, "address": 0 }) ] # This produces error because you have both 0 and 1


""" Query """
# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# [print(x) for x in mydoc]

" Advanced Query "
# myquery = { "address": { "$gt": "S" } }
# mydoc = mycol.find(myquery)
# [print(x) for x in mydoc]

" Filter With Regular Expressions "
# myquery = { "address": { "$regex": "^S" } }
# mydoc = mycol.find(myquery)
# [print(x) for x in mydoc]

""" Sort """
# mydoc = mycol.find().sort("name")
# [print(x) for x in mydoc]

" Sort Descending "
# mydoc = mycol.find().sort("name", -1)
# [print(x) for x in mydoc]


""" Delete """
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)

" Delete Many Documents "
# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")

" Delete All Documents in a Collection"
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")


""" Drop Collection """
# mycol.drop()


""" Update Collection """
" Update One "
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
# [print(x) for x in mycol.find()]

" Update Many "
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")


""" Limit """
# myresult = mycol.find().limit(5)
# [print(x) for x in myresult]
