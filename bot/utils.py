import re
from app.controllers import check_imei
from app.http_calls import get_http_client
from api.serializers.request import IMEIInfoRequest
from bot.enums import StaticMessages
from config import config


async def process_code(imei: str):
    if re.fullmatch('^\d{15}$', imei):
        async for client in get_http_client():
            return await check_imei(
                request_params=IMEIInfoRequest(
                    imei=imei,
                    token=config.CHECK_API_TOKEN
                ),
                client=client
            )
    else:
        return StaticMessages.WRONG_IMEI
