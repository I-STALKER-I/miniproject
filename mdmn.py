import datetime

<<<<<<< HEAD
class person :
    _users = []
    def __init__(self,id) :
        self.id = id
        self.last_cancel = None

    def reservation_cancelation(self,date_time) :
        self.last_cancel = date_time
class ticket :
    _tickets = []
    def __init__(self,date_time ,user_id ,ticket_dapar ,ticket_arrival) :
=======

class person :
    _users = []
    def __init__(self,id,date_time) :
        self.id = id
        self.last_cancel = None
        self.reserves = {}
        self.last_reserve = date_time

    def reservation_cancelation(self,date_time,ticket_class) :
        self.last_cancel = date_time
        self.reserves[ticket_class] -= 1
        
    @classmethod
    def reservation(cls,user_id,ticket_level,date_time) :
        if ticket_level == None :
            ticket_level = 0
        ticket_level = int(ticket_level)

        for user in cls._users :
            if user_id == user.id :
                if ticket_level in user.reserves :
                    user.reserves[ticket_level] += 1
                
                else :
                    user.reserves[ticket_level] = 1                    
                break

        else :
            new_user = person(user_id,date_time) 
            person._users.append(new_user) 
            new_user.reserves[ticket_level] = 1



class ticket :
    _tickets = []
    staged_for_remove_vips = {}
    def __init__(self,date_time ,user_id ,ticket_dapar ,ticket_arrival ,level = None,order = None) :
>>>>>>> feature
        self.date_time = date_time
        self.user_id = user_id
        self.departure = ticket_dapar
        self.arrival = ticket_arrival
<<<<<<< HEAD
=======
        self.order = order
        self.level = level
>>>>>>> feature

    @property
    def date_time(self) :
        return self._date_time
    
<<<<<<< HEAD
    @date_time.setter
    def date_time(self,ticket_date_time) :
        """the ticket_date_time we get is a string we have to separate the year and month and minute and  etc..."""

        first_slash_index = ticket_date_time.find('/')
        year = int(ticket_date_time[:first_slash_index])
        month = int(ticket_date_time[first_slash_index + 1:first_slash_index + 3])
        day = int(ticket_date_time[first_slash_index + 4:first_slash_index + 6])
        hour = int(ticket_date_time[first_slash_index + 7 : first_slash_index + 9])
        minute = int(ticket_date_time[first_slash_index + 10 : first_slash_index + 12])

        self._date_time = datetime.datetime(year ,month ,day ,hour ,minute)
    
    def __eq__(self,other_ticket) :
        if self.departure == other_ticket.departure and self.arrival == other_ticket.arrival and self.user_id == other_ticket.user_id :
=======
    @property
    def level(self) :
        return self._level
    
    
    @date_time.setter
    def date_time(self,ticket_date_time) :
        """the ticket_date_time we get is a string we have to separate the year and month and minute and  etc..."""
        try :
            first_slash_index = ticket_date_time.find('/')
            year = int(ticket_date_time[:first_slash_index])
            month = int(ticket_date_time[first_slash_index + 1:first_slash_index + 3])
            day = int(ticket_date_time[first_slash_index + 4:first_slash_index + 6])
            hour = int(ticket_date_time[first_slash_index + 7 : first_slash_index + 9])
            minute = int(ticket_date_time[first_slash_index + 10 : first_slash_index + 12])

            self._date_time = datetime.datetime(year ,month ,day ,hour ,minute)
        except AttributeError :
                
                self._date_time = ticket_date_time
    
    @level.setter
    def level(self,value) :
        if value == None :
            self._level = 0
        elif self.order == 'cancel' :
            self._level = int(value)
        
        elif value == 'cancel' :
            self._level = 0
            
        else :
            self._level = int(value)
            
    def __eq__(self,other_ticket) :
        if self.departure == other_ticket.departure and self.arrival == other_ticket.arrival and self.user_id == other_ticket.user_id and self.level == other_ticket.level :

>>>>>>> feature
            return True
        
        return False
    
<<<<<<< HEAD

class train :
    _trains = []

    def __init__(self ,train_depar ,train_arri ,train_date_time ,train_sits) :
        self.departure = train_depar
        self.arrival = train_arri
        self.date_time = train_date_time
        self.sits = int(train_sits)
=======
    @classmethod
    def removation(cls,_ticket) :
        if _ticket.level ==  0 :
            ticket._tickets.remove(_ticket)
            return  f'Reserve karbar {_ticket.user_id} ba movaghiat cancel shod.'


        else :
            for vip in ticket.staged_for_remove_vips :
                if ticket.staged_for_remove_vips == _ticket.user_id and ticket.staged_for_remove_vips[vip] == _ticket.level :
                    return 'Na Movafagh. Darkhast cancel shoma qablan sabt shode ast.'
            ticket._tickets.remove(_ticket)
            ticket.staged_for_remove_vips[_ticket.user_id] = _ticket.level
            return f'Darkhast cancel reserve karbar {_ticket.user_id} baraye belit VIP{_ticket.level} sabt shod.'
