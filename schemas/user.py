def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "password":item["password"],
        "city":item["city"],
        "pincode":int(item["pincode"]),
        "mobile_no":int(item["mobile_no"])
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]