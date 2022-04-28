from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "helloWorld"

contacts = [{
    "id": 1,
    "name": "siddharth",
    "contact": "9055896589",
    "done":False
},
{
    "id": 2,
    "name": "Dev",
    "contact": "8204568997",
    "done":False
}]

@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        })
    contact = {
        "id":contacts[-1]["id"]+1,
        'title': request.json['name'], 
        'description': request.json.get('contact', ""), 
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data":contacts
    })

if(__name__=="__main__"):
    app.run(debug=True)