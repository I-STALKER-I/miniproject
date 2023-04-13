"""the code was a mess so i decided to do a hotfix"""
"""the code was a mess so i decided to do a hotfix"""
import datetime

class Order :
    """this orders list are sorted by date_time"""
    orders = []
    orders_not_sorted = []
    """we need not sorted for represntation"""

    def __init__(self ,date_time ,user_id ,origin ,destination ,vehicle_model = None,shifter_1 = None ,shifter_2 = None) :
        """i call them shifter because they can change """
        self._origin = origin
        self._destination = destination
        self._date_time = date_time
        self._age = [vehicle_model,shifter_1]
        self._user_id = int(user_id)
        self._answer = None

        if Order.nearest_way_check(vehicle_model) == False :
            
            self._level = [shifter_1,shifter_2]
            self._rule = [shifter_1,shifter_2] 
            self._vehicle_model = vehicle_model
            """level assumes that what in what class our order is(Normal,VIP1,VIP2,...)"""
            """rule assumes that our order is a cancelation or a reservation"""
        else :
            self._level = [vehicle_model,None]
            self._rule = ["quickway",None]
            self._vehicle_model = None

        Order.sort(self)

    @property
    def _age(self) :
        return self.age
    
    @_age.setter
    def _age(self,lst) :
        if lst[1] == "cancel" :
            return
        
        if lst[1] == None :
            self.age = int(lst[0])
        else :
            try :
                self.age = int(lst[1])

            except ValueError :
                pass
            
    @property
    def _vehicle_model(self) :
        return self.vehicle_model

    @_vehicle_model.setter
    def _vehicle_model(self ,string) :
            try :
                self.vehicle_model = string.lower()
            except AttributeError :
                self.vehicle_model = string

    @property
    def _date_time(self) :
        return self.date_time
    

    @_date_time.setter
    def _date_time(self,string) :
        """the datetime we get as input is a string we have to extract the year and the mont and etc... from it """
        first_slash_index = string.find('/')
        year = int(string[:first_slash_index])
        month = int(string[first_slash_index + 1:first_slash_index + 3])
        day = int(string[first_slash_index + 4:first_slash_index + 6])
        hour = int(string[first_slash_index + 7 : first_slash_index + 9])
        minute = int(string[first_slash_index + 10 : first_slash_index + 12])
        self.date_time = datetime.datetime(year ,month ,day ,hour ,minute)

    @property
    def _level(self) :
        return self.level

    @_level.setter
    def _level(self,shifters) :
        if shifters[0] == None :
            self.level = 0
        elif shifters[0] == 'cancel' :
            self.level = 0
        elif  isinstance(int(shifters[0]),int):
                if not shifters[1] == "cancel" and not shifters[1] == None :
                    self.level = int(shifters[1])
                elif shifters[1] == None and isinstance(int(shifters[0]),int) :
                    self.level = 0
                elif shifters[1] == "cancel" :
                    self.level = int(shifters[0])



        else :
            self.level = 0

    @property
    def _rule(self) :
        return self.rule
    
    @_rule.setter
    def _rule(self,shifters) :
        if shifters[0] == "quickway" :
            self.rule = "quickway"
            return
        
        if shifters[0] == None :
            self.rule = "reserve"
        elif shifters[0] == 'cancel' or shifters[1] == 'cancel' :
            self.rule = 'cancel'
        else :
            self.rule = "reserve"
    
    @staticmethod
    def nearest_way_check(vehicle_model) :
        try :
            if vehicle_model == None or isinstance(int(vehicle_model),int) :
                return True
            return False
        except ValueError :
            return False
        
    @classmethod
    def sort(cls,instance) :
        cls.orders_not_sorted.append(instance)
        for order in cls.orders :
            if instance < order :
                
                cls.orders.insert(cls.orders.index(order),instance)
                return
            
        cls.orders.append(instance)
        return
        
    def __lt__(self,other_instance) :
        if self._date_time < other_instance._date_time :
            return True
        return False
    
    def __repr__(self) :
        #return f"{self._user_id}"
        return f"{self._date_time} ,{self._origin} ,{self._destination} ,{self._vehicle_model} ,{self._level} ,{self._rule} ,{self._user_id}"
    
