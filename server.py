from flask import Flask, request
import json
from datetime import date
import os.path

app = Flask(__name__)


@app.route('/network_test')
def test():

    return 'Connection successful!'

@app.route('/recieve_tutor_request', methods = ['POST'])
def update_file():

    requestData = (str)(request.data.decode('utf-8'))
    data = json.loads(requestData)
    filepath = 'E:/workshop-app-server/tutor_requests/' +data['user'] +'/'

    if(not os.path.isdir(filepath)): 
        os.mkdir(filepath)
    
    request_num = 0

    while True: 
        filename =  str(date.today()) + '-' + str(request_num) + '.txt'

        if (os.path.isfile(filepath + filename)):
            request_num += 1
        else:
            with open(filepath + filename, 'x') as f:
                f.write(requestData)   

            return 'Tutor request recieved!'

@app.route('/login',methods = ['POST'])
def login():
    requestData = (str)(request.data.decode('utf-8'))
    data = json.loads(requestData)

    username = data['username']
    password = data['password']

    response =  {'passwordCheck':True, 'usernameCheck':True}

    return json.dumps(response)
          
@app.route('/event_data/<string:file>')
def get_calendar_data(file):
    requestData = (str)(request.data.decode('utf-8'))

    f = open(file,'r')
    return f.read()
    



if __name__ ==  '__main__':
    app.run(host='localhost', port=5000)


