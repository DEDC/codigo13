import datetime

def check_available_date(date):
    try:
        d = datetime.datetime.fromisoformat(date).date()
        if d >= datetime.datetime.today().date():
            return True
        else:
            return False
    except:
        return False