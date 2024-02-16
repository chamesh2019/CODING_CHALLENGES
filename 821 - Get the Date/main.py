from datetime import datetime

def get_day(date):
    return datetime.strptime(date, "%m/%d/%Y").strftime("%A")