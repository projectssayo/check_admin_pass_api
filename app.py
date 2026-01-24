from fastapi import FastAPI

from validate_password import Verify

app = FastAPI()
v=Verify()
@app.get("/password/")
def check_password(password: str):
    result=v.verify_password_one_input(password)
    return {**result}
    

@app.get("/info")
def get_info(cmd: str):

    return {
        "feed_password":"https://check-admin-pass.onrender.com/password/?password=123"
    }
    
