from pydantic import BaseModel


class QualityReport(BaseModel):

    score: int

    critical_issues: list[str]

    medium_issues: list[str]

    low_priority_issues: list[str]

    recommendations: list[str]

    warehouse_approved: bool

    reasoning: str