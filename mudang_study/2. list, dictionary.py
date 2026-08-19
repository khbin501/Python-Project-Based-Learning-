reports = [
    {"device_id": "a", "station": "semiconductor", "level": 2},
    {"device_id": "b", "station": "ai_engineering", "level": 4},
]

reports.append({"device_id" : "a", "station" : "semiconductor", "level" : 5})


ai_report = [report for report in reports if report["staion"] == "ai_engineering"]

avg = sum(report["level"] for report in reports) // len(reports)

latest_report = {}
for report in reports:
    latest_report[report["device_id"]] = report

latest_report = list(latest_report.values())

print(reports[0]["staion"])
