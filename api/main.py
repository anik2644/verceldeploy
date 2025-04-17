from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


# Define a route that responds to GET requests at the root URL ("/")
@app.get("/")
async def read_root():
    return {"message": "Hello World"}


# Another example with a path parameter
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
