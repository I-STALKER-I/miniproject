"""the code was a mess so i decided to do a hotfix"""
import datetime

class Order :
    """this orders list are sorted by date_time"""
    orders = []
    orders_not_sorted = []
    """we need not sorted for represntation"""

    def __init__(self ,date_time ,user_id ,origin ,destination ,vehicle_model = None ,shifter_1 = None ,shifter_2 = None) :
        """i call them shifter because they can change """
        self._origin = origin
        self._destination = destination
        self._date_time = date_time
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
        else :
            self.level = int(shifters[0])

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
        return f"{self._date_time} ,{self._origin} ,{self._destination} ,{self._vehicle_model} ,{self._level} ,{self._rule}"
    


class vehicle(Order) :
    vehicles = []
    def __init__(self ,vehicle_model ,origin ,destination ,date_time ,Normal_sits ,vip_sits = None) :
        self._vehicle_model = vehicle_model
        self._origin = origin
        self._destination = destination
        self._date_time = date_time
        self._sits = [Normal_sits ,vip_sits]
        vehicle.sorts(self)

    @property
    def _sits(self) :
        return self.sits 
    
    @_sits.setter
    def _sits(self,shifters) :
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
        
        if self._origin == order._origin and self._destination == order._destination and self._vehicle_model == order._vehicle_model :
            return True
        return False
      
    
