from datetime import datetime ,date

corrent_date = datetime.now().date()

deadline_date = date(2026,5,31)

remaining_days = (deadline_date - corrent_date).days

print(remaining_days)