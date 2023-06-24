import datetime

def only_between_9_and_5(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        if now.hour < 9 or now.hour > 17:
            raise ValueError('Function can only be called between 9am and 5pm')
        return func(*args, **kwargs)
    return wrapper

@only_between_9_and_5 
def do_something():
    print("do something")