import jwt
from dotenv import dotenv_values
import datetime as dt

config = dotenv_values("./.env")

encoded_jwt = jwt.encode(
    {
        "exp": dt.datetime.utcnow() + dt.timedelta(weeks=1)
    }, 
    config.get("KEY"), 
    algorithm=config.get("ALGORITHM")
    )

print(f"Bearer {encoded_jwt}")
