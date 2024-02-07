'''
---------------------------It is a html file---------------------------------------------------
<!DOCTYPE html>
<html>
    <head>
        <title>form Examples</title>
    </head>
    <body>
        <h1>Sumbit a Form</h1>
        <form action="/check_password" method="post">
            <label for="Username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>

            <input type="submit" value="Sumbit">

        </form>
    </body>
</html>

---------------------------It is form for below API-------------------------------------------
'''

from flask import Flask ,request,jsonify ,render_template
app = Flask(__name__)

# first we create a funcation for access  to html or ui page 
#  by using -----> render_template
# it is a function  present in the flask by which you will able to show case html file
@app.route("/")
def show_form():
    return render_template('index.html')


# Define a Flask route for handling POST requests to "/check_password"
@app.route("/check_password",methods=['POST'])
# Define a function named check_password to be executed when the route is accessed
def check_password():# it is funcation for pull the data from form
    # Retrieve 'username' and 'password' from the form data submitted through the HTTP request
    name =request.form.get('username')
    password = request.form.get('password')
    # Print the received 'username' and 'password' to the console
    print({name},{password})
    # Return a simple response acknowledging the receipt of username and password
    return "username and password received" # and then return this string



if __name__ =="__main__":
    app.run(host="0.0.0.0")
    

