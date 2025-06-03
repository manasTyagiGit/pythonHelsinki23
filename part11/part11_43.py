class Task :
    cur_id = 1
    def __init__ (self, description: str, programmer: str, workload: int) :
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.cur_id
        Task.cur_id += 1        
        self.finish_flag = False

    def is_finished (self) :
        return self.finish_flag
    
    def mark_finished (self) :
        self.finish_flag = True

    def __str__ (self) :
        return f"{self.id} : {self.description} ({self.workload} hours), programmer {self.programmer} finished = {self.finish_flag}"
    
class OrderBook :
    def __init__ (self) :
        self.order_list = []
        self.programmer_list = []

    def add_order (self, description: str, programmer: str, workload: int) :
        task = Task (description, programmer, workload)
        self.order_list.append (task)
        if programmer not in self.programmer_list :
            self.programmer_list.append (programmer)

    def all_orders (self) :
        return self.order_list
    
    def programmers (self) :
        return self.programmer_list
    
    def mark_finished (self, id: int) :

        for task in self.order_list :
            if task.id == id :
                task.finish_flag = True
                return
            
        raise ValueError

    def finished_orders (self) :
        ret_list = []

        for task in self.order_list :
            if task.finish_flag == True :
                ret_list.append (task)

        return ret_list

    def unfinished_orders (self) :
        ret_list = []

        for task in self.order_list :
            if task.finish_flag == False :
                ret_list.append (task)

        return ret_list  
    
    def status_of_programmer (self, programmer: str) :

        if programmer not in self.programmer_list :
            raise ValueError
        
        finish_hours = 0
        unfinish_hours = 0
        finish_count = 0
        unfinish_count = 0

        for task in self.order_list :
            if task.programmer == programmer :
                if task.finish_flag == True :
                    finish_count += 1
                    finish_hours += task.workload

                else :
                    unfinish_count += 1
                    unfinish_hours += task.workload
        
        return (finish_count, unfinish_count, finish_hours, unfinish_hours)

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

print (orders.finished_orders()[1])
print (orders.unfinished_orders()[0])

status = orders.status_of_programmer("Adele")
# status = orders.status_of_programmer("Manas")
print(status)