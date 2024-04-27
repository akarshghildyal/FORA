from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Device(BaseModel):
    connection: Optional[bool] = Field(default=None)
    motor: Optional[str] = Field(default=None)
    speed: Optional[float] = Field(default=None)
    object: Optional[str] = Field(default=None)

device_status = Device(connection=True, motor="on", speed=1.2, object="NULL")

@app.get("/device")
def read_device():
    return device_status

@app.patch("/device")
def update_device(device: Device):
    global device_status
    updated_fields = device.dict(exclude_unset=True)
    for key, value in updated_fields.items():
        setattr(device_status, key, value)
    return device_status
