from app.models.quality_report import QualityReport
from app.models.warehouse_report import WarehouseReport
from app.models.demand_forecast import DemandForecast
from app.models.inventory_plan import InventoryPlan
from app.models.approval import Approval

from app.prompts.quality_prompt import QUALITY_PROMPT
from app.prompts.warehouse_prompt import WAREHOUSE_PROMPT
from app.prompts.demand_prompt import DEMAND_PROMPT
from app.prompts.inventory_prompt import INVENTORY_PROMPT
from app.prompts.approval_prompt import APPROVAL_PROMPT


from app.utils.llm import llm


quality_llm = llm.with_structured_output(QualityReport)

warehouse_llm = llm.with_structured_output(WarehouseReport)

demand_llm = llm.with_structured_output( DemandForecast)

inventory_llm = llm.with_structured_output(InventoryPlan)

approval_llm = llm.with_structured_output(Approval)

def quality_node(state):

    prompt = QUALITY_PROMPT.format(
        profile=state["profile"]
    )

    report = quality_llm.invoke(prompt)

    state["quality_report"] = report.model_dump()

    return state


def warehouse_node(state):

    prompt = WAREHOUSE_PROMPT.format(
        quality_report=state["quality_report"]
    )

    report = warehouse_llm.invoke(prompt)

    state["warehouse_report"] = report.model_dump()

    return state


def demand_node(state):

    prompt = DEMAND_PROMPT.format(
        analytics=state["analytics"]
    )

    report = demand_llm.invoke(prompt)

    state["demand_forecast"] = report.model_dump()

    return state


def warehouse_router(state):

    if state["warehouse_report"]["ready_for_warehouse"]:
        return "demand"

    return "end"

def inventory_node(state):

    prompt = INVENTORY_PROMPT.format(
        demand_forecast=state["demand_forecast"]
    )

    report = inventory_llm.invoke(prompt)

    state["inventory_plan"] = report.model_dump()

    return state


def approval_node(state):

    prompt = APPROVAL_PROMPT.format(

        quality_report=state["quality_report"],

        warehouse_report=state["warehouse_report"],

        demand_forecast=state["demand_forecast"],

        inventory_plan=state["inventory_plan"]

    )

    report = approval_llm.invoke(prompt)

    state["approval"] = report.model_dump()

    return state