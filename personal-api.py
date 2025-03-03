# Update this file to add your code
# /name - Should give your name
# /register_number - Should give your register_number
# /department - Should give your department
from flask import Flask

app =Flask(__name__)

@app.route("/")
def name():
    return "Nandhakumar B M"


@app.route("/registerNumber")
def register_number():
    return "22IT026"

@app.route("/department")
def department():
    return "IT(Information Technology)"

if __name__ == "__main__":
    app.run(debug =True)
    
      