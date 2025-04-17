from flask import Flask, jsonify, request

app = Flask(__name__)

#Temporary list of todos 
todos = [
    {"id": 1, "task": "Make dinner", "done": False},
    {"id": 2, "task": "Clean the house", "done": True}
]

@app.route('/')
def home():
    return "Welcome!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST request to add new todo
@app.route('/todo', methods = ['POST'])
def create_todo():
    #Get the data from the request
    data = request.get_json()

    # Create a new todo item
    new_todo = {
        "id": len(todos) + 1,
        "task": data['task'],
        "done": data.get('done', False)
    }

    todos.append(new_todo)
    return jsonify(new_todo), 201 # Return the new todo item with status 201 (Created)


if __name__ == '__main__':
    app.run(debug=True)
