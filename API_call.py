from flask import Flask, request, jsonify#import Flask
import requests

app = Flask(__name__) #creating flask app

#personal_data = {1: {'name': 'Omkar Gawade', 'gender':'female'}, 2:{'name': 'Rutuja', 'gender': 'female'}}

personal_data = {
                1:{'name':'Omkar Gawade', 'gender':'Male'}, 
                2:{'name':'Rutuja Dukhande', 'gender':'Female'},
                3:{'name':'Sam Dukhande', 'gender':'Female'},
                 }


@app.route('/', methods = ['GET']) #creating first endpoint
def main_page():
    return personal_data[1]['name']


@app.route('/<int:num>', methods=['GET'])
def user_page(num):
    for key, value in personal_data.items():
        if key == num:
            return value
    return 'wrong data1'

@app.route('/<string:name>', methods = ['GET']) #creating first endpoint
def user_page1(name):
    for user_id, user_data in personal_data.items():
        if user_data['name'] == name:
            return user_data
    return 'wrong data'

@app.route('/updateRecord') #creating first endpoint
def updateRecord():
    key = int(request.args.get('key'))
    name = request.args.get('name')
    subname = request.args.get('subname')
    if key in personal_data:
        if name in personal_data[key]:
                personal_data[key][name] = subname  
    return jsonify(personal_data)


    #return personal_data[key][value] == subvalue

if __name__ == '__main__':
    app.run(debug=True)