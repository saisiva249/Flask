from flask import Flask

# calling Flask constructor
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

# to run our web service when the 
if __name__ == "__main__":
    app.run()


# to run our flask web service we navigate to folder where our py file is there 
#>>to run the  following commands open command prompt in adminstrator
#1. we ahve to export our flask app> export FLASK_APP = HelloWorld.py
#2. then we can run our dlask >flask run
# as we are trying to modify the environment variables every time to run an application we will tryto create a 
# virtual environment or use Virtual box
