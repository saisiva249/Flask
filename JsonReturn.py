from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def returnJson():
    retJson={
        "name":"Venkata",
        "Age":29,
        "array": [1,2,3,"Abc"]
    }
    return jsonify(retJson)

if __name__ =="__main__":
    app.run()

# all the communications betweeen teh server-> server, server-> browser, browser-> 
# we should be careful giving the values to json values, because some browsers may 
# support the null, also some may accept True, or true.

# Working of browser
# 1. when we hit a url in the browser, then the url will be sent to the ISP(internet service provider) 
# and this ISP will search in its DNS(Domain Name System) and returns the Domain Name and Ip address (which are unique for each site)
# 2. then our broser sends the request to the IP address, and the server which is at that IP will return the assosiated response to the browser

# How the requst and response should look like **when ever a server want ot request another server using HTTP 
# Request: there are so many request types (get, put, post) 
# example GET google.com/index.html => then it says we are asking google to provide index.html page as a response
# post(data of anu type can be json) /name="sai" google.com => this says that we are asking the google to take the data we are sending
# Response: this should consists of basically the status line
# status code
# message body {JSON}
