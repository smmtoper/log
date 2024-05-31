import hashlib
from datetime import datetime
from fastapi import FastAPI
from logger_wrapper import get_logger

logger = get_logger("user_service")

app = FastAPI()

@app.get("/user_id")
def get_user_id():
    time_str = str(datetime.now())
    user_id = hashlib.md5(time_str.encode()).hexdigest()
    logger.info(f"Generated user_id: {user_id}")
    return {"user_id": user_id}
