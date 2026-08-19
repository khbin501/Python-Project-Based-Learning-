reports = [
    {"device_id": "a", "station": "semiconductor", "level": 2},
    {"device_id": "b", "station": "ai_engineering", "level": 4},
]

reports.append({"device_id" : "a", "station" : "semiconductor", "level" : 5})

ai_selected = []
semi_selected = []

for report in reports:
    if report["station"] == "ai_engineering":
        ai_selected.append(report)
    else :
        semi_selected.append(report)

print(len(ai_selected), len(semi_selected))

