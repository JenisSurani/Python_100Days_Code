import requests
# browser send http request to the website every time you search www.google.com
# and server of goggle responds as webpage

# there are many types of request

# get request

# to get data
# r=requests.get("https://site.financialmodelingprep.com/") # now r holds to the website 
# print(r.text) # gives html code for the website

# this is my api for the testing saved as api.py in directory
# /GET request is used to retrieve data.
# POST request is used to send data to a server.
r3=requests.get("http://127.0.0.1:5000/test")
print(r3.json()) # get responded data that send by server or api
print(r3.status_code) # search for the http status code in web


# post request
url="http://127.0.0.1:5000/test"
data = {"name": "Jenish", "age": 20}
r2=requests.post(url=url,json=data) # there are many parameters in post request so use dict format
print(r2.status_code)
print(r2.json())

#api is middleman between app and server
# api genrates codes accourding to user request and then send it to server and get respones and print the data



# Author : Jenis Surani
# Topic  : Request Module
# Date   : 28/02/2025