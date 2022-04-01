from flask import Flask, jsonify, request 

app = Flask(__name__)

data= [
        {
            'Contact': "9988776655",
            'Name': 'Raju',
            'done': False,
            'id': 1
        },
        {
            'Contact': "1111111112",
            'Name': 'Rahul',
            'done': False,
            'id': 2
        }
    ]


@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data! "
        },400)
    else:
     contact = {
        'id': request.json['id'],
        'Name': request.json['Name'],
        'Contact': request.json.get['Contact', ""],
        'done': False
        }

     data.append(contact)
     return jsonify({
        "status": "success",
        "message": "Data added successfully! "
     })

@app.route("/get-data")
def get_data():
    return jsonify({
        'data': data
    })


if __name__ == "__main__":
    app.run(debug= True)