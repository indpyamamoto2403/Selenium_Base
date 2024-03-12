import time

class Counter_Timer:
    
    def __init__(self):
        self.counter = 0
        self.current_start = None
        self.current_stop = None
        self.current_margin = None
        self.watched_history = []
    
    def start(self):
        self.current_start = time.time()
        
    def stop(self):
        self.current_stop = time.time()
    
    def get_span(self) -> float:
        self.current_margin = self.current_stop - self.current_start
        return round(self.current_margin, 2)
        
    def show_span(self):
        self.current_margin = self.current_stop - self.current_start
        self.current_margin = round(self.current_margin, 2)
        print(f'{self.current_margin}秒かかりました。')
        
    def add_span(self):
        self.current_margin = self.current_stop - self.current_start
        self.current_margin = round(self.current_margin, 2)
        self.watched_history.append(self.current_margin)
    
    def get_sum(self) ->float:
        return sum(self.watched_history)
    
    def show_sum(self):
        print(f'合計時間:{sum(self.watched_history)}')
    
    def get_count(self) ->int:
        return len(self.watched_history)

    def show_count(self):
        print(f"計測の合計回数は{len(self.watched_history)}です。")

    def get_average(self):
        sum = self.get_sum()
        count = self.get_count()
        avg = round(sum / count, 2)
        return avg
    
    def show_average(self):
        avg = self.get_average()
        print(f"計測の平均時間は{avg}です。")
    
    def reset_current(self):
        self.current_start = None
        self.current_stop = None
        self.current_margin = None
    
    def reset_all(self):
        self.counter = 0
        self.current_start = None
        self.current_stop = None
        self.current_margin = None
        self.watched_history = []
    
# timer = Counter_Timer()

# timer = Counter_Timer()
# for i in range(5):
#     timer.start()
#     time.sleep(i)
#     timer.stop()
#     timer.show_span()
#     timer.add_span()



# sum_time = timer.get_sum()
# timer.show_sum()
# timer.show_count()
# timer.show_average()