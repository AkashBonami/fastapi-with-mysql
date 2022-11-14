from fastapi import FastAPI
import dbconfig
import uvicorn
import schemas



app = FastAPI()
@app.get('/crud')
def get(id):
    try:
        db = dbconfig.mydb
        cursor = db.cursor()
        query = f"SELECT * FROM users WHERE id = {id};"
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except Exception as error:
        return error
        
@app.post("/crud")
def post(request : schemas.User):
    try:
        name = request.name
        lname = request.lname
        salary = request.salary
        db = dbconfig.mydb
        cursor = db.cursor()
        query = "INSERT INTO users(name,surname,salary) VALUES(%s,%s,%s);"
        val = (name, lname, salary)
        cursor.execute(query, val)
        db.commit()
        credentials = {"Success": "Successfully Saved", }
        return credentials
    except Exception as es:
        error = es
        return error


@app.put("/crud")
def put(request : schemas.User):
    try:
        id = request.id
        name = request.name
        lname = request.lname
        salary = request.salary
        db = dbconfig.mydb
        cursor = db.cursor()
        query = "UPDATE users SET name = %s , surname = %s , salary = %s WHERE id = %s;"
        val = (name,lname,salary,id)
        cursor.execute(query, val)
        db.commit()
        credentials = {"Success": "Successfully Updated", }
        return credentials
    except Exception as error:
        return error


@app.delete("/crud")
def delete(id):
    try:
        id = id
        db = dbconfig.mydb
        cursor = db.cursor()
        query = f"DELETE FROM users WHERE id = {id};"
        cursor.execute(query)
        db.commit()
        credentials = {"Success": "Successfully Deleted", }
        return credentials
    except Exception as error:
        return error



if __name__ == "__main__":
    uvicorn.run(app, port=8001, host='127.0.0.1')
