from fastapi import APIRouter,Request
from bson.json_util import dumps

router = APIRouter()

#add to-do-list(Create)
@router.post("/")
def add_list(request:Request):
    entry = {
        "new_item":"Hero1"
    }
    inserted_id = request.app.db["Item"].insert_one(entry).inserted_id
    print(inserted_id)
    latest_entry = list(request.app.db['Item'].find_one({"new_item":"Hero1"}))
    print(type(latest_entry))
    print("============================")
    json_latest_entry = dumps(latest_entry)
    print(json_latest_entry)
    return latest_entry

# #Read to-do-list(Read)
@router.get("/")
def read_list(request: Request):
    db_users = list(request.app.db['Item'].find()) #convert cursor object to list
    print("======")
    print(db_users)
    json_data = dumps(db_users) #converting list_cursor object to the JSON
    return json_data

#Update to-do-list(Update)
@router.put("/")
def update_list(request:Request):
    to_find_item_to_update = request.app.db['Item'].find_one({"new_item":"Done456"})
    print(type(to_find_item_to_update))
    print("============")
    if to_find_item_to_update:
        print("+++++")
        updated_item = request.app.db['Item'].update_one(
               {"new_item":"Done456"},{"$set":{"new_item":"Done4567"}}
        )
        return updated_item.modified_count

#Delete to-do-list
@router.delete("/")
def delete_item(request:Request):
    find_item = request.app.db['Item'].find_one({"ObjectId":"two"})
    print(type(find_item))
    delete_one_item = request.app.db['Item'].delete_one({"ObjectId":"two"})
    return delete_one_item.deleted_count
