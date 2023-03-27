import jdatetime


class ticket :
    _tickets = []
    def __init__(self,date_time ,user_id ,ticket_dapar ,ticket_arrival,order) :
        self.date_time = date_time
        self.user_id = user_id
        self.departure = ticket_dapar
        self.arrival = ticket_arrival
        self.order = order

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

        self._date_time = jdatetime.datetime(year ,month ,day ,hour ,minute)
    
    def __eq__(self,other_ticket) :
        if self.departure == other_ticket.departure and self.arrival == other_ticket.arrival and self.user_id == other_ticket.user_id :
            for _train in train._trains :
                if _train == self :
                    if other_ticket.date_time - self.date_time >= jdatetime.timedelta(0,3600) :
                        _train.sits += 1
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

        self._date_time = jdatetime.datetime(year ,month ,day ,hour ,minute)
    
    def __ls__(self) :
        pass

    def __eq__(self,ticket) :
        if self.departure == ticket.departure and self.arrival == ticket.arrival :
            if self.date_time >= ticket.date_time :
                    return True   
                  
        return False


while True :
    try : 
        train_cnt = int(input())
        break
    except ValueError :
        print("Error")

for i in range(train_cnt) :
    while True :
        try :
            train_departure ,train_arrival ,train_date_time ,train_sits = map(str ,input().split())
            new_train = train(train_departure ,train_arrival ,train_date_time ,train_sits)
            train._trains.append(new_train)
            break
        except ValueError :
            print("Error")
print("Done")


while True :
    try : 
        calls_cnt = int(input())
        break
    except ValueError :
        print("Error")

for i in range(calls_cnt) :
    while True :
        try :
            ticket_date_time ,ticket_user_id ,ticket_departure ,ticktet_destination,*order = map(str ,input().split())
            if order == [] :

                new_ticket = ticket(ticket_date_time ,ticket_user_id ,ticket_departure ,ticktet_destination,order)
    
                for _train in train._trains :
                    if _train == new_ticket :
                        if _train.sits > 0 :
                            print("Movafag")
                            _train.sits -= 1
                            ticket._tickets.append(new_ticket)
                        else :
                            print("Na movafag")

                        break
                else :
                    print("Na Movafag")

            else :
                new_ticket = ticket(ticket_date_time ,ticket_user_id ,ticket_departure ,ticktet_destination,order)
                for _ticket in ticket._tickets :
                    if _ticket == new_ticket :
                        print("Movafag")

                        break
                else :
                    print("Na Movafag")


            break

        except ValueError :
            print("Error")


    

