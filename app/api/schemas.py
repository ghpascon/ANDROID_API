from pydantic import BaseModel, Field


class MessagePayload(BaseModel):
    message: str = Field(..., description="Mensagem enviada para a API.")


class ApiResponse(BaseModel):
    status: str
    method: str
    message: str
    received: str | None = None