class order_laws(Order) :
    counter = 0
    def __init__(self,entry_line) :
        self._date_time = entry_line[0]
        self._rule = "order_law"
        self.add_number()
        self._law_number = self.counter
        self._answer = ''
        if entry_line[1] == "Zarfiat" :

            self._action = "Zarfiat"
            self._vehicle_model = entry_line[4]
            self._percent = int(entry_line[6]) / 100

        elif entry_line[1] == "Reserve" and entry_line[3] == "baraye" :
            self._action = "sen"
            self._vehicle_model = entry_line[2]
            self._age = int(entry_line[6])
            

        elif entry_line[1] == "Reserve" and entry_line[3] == "dar" :
            self._action = 'saat'
            self._vehicle_model = entry_line[2]
            self._begin_time = self.date_time_maker(entry_line[5])
            self._end_time = self.date_time_maker(entry_line[7])

        elif entry_line[1] == "Emkan" :

            self._action  = "Emkan"
            self._vehicle_model = entry_line[4]
            self._times_per_period = int(entry_line[7])
            self._period = entry_line[10]

        else :
            raise ValueError
        
        Order.sort(self)

    @property
    def _age(self) :
        return self.age
    
    @_age.setter
    def _age(self,value) :
        self.age = value

    @property
    def _answer(self) :
        return self.answer

    @_answer.setter
    def _answer(self,value) :
        if value == '' :
            self.answer = f"Qanoon shomareye {self._law_number} ba movafaghiat sabt shod."

        else :
            self.answer += "\n" + value
     
    @property
    def _rule(self) :
        return self.rule
    
    @_rule.setter
    def _rule(self,value) :
        self.rule = value

    @classmethod
    def add_number(cls) :
        cls.counter += 1

    @staticmethod
    def  date_time_maker(string) :
        hour = int(string)
        return datetime.time(hour)


class vehicle(Order) :
    vehicles = []
        
    def __init__(self ,vehicle_model ,origin ,destination ,date_time ,Normal_sits ,vip_sits = None) :
        
        """be aware that time means hour and seconds and etc...
           but times means how many times"""
        self._time_limiter = {}
        self._times_limiter = {}
        self._vehicle_model = vehicle_model
        self._origin = origin
        self._destination = destination
        self._date_time = date_time
        self._sits_calculator = [Normal_sits ,vip_sits]
        self._sits = self._sits_calculator
        self._const_sits = self._sits_calculator
        self._reserves_datetime_list = []
        self._reserves_counter = 0
        self._reservers = None
        vehicle.vehicles.append(self)

    @property
    def _const_sits(self) :
        return self.const_sits
        
    @_const_sits.setter
    def _const_sits(self,kwargs) :
        self.const_sits = {**kwargs}

    @property
    def _reservers(self) :
        return self.reservers
    
    @_reservers.setter
    def _reservers(self,value) :
        if value == None :
            self.reservers = []
        
        else :
            self.reservers.insert(0,value)

    @property
    def _sits_calculator(self) :
        return self.sits 
    
    @_sits_calculator.setter
    def _sits_calculator(self,shifters) :
        all_sits = {0 : int(shifters[0])}
        if shifters[1] == None :
            self.sits = all_sits
            return
        

        
        if int(shifters[1]) > 0 :
            vip_sits = input().split()
            for i in range(int(shifters[1])) :
                all_sits[i + 1] = int(vip_sits[i])

        self.sits = all_sits
    
    def remove(self,sit_class) :
        self._sits[sit_class] -= 1

    @classmethod
    def sorts(cls ,instance) :
        for transporter in cls.vehicles :
            if instance < transporter :
                
                cls.vehicles.insert(cls.vehicles.index(transporter),instance)
                return
            
        cls.vehicles.append(instance)
        return
    
    def __eq__(self,order) :
        if not isinstance(order,vehicle) :
            if self._origin == order._origin and self._destination == order._destination and self._vehicle_model == order._vehicle_model :
                return True
            return False
    
    def __repr__(self) :
        return f"{self._date_time}"
    
class transporter_limiter :
    def __init__(self,end_time,reservation_count,limitaion_count) :
        self._end_time = end_time
        self._reserves = reservation_count
        self._limitation_cnt = limitaion_count


