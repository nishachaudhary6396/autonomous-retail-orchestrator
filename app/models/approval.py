from pydantic import BaseModel


class Approval(BaseModel):

    approved: bool

    approver: str

    reason: str

    next_action: str