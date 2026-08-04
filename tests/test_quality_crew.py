from app.crews.quality_crew import create_quality_crew

profile = {
    "total_rows": 541909,
    "duplicate_rows": 5268,
    "negative_quantity": 10624,
    "zero_price": 2515,
}

crew = create_quality_crew(profile)

result = crew.kickoff()

print(result)