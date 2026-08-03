from pydantic import BaseModel


class InventoryPlan(BaseModel):

    priority_reorders: list[str]

    standard_reorders: list[str]

    no_reorder_products: list[str]

    warehouse_actions: list[str]

    procurement_summary: str

    reasoning: str