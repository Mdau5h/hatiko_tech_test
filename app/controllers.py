import json
import pprint
from httpx import AsyncClient, HTTPStatusError
from fastapi import HTTPException, status
from api.serializers.request import IMEIInfoRequest
from config import config


async def check_imei(
        request_params: IMEIInfoRequest,
        client: AsyncClient
):

    url = config.CHECK_API_URL

    headers = {
        'Authorization': 'Bearer ' + request_params.token,
        'Content-Type': 'application/json'
    }

    payload = {
        "deviceId": request_params.imei,
        "serviceId": 12
    }

    try:
        response = await client.post(url, json=payload, headers=headers)
    except HTTPStatusError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=response.text
        )
    return response.text
