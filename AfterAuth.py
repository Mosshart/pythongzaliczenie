from datetime import datetime

def returnActualTime(username, password):
    if not username == 'admin' or not password == 'admin': return 'Bledny login lub haslo'

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "Current Time: " + current_time
