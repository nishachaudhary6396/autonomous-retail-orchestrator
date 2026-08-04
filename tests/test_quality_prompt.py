from app.prompts.quality_prompt import QUALITY_PROMPT

profile = {
    "total_rows": 541909,
    "duplicate_rows": 5268,
    "negative_quantity": 10624,
    "zero_price": 2515,
}

prompt = QUALITY_PROMPT.format(profile=profile)

print(prompt)