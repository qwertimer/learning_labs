from fastapi import FastAPI

app = FastAPI()

#Minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return{"Ping":"Pong"}

# Get --> read ToDo

@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return{"data": todos}


#Post  --> Create ToDo
@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) ->dict:
    todos.append(todo)
    return{"data": " Todo has been added"}

#Put  --> Update Todo
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todos['Activity'] = body['Activity']
            return{
                "data":f"Todo with id {id} has been updated"
            }
    return {
        "data":f"Todo with id {id} was not found"
    }
#Delete --> delete



todos = [

    {"id": "1",
    "Activity": "Run"},
    {"id": "2",
    "Activity": "Stop"},
    
]