from pprint import pprint
from fastapi import APIRouter,Request,Body,Response,status
from typing import List
from crud import items,Updatelist_item
from fastapi.encoders import jsonable_encoder

router = APIRouter()

#Read to-do-list
@router.get("/")
def read_list(request: Request):

    db_users = request.app.db['users'].find()
    print(type(db_users))
    pprint(pprint (db_users))
    users = []
    for _user in db_users:
        users.append({
            "name": _user.get("name")
        })

    return {"items": list(users)}

#Add to-do-list
@router.post("/")
def add_list(request:Request,item: items = Body(...)):
    item = jsonable_encoder(item)
    new_item = request.app.users.find()
    print(new_item)
    # create_list = request.app.database["Entries"].find_one(
    #     {
    #         "id":new_item.inserted_id
    #     }
    # )
    return "create_list"


#Update to-do-list
@router.put("/",response_model=Updatelist_item )
def update_list(request:Request,item: Updatelist_item = Body(...)):
    item = {i:j for i,j in item.dict().items if j is not None}
    if len(item)<=1:
        update_list_result = request.app.database["Entries"].update_one(
            {"_id":id},{"$set":item}
        )
        if update_list_result.modified_count == 0:
            return "List is not found"

        exit_list = request.app.database["users"].find_one(
            {"_id":id}
        )
        return exit_list
    return "List not found"

#Delete to-do-list
@router.delete("/")
def delete_list(request:Request,response:Response):
    delete_result = request.app.database["Entries"].delete_one(
        {"_id":id}
    )
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    return "List not found"