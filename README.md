# Create a Python API using flask
## Why Build an API?
An API acts as a bridge between different software applications, allowing them to communicate and share data. Whether you’re building a web application, mobile app, or even just automating some tasks, understanding how to # create and consume APIs opens up a world of possibilities.

## Setting Up Your Environment
We’ll need Python installed, and you can install Flask using a package manager like pip.
- Install flask: **pip install flask**

## Clone the Repo
**git clone https://github.com/vishalr22/Create-Python-API.git**

## Execute the Code: 
- **python main.py**

It will run the flask server on **localhost:5000** or **127.0.0.1:5000**

## Making a GET Request in Browser
http://127.0.0.1:5000/get_user/user_value?query="query_value"

## Response
![image](https://github.com/vishalr22/Create-Python-API/assets/58001028/e7791fbf-c5ba-460d-a2ee-01d8fe9c13e2)

## Making a POST Request using postman:
1. **Launch Postman**: Open Postman and make sure your Flask server is running at http://127.0.0.1:5000.
2. **Set Up Your Request**:
- Choose the HTTP method as POST.
- Enter the URL: http://127.0.0.1:5000/create-user.
- Navigate to the Body tab.
- Select raw and set the data type to JSON (application/json).
- In the text area, enter your JSON payload. For example: <b>{"username": "Vishal Rawat"}</b>
3. **Send the Request**: Hit the “Send” button to make the POST request.

## Response
![image](https://github.com/vishalr22/Create-Python-API/assets/58001028/faedef5e-1156-43fb-8635-fe62be4256e0)

## Congratulations! You’ve reached the end of our journey in creating a simple Python API using Flask.

# Thanks for Reading!