class train :
    _trains = []

    def __init__(self ,train_depar ,train_arri ,train_date_time ,train_normal_sits) :
        self.departure = train_depar
        self.arrival = train_arri
        self.date_time = train_date_time
        self.sits = {0 : int(train_normal_sits)}
>>>>>>> feature

    @property
    def date_time(self) :
        return self._date_time
    
    @date_time.setter
    def date_time(self ,train_date_time) :
        """the train_date_time we get is a string we have to separate the year and month and minute and  etc..."""

        first_slash_index = train_date_time.find('/')
        year = int(train_date_time[:first_slash_index])
        month = int(train_date_time[first_slash_index + 1:first_slash_index + 3])
        day = int(train_date_time[first_slash_index + 4:first_slash_index + 6])
        hour = int(train_date_time[first_slash_index + 7 : first_slash_index + 9])
        minute = int(train_date_time[first_slash_index + 10 : first_slash_index + 12])

        self._date_time = datetime.datetime(year ,month ,day ,hour ,minute)
    
<<<<<<< HEAD
    def sit_reservation(self) :
        if self.sits > 0 :
            self.sits -= 1
            return True
        
        return False
    
    def sit_cancelation(self) :
        self.sits += 1
=======
    def sit_reservation(self,ticket_level,user_id,date_time) :
        if ticket_level == None :
            ticket_level = 0

        if int(ticket_level) > 0 :
            for user in person._users :
                if user.id == user_id : 
                    if 0 in user.reserves :
                        if date_time - user.last_reserve <= datetime.timedelta(30) :
                            break
            
            else :      
                return 'Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid.'
            
        if int(ticket_level) > 0 :
            
            for vip_class in ticket.staged_for_remove_vips :
                if ticket.staged_for_remove_vips[vip_class] == int(ticket_level) :
                    del ticket.staged_for_remove_vips[vip_class]
                    return f'Reserve karbar {user_id} baraye belit model VIP{ticket_level} movafagh bood. Hamchenin Reserve karbar {vip_class} baraye in belit cancel shod.'
                


        for sit_level in self.sits :
            if int(sit_level) == int(ticket_level) :
                if self.sits[sit_level] > 0 :
                    self.sits[sit_level] -= 1
                    return True
                    
                return "Na Movafagh. Zarfiat vojood nadarad."
            
        return "Na Movafagh. Model vojood nadarad."
    
    def sit_cancelation(self,sit_class) :
        
        self.sits[sit_class] += 1
>>>>>>> feature

    def __eq__(self,ticket) :
        if self.departure == ticket.departure and self.arrival == ticket.arrival :
            if self.date_time >= ticket.date_time :
                    return True   
                  
        return False


<<<<<<< HEAD
=======
class Order(ticket) :
    _orders = []
    def __init__(self ,date_time ,user_id ,ticket_departure ,ticket_arrival ,level = None ,order = None) :
        super().__init__(date_time,user_id,ticket_departure,ticket_arrival)
        self._level = level
        self._order = order
        self.answer = None
    
    @classmethod
    def sort(cls,new_order) :
        for order in cls._orders :
            if new_order <  order :
                cls._orders.insert(cls._orders.index(order),new_order)
                return 
        cls._orders.append(new_order)
        
    def __lt__(self,order) :
        """define self as new_order"""
        if self.date_time <= order.date_time :
            return True
        return False

    def __call__(self) :
        """here we want to pass a list to our order_manager function """
        
        lst = [self.date_time,self.user_id,self.departure,self.arrival,self._level,self._order]
        return lst
    
    def __eq__(self,other) :
        if id(self) == id(other) :
            return True
        return False
    """guess why i overrided __eq__ ...
    when python wants to hash in a list it checks the equality of objects in the list(i guess) and if they are 
    equals they both get a same index.our subclass to be Orders inherits from the main class ticket  
    that in it we had overrided __eq__ once.this causes problem in our hashing so we have to override our __eq__ again """


>>>>>>> feature
try : 
    train_cnt = int(input())

except ValueError :
    print("Error")
    exit()

for i in range(train_cnt) :
        try :
<<<<<<< HEAD
            train_departure ,train_arrival ,train_date_time ,train_sits = map(str ,input().split())
            new_train = train(train_departure ,train_arrival ,train_date_time ,train_sits)
=======
            train_departure ,train_arrival ,train_date_time ,train_normal_sits,*train_vip_sits = map(str ,input().split())

            new_train = train(train_departure ,train_arrival ,train_date_time ,train_normal_sits)

            if train_vip_sits != [] and int(train_vip_sits[0]) > 0 :
                vip_count = list(map(int ,input().split()))
                for i ,j in enumerate(vip_count) :
                    new_train.sits[i + 1] = j

