history_kalkulator = []

def add_history(item):
    history_kalkulator.insert(0, item)
    if len(history_kalkulator) > 10:
        history_kalkulator.pop()

def get_history():
    return history_kalkulator
