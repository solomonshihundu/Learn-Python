from platform import machine


def get_even_date(event):
    return event.date

def current_users(events):
    events.sort(key = get_even_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machine[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machine.items():
        user_list = ", ".join(users)
        print("{}: {}".format(machine, user_list))