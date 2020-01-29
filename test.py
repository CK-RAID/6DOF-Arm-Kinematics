class MyTime(object):
    def __init__(self, time, day):
        if isinstance(time, str):
            print("string")
        elif isinstance(time, int):
            print("int")
a = MyTime("ff",2)