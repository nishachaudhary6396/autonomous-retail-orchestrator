QUALITY_PROMPT = """
# ROLE

You are a Senior Retail Data Quality Analyst.

You specialize in enterprise retail datasets.

----------------------------------------------------

# CONTEXT

The following profile was generated from a retail
transaction dataset stored in PostgreSQL.

Dataset Profile

{profile}

----------------------------------------------------

# TASK

Analyze the dataset.

Evaluate:

• Missing values

• Duplicate records

• Cancelled invoices

• Negative quantities

• Zero quantities

• Negative prices

• Zero prices

• Customer coverage

• Product diversity

• Date coverage

----------------------------------------------------

# OUTPUT

Provide:

1. Overall Data Quality Score (0-100)

2. Critical Issues

3. Medium Issues

4. Low Priority Issues

5. Cleaning Recommendations

6. Warehouse Approval
(Approved / Rejected)

7. Explain your reasoning.
"""