class staged_vips :
    staged_vips_list = []
    def __init__(self,previous_user,vip_class,using_vehicle,date_time) :
        self._previous_user = previous_user
        self._vip_class = vip_class
        self._vehicle_model = using_vehicle
        self._date_time = date_time
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
            if self._vip_class == order._level and self._vehicle_model == order._vehicle_model and self._previous_user == order._user_id :
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
        self._tickets.remove(ticket)

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
        else :
            raise ValueError
        
    @classmethod
    def cancelation(cls,order) :
        tickets_existing_validate = cls.tickets_existing_validation(order)
        if tickets_existing_validate == False :
            order._answer = "Na Movafagh. Reserve vojood nadarad."
        else :
            if order._level == 0 :
                cls.normal_cancelation(*tickets_existing_validate,order)
            else :
                cls.vip_cancelation(*tickets_existing_validate,order)



    @classmethod
    def normal_cancelation(cls ,user ,ticket ,order) :
        if cls.one_hour_check(user ,order) :
            cls.user_cancel_changes(user ,order ,ticket)
            order._answer = f"Reserve karbar {order._user_id} baraye {order._vehicle_model} ba movafaghiat cancel shod.‍‍"
            
        else :
            order._answer = "Na Movafagh. Shoma dar 1 sa'at akhir darkhast cancel dashtid."

 
    @classmethod
    def vip_cancelation(cls ,user ,ticket,order) :
        if cls.one_hour_check(user ,order) :
            if cls.staged_vips_cancelation(order) == False :
                    staged_vips(order._user_id,order._level,order._vehicle_model,ticket._date_time)
                    cls.user_cancel_changes(user ,order ,ticket,True)
                    order._answer = f"Darkhast cancel reserve karbar {order._user_id} baraye belit {order._vehicle_model} VIP{order._level} sabt shod."
            else :
                order._answer =  "Na Movafagh. Darkhast cancel shoma qablan sabt shode ast."
            
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
            transporter.remove(order._level)
            order._answer = f"Reserve karbar {order._user_id} baraye belit {order._vehicle_model} model Normal movafagh bood."
            return
        
    @classmethod
    def vip_reservation(cls ,order ,transporter) :
        staged_vip = cls.staged_vips_reservation(order)
        if isinstance(staged_vip,staged_vips) :
            order._answer = f"Reserve karbar {order._user_id} baraye belit model VIP{order._level} movafagh bood. Hamchenin Reserve karbar {staged_vip._previous_user} baraye in belit cancel shod."
            staged_vip.delete()
            return
        
        if cls.sit_check(transporter ,order._level) :
            if cls.thirty_days_vip_check(order) == False :
                order._answer = "Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid."
                return
            else :
                person(order._user_id,order._date_time,order)
                transporter.remove(order._level)
                
                order._answer = f"Reserve karbar {order._user_id} baraye belit {order._vehicle_model} model VIP{order._level} movafagh bood."
                return

        else :
            order._answer = "Na Movafagh. Zarfiat vojood nadarad."
            return
        
    @classmethod
    def quickway(cls,order) :
        if order._level > 0 :
            if cls.thirty_days_vip_check(order) == False :
                order._answer = "Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid."
                return   
        validation_1 = False
        validation_2 = False
        quickest_vehicle = None
        nearest_time = datetime.timedelta(6000,0)
        for transporter in vehicle.vehicles :
                if cls.quick_way_transporter_check(transporter,order) :
                    validation_1 = True
                    if cls.sit_check(transporter,order._level) :
                        validation_2 = True
                        if nearest_time > transporter._date_time - order._date_time :
                            nearest_time = transporter._date_time - order._date_time
                            quickest_vehicle = transporter
        if validation_1 == False :
            order._answer = "Na Movafagh. Masir vojood nadarad."
        elif validation_2 == False :
            order._answer = "Na Movafagh. Zarfiat vojood nadarad."
        else :
            order._vehicle_model = quickest_vehicle._vehicle_model
            order._rule = [None,None]
            cls.main_executioner(order)

    @classmethod
    def equality_check(cls,order) :

        validation_1 = False
        validation_2 = False
            
        for staged_vip in staged_vips.staged_vips_list :
            if staged_vip._vip_class == order._level and staged_vip._vehicle_model == staged_vip._vehicle_model :
                validation_1 = True
                validation_2 = True
                return staged_vip
                
        for transporter in vehicle.vehicles :
            if transporter == order :
                validation_1 = True
                if cls.sit_check(transporter,order._level) :
                    validation_2 = True
                    return transporter

        if validation_1 == False :
            order._answer = "Na Movafagh. Masir vojood nadarad."
        elif validation_2 == False :
            order._answer = "Na Movafagh. Zarfiat vojood nadarad."

        return False

    @staticmethod
    def quick_way_transporter_check(transporter,order) :
        if transporter._origin == order._origin and transporter._destination == order._destination   :
            return True
        return False

    @staticmethod
    def sit_check(transporter,order_class) :
        if order_class in transporter._sits :
            if transporter._sits[order_class] > 0 :
                return True
        return False

    @staticmethod
    def staged_vips_cancelation(order) :
        for staged_vip in staged_vips.staged_vips_list :
            if staged_vip == order :
                return True
            else :
                return False
        return False
    
    @staticmethod
    def staged_vips_reservation(order) :
        for staged_vip in staged_vips.staged_vips_list :
            if staged_vip._vip_class == order._level and staged_vip._vehicle_model == staged_vip._vehicle_model :

                return staged_vip
        
        return False
    
    @staticmethod
    def thirty_days_vip_check(order) :
        for user in person.users :
            if user._user_id == order._user_id :
                if order._date_time - user._last_buy_date_time <= datetime.timedelta(30) :
                    return True
                
        return False
    
    @staticmethod
    def vehicle_end_date_checker(order) :
        for transporter in vehicle.vehicles :
            if transporter._date_time < order._date_time :
                vehicle.vehicles.remove(transporter)

    @staticmethod
    def tickets_existing_validation(order) :
        for user in person.users :
            if user._user_id == order._user_id :
                for ticket in user._tickets :
                    if ticket._origin == order._origin and ticket._destination == order._destination and ticket._level == order._level and ticket._vehicle_model == order._vehicle_model :
                        for transporter in vehicle.vehicles :
                            if transporter == order :
                                if transporter._date_time > order._date_time :

                                    return [user,ticket]
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
        Order(*input().split()) 
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
    for order in Order.orders :
     
        print(order._answer)
except ValueError :
    print("Error")
    exit()

