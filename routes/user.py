from fastapi import APIRouter
from models.user import User
from config.db import connection
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()

@user.get('/')  #decorator
async def find_all_users():
    #print(connection.local.user.find())
    #print(usersEntity(connection.local.user.find()))
    return usersEntity(connection.local.user.find())

@user.get('/{id}') 
async def find_one_user(id):
    return userEntity(connection.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/') 
async def create_users(user: User):
    connection.local.user.insert_one(dict(user))
    return usersEntity(connection.local.user.find())

@user.put('/{id}') 
async def update_users(id,user: User):
    connection.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity(connection.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}') 
async def delete_users(id):
    return userEntity(connection.local.user.find_one_and_delete({"_id":ObjectId(id)}))
