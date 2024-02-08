'''
-----------------A html file for calculator------------------------

<!DOCTYPE html>
<html>
    <head>
        <title>calculator</title>
        
    </head>
    <div class="content">
     <div class="form">
            <form action="/math" method="POST">
                <label for="operation">Choose a Methematical Operation</label>
                <select id="operation" name="operation">
                    <option value="add">add</option>
                    <option value="subtract">subtract</option>
                    <option value="multiply">multiply</option>
                    <option value="divide">divide</option>
                </select>
                         <input type="text" name="num1" id="num1">
                         <input type="text" name="num2" id="num2">
                         <input type="submit" value="Calculator">                
            </form>
        </div>
    </div>
   
    </html>


----------------below code is for API for calculator----------------
'''

#Importing Flask and necessary modules
from flask import Flask ,request,render_template
#Creating a Flask application instance
app = Flask(__name__)
#Defining a route for the calculator page
@app.route('/')
def cal_page():
    return render_template('calculator.html')

#efining a route for handling calculator operations:
@app.route('/math',methods=['POST'])
def calculator_test():
    #Performing calculations based on the selected operation
    ops =request.form['operation']
    first_num=int(request.form['num1'])
    second_num =int(request.form['num2'])


    #Handling different operations (addition, subtraction, multiplication, division):
    if(ops=='add'):
        r= first_num + second_num
        return f"addition of {first_num} and {second_num} is{r}"
    
    if(ops=='subtract'):
        r= first_num - second_num
        return f"subtraction of {first_num} and {second_num} is{r}"
    
    if(ops=='multiply'):
        r= first_num * second_num
        return f"multiply of {first_num} and {second_num} is{r}"
    
    if(ops=='divide'):
        r= first_num / second_num
        return f"divide of {first_num} and {second_num} is{r}"

#Running the Flask application
if __name__ =="__main__":
    app.run(host="0.0.0.0")