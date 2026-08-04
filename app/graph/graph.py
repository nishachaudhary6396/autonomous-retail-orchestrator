from langgraph.graph import StateGraph
from langgraph.graph import END

from app.graph.state import RetailState

from app.graph.nodes import (
    quality_node,
    warehouse_node,
    demand_node,
    inventory_node,
    approval_node,
)

workflow = StateGraph(RetailState)

# Add Nodes

workflow.add_node(
    "quality",
    quality_node
)

workflow.add_node(
    "warehouse",
    warehouse_node
)

workflow.add_node(
    "demand",
    demand_node
)

workflow.add_node(
    "inventory",
    inventory_node
)

workflow.add_node(
    "approval",
    approval_node
)


# Entry Point


workflow.set_entry_point(
    "quality"
)


# Workflow

workflow.add_edge(
    "quality",
    "warehouse"
)

workflow.add_edge(
    "warehouse",
    "demand"
)

workflow.add_edge(
    "demand",
    "inventory"
)

workflow.add_edge(
    "inventory",
    "approval"
)

workflow.add_edge(
    "approval",
    END
)

graph = workflow.compile()