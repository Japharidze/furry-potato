# furry-potato
Randomly named code assignment

This is the python project, built with [FastAPI](https://fastapi.tiangolo.com/)

## Description
Fetch list of open github gists for the provided user.  
By using the great [github API](https://docs.github.com/en/rest)

## Launch
Follow the steps:
1. Make sure you have python installed and opened the terminal in the project's directory
2. I recommend use the python virtualenv, but you can skip this step
3. Run ```pip install -r requirements.txt```
4. run ```uvicorn main:app```
5. It should be running at (http://127.0.0.1:8000/)

## Documentation
For API documentation, FastAPI uses it's own builtin tools to generate docs automatically.   
It even has more than one way of building it.  
For example you can check the next links
* (http://127.0.0.1:8000/docs)
* (http://127.0.0.1:8000/redoc)
