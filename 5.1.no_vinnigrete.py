import random
from datetime import datetime, timedelta

date1_str = input("הזן תאריך ראשון (YYYY-MM-DD): ")
date2_str = input("הזן תאריך שני (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

start_date = min(date1, date2)
end_date = max(date1, date2)

delta_days = (end_date - start_date).days

random_days = random.randint(0, delta_days)
random_date = start_date + timedelta(days=random_days)

print(f"התאריך שהוגרל הוא: {random_date.strftime('%Y-%m-%d')}")

if random_date.weekday() == 0:
    print("אין לי ויניגרט!")