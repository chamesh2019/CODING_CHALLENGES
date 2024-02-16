from datetime import datetime

def get_day(date: str) -> str:
    return datetime.strptime(date, "%m/%d/%Y").strftime("%A")