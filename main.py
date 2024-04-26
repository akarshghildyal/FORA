from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Device(BaseModel):
    connection: bool
    motor: str
    speed: float

device_status = Device(connection=True, motor="on", speed=1.2)

@app.get("/device")
def read_device():
    return device_status

@app.post("/device")
def update_device(device: Device):
    global device_status
    device_status = device
    return device_status
