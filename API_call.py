from flask import Flask, request, jsonify #import Flask
from flask_cors import CORS
import random
import string

app = Flask(__name__) #creating flask app
CORS(app)

# personal_data = {
#                 1:{'name':'Omkar Gawade', 'gender':'Male'}, 
#                 2:{'name':'Rutuja Dukhande', 'gender':'Female'},
#                 3:{'name':'Sam Dukhande', 'gender':'Female'},
#                  }
personal_data = {}
with open("C:/Users/Rutuja/Desktop/Projects/myReactApp/Backend-API/data.txt", "r") as e:
    personal_data_read = e.read()

personal_data = eval(personal_data_read)

print(personal_data)

    
@app.route('/', methods = ['GET']) #creating main endpoint
def main_page():
    return personal_data


@app.route('/<string:num>', methods=['GET']) #endpoint to view data based on key #Read
def user_page(num):
    for key, value in personal_data.items():
        if key == num:
            return value
    return 'wrong id entered.'

@app.route('/<string:name>', methods = ['GET']) #endpoint to view data based on 'name' #Read
def user_page1(name):
    for key, value in personal_data.items():
        if value['name'] == name:
            return jsonify(value)
    return 'wrong name entered.'

@app.route('/create', methods = ['POST']) #endpoint to creating new record  #Create
def createRecord():
    data = request.json
    #new_id = max(personal_data.keys()) +1
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
    
    #return jsonify(new_record), 201

@app.route('/updateRecord', methods = ['POST', 'GET']) #endpoint to update the data 
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
            
    
    #return jsonify(key, value, subvalue,password)

@app.route('/delete', methods = ['POST'])
def deleteRecord():
    jsonData = request.get_json()
    key = jsonData['key']
    if key in personal_data:
        del personal_data[key]
        return "Deleted"


    
if __name__ == '__main__':
    app.run(debug=True)