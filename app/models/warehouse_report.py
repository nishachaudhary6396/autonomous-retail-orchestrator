from pydantic import BaseModel


class WarehouseReport(BaseModel):

    ready_for_warehouse: bool

    risk_level: str

    warehouse_actions: list[str]

    rejected_tables: list[str]

    summary: str