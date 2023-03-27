import datetime

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
        self.date_time = date_time
        self.user_id = user_id
        self.departure = ticket_dapar
        self.arrival = ticket_arrival

    @property
    def date_time(self) :
        return self._date_time
    
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
            return True
        
        return False
    

class train :
    _trains = []

    def __init__(self ,train_depar ,train_arri ,train_date_time ,train_sits) :
        self.departure = train_depar
        self.arrival = train_arri
        self.date_time = train_date_time
        self.sits = int(train_sits)

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
    
    def sit_reservation(self) :
        if self.sits > 0 :
            self.sits -= 1
            return True
        
        return False
    
    def sit_cancelation(self) :
        self.sits += 1

    def __eq__(self,ticket) :
        if self.departure == ticket.departure and self.arrival == ticket.arrival :
            if self.date_time >= ticket.date_time :
                    return True   
                  
        return False


try : 
    train_cnt = int(input())

except ValueError :
    print("Error")
    exit()

for i in range(train_cnt) :
        try :
            train_departure ,train_arrival ,train_date_time ,train_sits = map(str ,input().split())
            new_train = train(train_departure ,train_arrival ,train_date_time ,train_sits)
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