class staged_vips :
    staged_vips_list = []
    def __init__(self ,previous_user ,vip_class ,using_vehicle ,date_time ,origin ,destination,transporter) :
        self._origin = origin
        self._destination = destination
        self._previous_user = previous_user
        self._level = vip_class
        self._vehicle_model = using_vehicle
        self._date_time = date_time
        self._transporter = transporter
        staged_vips.sort(self)
    
    @classmethod
    def sort(cls,instance) :
        for staged_vip in cls.staged_vips_list :
            if instance._date_time < staged_vip._date_time :
                
                cls.staged_vips_list.insert(cls.staged_vips_list.index(staged_vip),instance)
                return
            
        cls.staged_vips_list.append(instance)
        return


    def delete(self) :
        staged_vips.staged_vips_list.remove(self)

    def __eq__(self,order) :
        try :
            if self._level == order._level and self._vehicle_model == order._vehicle_model and self._previous_user == order._user_id and self._origin == order._origin and self._destination == order._destination :
                return True
            return False
        except AttributeError :
            if id(self) == id(order) :
                return True
            return False


class person :
    users = []
    def __init__(self ,user_id ,date_time ,tickets) :
        maybe_a_user = person.equality_check(user_id)
        if maybe_a_user == False :
            self._user_id = int(user_id)
            self._last_buy_date_time = date_time
            self._last_cancel = None
            self._tickets = tickets
            person.users.append(self)
        else :
            """the maybe_a_username variable is now a real user cause it was found in searching check
            we will only update our tickets list and our last buy date_time"""
            maybe_a_user._tickets = tickets
            maybe_a_user._last_buy_date_time = date_time

    @property
    def _tickets(self) :
        return self.tickets
    
    @_tickets.setter
    def _tickets(self,ticket) :
        ticket = [ticket]
        try :
            self.tickets += ticket
        except AttributeError :
            self.tickets = ticket

    def remove(self,ticket) :
        try :
            self._tickets.remove(ticket)
        except ValueError :
            pass

    @classmethod
    def equality_check(cls,user_id) :
        for user in cls.users :
            if user._user_id == int(user_id) :
                return user
        return False


