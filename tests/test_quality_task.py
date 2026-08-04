from app.tasks.quality_task import create_quality_task

profile = {
    "total_rows": 541909,
    "duplicate_rows": 5268,
    "negative_quantity": 10624,
}

task = create_quality_task(profile)

print(task)