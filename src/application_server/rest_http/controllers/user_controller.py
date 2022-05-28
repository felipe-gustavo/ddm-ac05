from ..app import app

ROUTE_PREFIX = "/users"


@app.route(f'{ROUTE_PREFIX}/', methods=["GET"])
def getUsers():
    user = {"name": "Felipe", "age": 22}
    return {"data": [user, user]}
