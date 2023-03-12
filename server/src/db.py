from imports import *

class Db:

    def add(request, file_id):
        db_file = "../db/db.json"
        client_id = request['client_id']
        key = request['key']
        data = request['data']
        path = f"../db/{client_id}/{file_id}"
        file_json = {
            "file_path": path,
            "key": key
        }

        with open(db_file, "r") as db:
            db_json = json.loads(db.read())
        try:
            db_json["clients"][client_id][file_id] = file_json
        except:
            db_json["clients"][client_id] = {}
            db_json["clients"][client_id][file_id] = file_json

        with open(db_file, "w") as db:
            db.write(json.dumps(db_json))

        try:
            with open(path, "wb") as file:
                file.write(base64.b64decode(data))
        except:
            os.mkdir(f"../db/{client_id}")

        with open(path, "wb") as file:
            file.write(base64.b64decode(data))

    def find(request):
        db_file = "../db/db.json"
        client_id = request["client_id"]
        key = request["key"]
        file_id = request["file_id"]
        path = ""

        with open(db_file, "r") as db:
            db_json = json.loads(db.read())

        if client_id in db_json["clients"]:
            if file_id in db_json["clients"][client_id]:
                if db_json["clients"][client_id][file_id]["key"] == key:
                    path = db_json["clients"][client_id][file_id]["file_path"]
                else:
                    return {"error": "bad key"}
            else:
                return {"error": "file don't exist"}
        else:
            return {"error": "client d'ont exist"}

        with open(path, "rb") as data:
            return {"data": base64.b64encode(data.read()).decode()}