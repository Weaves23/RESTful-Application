
import json
from bson import json_util
from pymongo import MongoClient
import bottle
from bottle import route, run, request, abort

connection=MongoClient('localhost',27017)
db=connection['sample']
collection=db['data']

def Use_RESTful():

  user_select="y"
  while(user_select!="e"):
    
      user_select=input("Type 'c' to create\n 'r' to read\n 'u' to update\n or 'd' to delete\n")
    
      if(user_select == "c"):
        key = input("enter key\n")
        val = input("enter value\n")
        document={key:val}
        collection.insert_one(document)
      
      elif(user_select == "r"):
        key = input("enter key\n")
        val = input("enter value\n")
        document={key:val}
        print(collection.find_one(document))
      
      elif(user_select == "u"):
        old_key = input("enter key\n")
        old_val = input("enter value\n")
 	new_key = input("enter key\n")
        new_val = input("enter value\n")
        old_document={old_key:old_val}
	new_document={"$set":{new_key:new_val}}
        collection.update_one(old_document, new_document)
      
      elif(user_select == "d"):
        key = input("enter key\n")
        val = input("enter value\n")
        document={key:val}
        collection.delete_one(document)
      
      else:
        print("invalid input\n")


if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080, debug=True)