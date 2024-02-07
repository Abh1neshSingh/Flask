from flask import Flask ,request
app =Flask(__name__)

@app.route('/add')
def addition():
    return f"this is my test fun"
@app.route('/abhi')
def print_name():
    return f"Abhinesh singh"
@app.route('/singh')
def hellosir():
    return f"hey i am here"
   

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5003)