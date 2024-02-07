from flask import Flask ,request
app =Flask(__name__)

@app.route('/user')
def print_user():
    data=request.args.get('name') # to take user input by url
    return f"{data}"

# to take a user input by url like we write ----?name=Abhineshsingh
# full url is given below for access it
#http://localhost:5006/user?name=AbhineshSingh

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5006)