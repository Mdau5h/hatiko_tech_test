from fastapi import APIRouter, status, Depends
from httpx import AsyncClient
from app.http_calls import get_http_client
from app.controllers import check_imei
from api.serializers.request import IMEIInfoRequest

routes = APIRouter(prefix='/api')


@routes.post(
    "/check-imei",
    status_code=status.HTTP_200_OK,
)
async def check_imei_view(
        request_params: IMEIInfoRequest,
        client: AsyncClient = Depends(get_http_client)
):
    return await check_imei(request_params, client=client)
