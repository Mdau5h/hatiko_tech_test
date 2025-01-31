from pydantic import BaseModel, Field


class IMEIInfoRequest(BaseModel):
    imei: str = Field(..., alias='imei', description='IMEI устройства')
    token: str = Field(..., alias='token', description='Токен авторизации')
