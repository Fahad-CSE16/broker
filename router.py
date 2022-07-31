from fastapi import APIRouter
from src.broker.schema import MessageSchema

router = APIRouter(
    tags=['items'],
    responses={404: {"description": "Page not found"}}
)


@router.post('/send-message')
async def send_message(payload: MessageSchema, request):
    request.app.pika_client.send_message(
        {"message": payload.message}
    )
    return {"status": "ok"}