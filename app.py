import dbconfig
import json
import fastapi

app = fastapi.FastAPI()

@app.get('/crud')
def on_get(cls, req, resp):
    try:
        request = req.media
        id = request.get("id", "")
        if id is not "":
            db = dbconfig.mydb
            cursor = db.cursor()
            query = f"SELECT * FROM customer WHERE id = {id};"
            cursor.execute(query)
            data = cursor.fetchall()
        else:
            db = dbconfig.mydb
            cursor = db.cursor()
            query = f"SELECT * FROM customer;"
            cursor.execute(query)
            data = cursor.fetchall()

        print(type(data))
        json_object = json.dumps(data, indent=4)
    except Exception as es:
        error = es
        json_object = json.dumps(error, indent=4)
    finally:
        resp.text = json_object
        return resp


# class create:
@app.post('/crud')
def on_post(cls, req, resp):
    try:
        request = req.media
        name = request.get("name")
        lname = request.get("surname")
        salary = request.get("salary")
        db = dbconfig.mydb
        cursor = db.cursor()
        query = "INSERT INTO customer(name,surname,salary) VALUES(%s,%s,%s);"
        val = (name, lname, salary)
        cursor.execute(query, val)
        db.commit()
        credentials = {"Success": "Successfully Saved", }
        json_object = json.dumps(credentials, indent=4)
        resp.text = json_object

    except Exception as es:
        error = es
        json_object = json.dumps(error, indent=4)
    finally:
        resp.text = json_object
        return resp