from pydantic import BaseModel, ConfigDict


class UserCalc(BaseModel):
    user_name: str
    row: str
    message_id: int
    chat_id: int

    model_config = ConfigDict(from_attributes=True)


UserID = str

UsersCalc = dict[UserID, UserCalc]
