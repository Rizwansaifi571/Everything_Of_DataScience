from flask import Flask, jsonify, request

# jsonify create json response from python data Structure like dic or list.
app = Flask(__name__)

## initial data in my to do list
items = [
    {'id': 1, 'name': 'item1', 'description': 'This is item 1'}, 
    {'id': 2, 'name': 'item2', 'description': 'This is item 2'}
]

@app.route('/')
def home():
    return "Welcome to The sample TO DO List App"

## get: Retrieve all the items
@app.route('/items', methods = ['GET'])
def g_items():
    return jsonify(items)

## get: Retrieve specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    found = None
    for item in items:
        if item['id'] == item_id:
            found = item
            break
    if found is None:
        return jsonify({"error": "Item not found"})
    return jsonify(found)
    
## Post : Create a new task
@app.route('/items', methods = ['POST'])
def create_item():
    if not request.json or 'name'not in request.json:
        return jsonify({"error": "Invalid request"})
    new_item = {
        'id' : items[-1]['id'] + 1 if items else 1, 
        'name' : request.json['name'], 
        'description' : request.json.get('description', "")

    }
    items.append(new_item)
    return jsonify(new_item)


## Put : Update an existing item
@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error" : "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

## Delete : Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    new_items = []
    deleted = False
    for item in items:
        if item['id'] != item_id:
            new_items.append(item)
        else:
            deleted = True
    items = new_items
    if deleted:
        return jsonify({"result": "Item deleted"})
    else:
        return jsonify({"error": "Item not found"})


if(__name__ == "__main__"):
    app.run(debug = True)