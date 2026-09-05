class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_time(self):
        flag_s = ""
        flag_m = ""
        flag_h = ""
        if self.second == 0: flag_s = "0"
        if self.minute == 0: flag_m = "0"
        if self.hour == 0: flag_h = "0"
        if self.hour > 24 or self.minute > 60 or self.second > 60:
            return f"Something Error"
        elif self.hour <= 12:
            return f"{self.hour}{flag_h}:{self.minute}{flag_m}:{self.second}{flag_s} am."
        else:
            return f"{self.hour - 12}{flag_h}:{self.minute}{flag_m}:{self.second}{flag_s} pm. "

    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
                if self.hour > 24:
                    self.hour = 0

# clock1 = Clock(20,45,59)
# clock2 = Clock(8,45,30)
# clock3 = Clock(50,20,45)
# print(clock1.get_time())
# print(clock2.get_time())
# print(clock3.get_time())
# clock3.set_time(21,30,55)
# print(clock3.get_time())
# clock1.tick()
# print(clock1.get_time())

# clock1 = Clock(20, 50, 15)
# print(clock1.get_time())  
# clock1.tick()
# clock1.tick()
# print(clock1.get_time())
# clock1.set_time(12, 0, 0)
# print(clock1.get_time())