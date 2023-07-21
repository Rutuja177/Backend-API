from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__) #creating flask app
CORS(app)

personal_data = {}
with open("data.txt", "r") as e:
    personal_data_read = e.read()

personal_data = eval(personal_data_read)


#endpoint to get all user data
@app.route('/users', methods = ['GET'])
def main_data():
    return personal_data

#endpoint to get data based on key or name
@app.route('/users/<string:id>', methods=['GET']) 
def getUserByKey(id):
    for key, value in personal_data.items():
        if id == key:
            return jsonify(value)
        elif id == value['name']:
            return jsonify(value)
        else:
            return 'Wrong user data entered.'

#endpoint to create a new user data
@app.route('/create', methods = ['POST']) 
def createRecord():
    data = request.json
    
    def generateNewid():
        sample_string = ""
        for i in range(5):
            sample_string += "".join(random.choice(string.ascii_lowercase))
        return sample_string
    
    new_id = generateNewid()
    
    for key, items in personal_data.items():
        if data['name'] in personal_data[key]['name']:
            return "The data is already is existed"
    personal_data[new_id] = {'name': data['name'], 'gender': data['gender']}
    return jsonify({'message': 'Person added successfully'}, personal_data[new_id])
    
   
#endpoint to update the data 
@app.route('/users/update', methods = ['POST', 'GET'])
def updateRecord():
    
    jsonData = request.get_json()
    key = jsonData['key']
    password = int(jsonData['password'])
    value = jsonData['value']
    if key in personal_data:
                #return jsonify(password, personal_data[key]['gender'])
                if password % 2 == 0 and personal_data[key]['gender'] == "Female":
                    personal_data[key]['name'] = value 
                    return "done"
                elif password % 2 != 0 and personal_data[key]['gender'] == "Male":
                    personal_data[key]['name'] = value 
                    return "done"
                else:
                    return "Invalid"
            
    
    return jsonify(key, value,password)

@app.route('/users/delete', methods = ['POST'])
def deleteRecord():
    jsonData = request.get_json()
    key = jsonData['key']
    if key in personal_data:
        del personal_data[key]
        return "Deleted"


    
if __name__ == '__main__':
    app.run(debug=True)