class execution :

    @classmethod
    def main_executioner(cls,order) :
        cls.vehicle_end_date_checker(order)
        if order._rule == "reserve" :
            cls.reservation(order)
        elif order._rule == "cancel" :
            cls.cancelation(order)

        elif order._rule == "quickway" :
            cls.quickway(order)

        elif order._rule == "order_law" :
            cls.order_law(order)

        else :
            raise ValueError
        
    @classmethod
    def order_law(cls,order) :

        if order._action == "Zarfiat" :
            cls.capacity_change(order)            

        elif order._action == "sen" :

            cls.age_limitation(order)

        elif order._action == "saat" :
            cls.time_limitation(order)

        elif order._action == "Emkan" :

            cls.times_limitation(order)

    @classmethod
    def times_limitation(cls,order) :
        for transporter in vehicle.vehicles :
            if transporter._vehicle_model == order._vehicle_model :
                cls.transporter_times_limit_set(transporter,order._period,order._times_per_period,order)

    @classmethod
    def capacity_change(cls ,order) :
        for transporter in vehicle.vehicles :
            if transporter._vehicle_model == order._vehicle_model :
                cls.capacity_changer(transporter,order) 

    @classmethod
    def age_limitation(cls,order) :
        for transporter in vehicle.vehicles :

            for reserve in transporter._reservers :
                if reserve._age > order._age :
                    transporter._reservers.remove(reserve)
                    for user in person.users :
                        if user._user_id == reserve._user_id :
                            user._tickets.remove(reserve)
                            order._answer = f"Reserve karbar {reserve._user_id} baraye airplane model VIP1 be dadil qanoon {order._law_number} cancel shod."

    @classmethod
    def time_limitation(self ,order) :
        for transporter in vehicle.vehicles :
            if transporter._vehicle_model  == order._vehicle_model :
                transporter._time_limiter[order._begin_time] = order._end_time

    @classmethod
    def cancelation(cls,order) :
        tickets_existing_validate = cls.validation_for_cancelation(order)

        if tickets_existing_validate == False :
            return
        else :
            if order._level == 0 :
                cls.normal_cancelation(*tickets_existing_validate,order)
            else :
                cls.vip_cancelation(*tickets_existing_validate,order)



    @classmethod
    def normal_cancelation(cls ,user ,ticket ,transporter ,order) :
        if cls.one_hour_check(user ,order) :
            cls.user_cancel_changes(user ,order ,ticket)
            order._answer = f"Reserve karbar {order._user_id} baraye {order._vehicle_model} ba movafaghiat cancel shod.‍‍"
            
        else :
            order._answer = "Na Movafagh. Shoma dar 1 sa'at akhir darkhast cancel dashtid."

 
    @classmethod
    def vip_cancelation(cls ,user ,ticket ,transporter ,order) :
        if cls.one_hour_check(user ,order) :
            staged_vips(order._user_id,order._level ,order._vehicle_model ,ticket._date_time,order._origin,order._destination,transporter)
            cls.user_cancel_changes(user ,order ,ticket ,True)
            order._answer = f"Darkhast cancel reserve karbar {order._user_id} baraye belit {order._vehicle_model} VIP{order._level} sabt shod."
        else :
            order._answer = "Na Movafagh. Shoma dar 1 sa'at akhir darkhast cancel dashtid."

    @classmethod
    def reservation(cls,order) :
        equality = cls.equality_check(order)
        if isinstance(equality,vehicle) == False and isinstance(equality,staged_vips) == False :
            return
        
        else :
            if order.level == 0 :
                cls.Normal_reservation(order,equality)
                return
            else :
                cls.vip_reservation(order,equality)
                return

    @classmethod
    def Normal_reservation(cls ,order ,transporter) :
            person(order._user_id,order._date_time,order)
            transporter._reservers = order
            transporter.remove(order._level)
            transporter._reserves_datetime_list.append(order._date_time)

            order._answer = f"Reserve karbar {order._user_id} baraye belit {order._vehicle_model} model Normal movafagh bood."
            cls.transporter_limiter_add(transporter,order)
            return
        
    @classmethod
    def vip_reservation(cls ,order ,transporter) :
        staged_vip = cls.staged_vips_reservation(order)
        
        if cls.sit_check(transporter ,order._level) :
            if cls.thirty_days_vip_check(order) == False :
                order._answer = "Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid."

            if isinstance(staged_vip,staged_vips) :
                order._answer = f"Reserve karbar {order._user_id} baraye belit {order._vehicle_model} model VIP{order._level} movafagh bood. Hamchenin Reserve karbar {staged_vip._previous_user} baraye in belit cancel shod."
                staged_vip.delete()
                return
                
            else :
                person(order._user_id,order._date_time,order)
                transporter._reservers = order
                transporter.remove(order._level)

                order._answer = f"Reserve karbar {order._user_id} baraye belit {order._vehicle_model} model VIP{order._level} movafagh bood."
                transporter._reserves_datetime_list.append(order._date_time)
                cls.transporter_limiter_add(transporter,order)
                return

        else :
            order._answer = "Na Movafagh. Zarfiat vojood nadarad."
            return
        
    @classmethod
    def quickway(cls,order) :

        validation_3 = True

        if order._level > 0 :
            if cls.thirty_days_vip_check(order) == False :
                validation_3 = False
            

        quickest_vehicle = None
        nearest_time = datetime.timedelta(6000,0)
        validation_1 = False
        validation_2 = False
        for transporter in vehicle.vehicles :
 
                if cls.quick_way_transporter_check(transporter,order) :
                    validation_1 = True
                    if cls.sit_check(transporter,order._level) :
                        validation_2 = True
                        if nearest_time > transporter._date_time - order._date_time and transporter._date_time - order._date_time > datetime.timedelta(0,0):
                            nearest_time = transporter._date_time - order._date_time
                            quickest_vehicle = transporter

        for staged_vip in staged_vips.staged_vips_list :


            if staged_vip._level == order._level and staged_vip._origin == order._origin and staged_vip._destination == order._destination :
                validation_1 = True
                validation_2 = True
                quickest_vehicle = staged_vip          


        if validation_1 == False :
            order._answer = "Na Movafagh. Masir vojood nadarad."
        
        elif validation_2 == False :
            order._answer = "Na Movafagh. Zarfiat vojood nadarad."

        elif validation_3 == False :
            order._answer =  "Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid."

        else :
            order._vehicle_model = quickest_vehicle._vehicle_model
            order._rule = [None,None]
            cls.main_executioner(order)

    @classmethod
    def equality_check(cls,order) :
        validation_1 = False
        validation_2 = False
        validation_3 = False

        for transporter in vehicle.vehicles :
            if transporter == order :
                validation_1 = True
                if cls.sit_check(transporter,order._level) :
                    validation_2 = True
                    if cls.transporter_time_limit_check(transporter,order) == True :
                        if cls.transporter_times_limit_check(transporter,order) == True :
                            validation_3 = True
                            answer =  transporter
                            break
            
        for staged_vip in staged_vips.staged_vips_list :

            if staged_vip._level == order._level and staged_vip._vehicle_model == staged_vip._vehicle_model and staged_vip._origin == order._origin and staged_vip._destination == order._destination :
                validation_1 = True
                validation_2 = True
                answer = staged_vip
                break
                
        if validation_1 == False :
            order._answer = "Na Movafagh. Masir vojood nadarad."
            return False
        elif validation_2 == False :
            order._answer = "Na Movafagh. Zarfiat vojood nadarad." 
            return False
        elif validation_3 == False :
            order._answer = "Na Movafagh. Emkan reserve vojood nadarad"
            return False
        
        else :

            return answer
        
        

    @classmethod
    def validation_for_cancelation(cls ,order) :
        if order._level == 0 :
            validation = cls.tickets_existing_validation(order) 
            if validation == False :
                order._answer = "Na Movafagh. Reserve vojood nadarad." 
                return False
            else :
                return validation
        else :
            validation_1 = cls.staged_vips_cancelation(order)
            validation_2 =  cls.tickets_existing_validation(order)

            if validation_1 == False and validation_2 == False :
                order._answer =  "Na Movafagh. Reserve vojood nadarad." 
                return False    
            elif validation_1 == True :
                order._answer = "Na Movafagh. Darkhast cancel shoma qablan sabt shode ast."
                return False
            elif validation_1 == True and validation_2 == False:
                return validation_2 
            elif validation_1 == False and validation_2 != False :
                return validation_2
            
    @classmethod
    def capacity_changer(cls,transporter,order) :
        old_const_sits = {**transporter._const_sits}
        for sit in transporter._const_sits :
            transporter._const_sits[sit] *= order._percent
            transporter._const_sits[sit] = int(transporter._const_sits[sit])
            transporter._const_sits[sit] -= old_const_sits[sit] - transporter._sits[sit]
            if transporter._const_sits[sit] < 0 :
                cls.ticket_remover(transporter ,sit,transporter._const_sits[sit],order)
                transporter._const_sits[sit] = 0

    @classmethod
    def ticket_remover(cls,transporter ,level,sits_to_cancel,order) :
        for i in range( - sits_to_cancel) :
            for reserve in transporter._reservers :
                if reserve._level == level :
                    
                    
                    for user in person.users :
                        if user._user_id == reserve._user_id :                         
                            user.remove(reserve)
                            order._answer = f"Reserve karbar {user._user_id} baraye {reserve._vehicle_model} model {cls.level_finder(reserve)} be dadil qanoon {order._law_number} cancel shod."
                    transporter._reservers.remove(reserve)
                    break

    @staticmethod
    def transporter_limiter_add(transporter,order) :
        if len(transporter._times_limiter) == 0 :
            return
        else :
            
            for limit in transporter._times_limiter :
                
                if order._date_time < limit :
                    transporter._times_limiter[limit][1] += 1

    @staticmethod
    def transporter_times_limit_check(transporter,order) :
        for limit in transporter._times_limiter :
            if limit > order._date_time :
                if transporter._times_limiter[limit][0] <= transporter._times_limiter[limit][1] :
                    return False

        return True


    @staticmethod
    def transporter_times_limit_set(transporter,time,times,order) :
        counter = 0
        if time == "rooz" :
            for datetimes in transporter.reserves_datetime_list :
                if datetimes.day == order._date_time.day :
                    counter += 1

            transporter._times_limiter[order._date_time + datetime.timedelta(1)] = [times,counter]
        elif time == "hafte" :
            for datetimes in transporter._reserves_datetime_list :
                aweek = datetime.timedelta(7)
                begin = datetimes - aweek
                end = datetimes
                if begin <= order._date_time <= end :
                    counter += 1

            transporter._times_limiter[order._date_time + datetime.timedelta(7)] = [times,counter]
        elif time == "maah" :
            for datetimes in transporter._reservers_datetime_list :
                if datetimes.month == order._date_time.month :
                    counter += 1

            transporter._times_limiter[order._date_time + datetime.timedelta(30)] = [times,counter]

        

        else :
            raise SystemError
        

        return counter


    @staticmethod
    def transporter_time_limit_check(transporter,order) :
        for time in transporter._time_limiter :
            if time <= order._date_time.time() <= transporter._time_limiter[time] :
                return False

        return True
    
    @staticmethod
    def level_finder(order) :
        if order._level == 0 :
            return "Normal"
        else :
            return f"VIP{order._level}"

    @staticmethod
    def person_vip_validation(order) :
        for user in person.users :
            if user._user_id == order._user_id :
                for ticket in user._tickets :
                    if ticket._level >= 0 :
                        return True
        return False

    @staticmethod
    def quick_way_transporter_check(transporter,order) :
        if transporter._origin == order._origin and transporter._destination == order._destination    :
            return True
        
        return False

    @staticmethod
    def sit_check(transporter,order_class) :
        try :
            if order_class in transporter._sits :
                if transporter._sits[order_class] > 0 :
                    return True
            return False
        except AttributeError :
            if isinstance(transporter,staged_vips) :
                return True

            return False

    @staticmethod
    def staged_vips_cancelation(order) :
        for staged_vip in staged_vips.staged_vips_list :
            if staged_vip == order :
                return True
            
        return False
    
    @staticmethod
    def staged_vips_reservation(order) :
        for staged_vip in staged_vips.staged_vips_list :
            if staged_vip._level == order._level and staged_vip._vehicle_model == staged_vip._vehicle_model and staged_vip._origin == order._origin and staged_vip._destination == order._destination:

                return staged_vip
        
        return False
    
    @staticmethod
    def thirty_days_vip_check(order) :
        for user in person.users :
            if user._user_id == order._user_id :
                if order._date_time - user._last_buy_date_time < datetime.timedelta(30) :
                    return True
                
        return False
    
    @staticmethod
    def vehicle_end_date_checker(order) :
        for transporter in vehicle.vehicles :
            if transporter._date_time < order._date_time :
                vehicle.vehicles.remove(transporter)

        for transporter in vehicle.vehicles :

            for limitation in transporter._times_limiter :
                if limitation <= order._date_time :
                    transporter._times_limiter.pop(limitation)
                    break

    @staticmethod
    def tickets_existing_validation(order) :
        for user in person.users :
            if user._user_id == order._user_id :
                for ticket in user._tickets :
                    if ticket._origin == order._origin and ticket._destination == order._destination and ticket._level == order._level and ticket._vehicle_model == order._vehicle_model :
                        for transporter in vehicle.vehicles :
                            if transporter == order :
                                if transporter._date_time >= order._date_time :

                                    return [user,ticket,transporter]
                                else :
                                    return False
        
        return False
    
    @staticmethod
    def one_hour_check(user,order) :
        try :
            if order._date_time - user._last_cancel < datetime.timedelta(0,3600) :
                return False
            return True
        except TypeError :
            return True

    @staticmethod
    def user_cancel_changes(user,order,ticket,vip_cancelation = False) :
        if vip_cancelation == False :
            for transporter in vehicle.vehicles :
                if transporter == order :
                    transporter._sits[order._level] += 1
                    transporter._reservers.remove(ticket)
                    

        user._last_cancel = order._date_time
        user._tickets.remove(ticket)
        
        



try :
    n = int(input())
except ValueError :
    print("Error")
    exit()

try :
    for i in range(n) :
        vehicle(*input().split())
except ValueError :
    print("Error")
    exit()
except TypeError :
    print("Error")
    exit()

print("Done")


try :
    n = int(input())
    for i in range(n) :
        entry = input().split()
        try :
            Order(*entry) 
        except TypeError :
            order_laws(entry)
except ValueError :
   print("Error")
   exit()
    

try :
    for order in Order.orders :
        execution.main_executioner(order)
except ValueError :
    print("Error")
    exit()

try :
    for order in Order.orders_not_sorted :
     
        print(order._answer)
except ValueError :
    print("Error")
    exit()


try :
    for order in Order.orders_not_sorted :
     
        print(order._answer)
except ValueError :
    print("Error")
    exit()

#for transporter in vehicle.vehicles :

    #print(transporter)

#for order in Order.orders :
    #print(order)

