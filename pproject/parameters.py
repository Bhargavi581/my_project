from fastapi import FastAPI

app=FastAPI()

items=[{"item_name":"Apple"},{"item_name":"orange"},{"item_name:grapes"}]
@app.get("/items/")
def root():
    return(items)