>>>>>>> feature
            train._trains.append(new_train)

        except ValueError :
            print("Error")
            exit()
print("Done")


try : 
    calls_cnt = int(input())
except ValueError :
    print("Error")
    exit()

<<<<<<< HEAD
def order_manager(date_time,ticket_user_id,ticket_departure,ticket_destination,order = None) :

    new_ticket = ticket(date_time,ticket_user_id,ticket_departure,ticket_destination)

    if order == None :
        for _train in train._trains :
            if _train == new_ticket :
                if _train.sit_reservation() : 
                    ticket._tickets.append(new_ticket)
                    person._users.append(person(ticket_user_id))
                    return True

        return False

    elif order == "cancel" :

        for _ticket in ticket._tickets :
            if new_ticket == _ticket :
                for _train in train._trains :
                    if _train == _ticket :
                        for user in person._users :
                            if user.id == ticket_user_id :
                                if user.last_cancel == None :
                                    user.reservation_cancelation(new_ticket.date_time)
                                    ticket._tickets.remove(_ticket)
                                    _train.sit_cancelation()
                                    return True
                                
                                else :
                                    if new_ticket.date_time - user.last_cancel >= datetime.timedelta(0,3600) :
                                        user.reservation_cancelation(new_ticket.date_time)
                                        ticket._tickets.remove(_ticket)
                                        _train.sit_cancelation()
                                        return True
                            
                                    else :
                                        return False
                        return False
                    
                return False

        return False

    else :
        raise ValueError

for i in range(calls_cnt) :
        try :
            call_order = input().split()
            if order_manager(*call_order) :
                print("Movafagh")
            else :
                print("Na Movafagh")

        except ValueError :
            print("Error")
=======
def order_manager(order_instance,date_time,ticket_user_id,ticket_departure,ticket_destination,order = None,order_2 = None) :

    new_ticket = ticket(date_time ,ticket_user_id ,ticket_departure ,ticket_destination ,order ,order_2)
    try :
        if (order == None or int(order) >= 0) and order != "cancel" and order_2 != 'cancel':
            for _train in train._trains :
                if _train == new_ticket :
                    answer = _train.sit_reservation(order,ticket_user_id,date_time)
                    if isinstance(answer,bool) : 
                        ticket._tickets.append(new_ticket)
                        person.reservation(ticket_user_id,order,date_time)
                        if order == None or int(order) == 0 :
                            model = "Normal"
                        else :
                            model = f"VIP{order}"
                        
                        order_instance.answer = f"Reserve karbar {ticket_user_id} baraye belit model {model} movafagh bood."
                        return
                    
                    else :
                        order_instance.answer = answer
                        return
        

            order_instance.answer =  "Na Movafagh. Masir vojood nadarad."
            return
        
        else :
            raise ValueError
        
    except ValueError :
        if order == "cancel" or order_2 == "cancel" :
        
            for _ticket in ticket._tickets :
                if new_ticket == _ticket :
                    for _train in train._trains :
                        if _train == _ticket :
                            for user in person._users :
                                if user.id == ticket_user_id :
                                    if user.last_cancel == None :
                                        user.reservation_cancelation(new_ticket.date_time,new_ticket.level)
                                        answer = ticket.removation(_ticket)
                                        _train.sit_cancelation(new_ticket.level)
                                        order_instance.answer = answer
                                        return 
                                    
                                    else :
                                        if new_ticket.date_time - user.last_cancel >= datetime.timedelta(0,3600) :
                                            user.reservation_cancelation(new_ticket.date_time,new_ticket.level)
                                            answer = ticket.removation(_ticket)
                                            _train.sit_cancelation(new_ticket.level)
                                            order_instance.answer = answer
                                            return 
                            
                                        else :
                                            order_instance.answer = "Na Movafagh. Shoma dar 1 sa'at akhir darkhast cancel dashtid."
                                            return
                            
                            order_instance.answer = "Na Movafagh. Reserve vojood nadarad."
                            return
            for vip in ticket.staged_for_remove_vips :
                if vip == new_ticket.user_id and ticket.staged_for_remove_vips[vip] == new_ticket.level :
                    order_instance.answer = "Na Movafagh. Darkhast cancel shoma qablan sabt shode ast."
                    return

            order_instance.answer = "Na Movafagh. Reserve vojood nadarad." 
    

not_sorted_list = []
for i in range(calls_cnt) :
        try :
            call_order = input().split()
            
            new_order = Order(*call_order)
            not_sorted_list.append(new_order)
            Order.sort(new_order)

        except ValueError :
            print("Error")

for _order in Order._orders :
    order_manager(_order,*_order())      


for order in not_sorted_list :
    print(order.answer)
>>>>>>> feature
