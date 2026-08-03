from pydantic import BaseModel


class DemandForecast(BaseModel):

    forecast_summary: str

    high_demand_products: list[str]

    medium_demand_products: list[str]

    low_demand_products: list[str]

    recommended_reorder: list[str]

    reasoning: str