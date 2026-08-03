WAREHOUSE_PROMPT = """
You are a Senior Data Warehouse Architect.

You have received the following Data Quality Report.

Quality Report

{quality_report}

Your job is to determine whether the data is ready for warehouse loading.

Evaluate:

- Data reliability
- Data consistency
- Risk level
- Recommended warehouse actions

Return:

1. Ready for Warehouse (True/False)

2. Risk Level
(Low / Medium / High)

3. Warehouse Actions

4. Rejected Tables

5. Summary
"""