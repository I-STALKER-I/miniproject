import unittest
import importlib
import mdmntest
class testmdmn(unittest.TestCase) :
   
    def setUp(self) :
      pass

    def test_1(self) :
        

        mdmntest.vehicle(*["Train" ,"Tehran","Rasht" ,"1402/03/06-08:00 " ,'2','1','1'])
        mdmntest.vehicle(*["Airplane" ,"Tehran","Rasht" ,"1402/02/24-21:00 " ,'2','2','1','3'])
        mdmntest.vehicle(*["Airplane" ,"Tehran","urmia" ,"1402/02/25-21:00 " ,'6','2','1','3'])


        order_1 =  mdmntest.Order(*["1402/01/05-10:35", "4","Tehran","Rasht","Airplane","20"])
        order_2 = mdmntest.Order(*["1402/01/05-10:56", "3","Tehran","urmia","Airplane","56",'1']) 
        order_3 = mdmntest.Order(*["1402/01/05-11:35", "3","Tehran","Rasht","Train","56",'0']) 
        order_4 = mdmntest.Order(*["1402/01/06-02:35", "4","Tehran","Rasht","Airplane","48",'1']) 
        order_5 = mdmntest.Order(*["1402/01/07-10:56", "3","Tehran","rasht","Airplane","1","cancel"])
        order_6 = mdmntest.Order(*["1402/01/07-11:45", "3","Tehran","Rasht","Airplane",'1',"cancel"])
        order_7 = mdmntest.Order(*["1402/01/07-12:34", "3","Tehran","Rasht","TrAiN","0","cancel"])
        order_8 = mdmntest.Order(*["1402/01/08-11:35", "4","Tehran","Rasht","Airplane","1",'cancel'])
        order_9 = mdmntest.Order(*["1402/01/08-06:35","3","Tehran","Rasht","Airplane","32",'1'])
        order_10 = mdmntest.Order(*["1402/01/08-10:56", "5","Tehran","urmia","20"])
        order_11 = mdmntest.Order(*["1402/01/16-07:05", "5","Tehran","Rasht","Train","55",'1']) 
        order_12 = mdmntest.order_laws("1402/01/18-09:25 Reserve train baraye afrad balaye 50 sal mamnoo ast.".split())
        order_13 = mdmntest.Order(*["1402/01/21-17:21", "4","Tehran","Rasht","airplane","55",])
        order_14 = mdmntest.Order(*["1402/01/27-19:38", "5","Tehran","Rasht","Train","48","1"])
        order_15 = mdmntest.Order(*["1402/02/22-23:15", "5","Tehran","Rasht","Train","1","cancel"])
        order_16 = mdmntest.Order(*["1402/02/23-23:15", "5","Tehran","Rasht","Train","55","1"])




        mdmntest.execution.main_executioner(order_1)
        mdmntest.execution.main_executioner(order_2)
        mdmntest.execution.main_executioner(order_3)
        mdmntest.execution.main_executioner(order_4)
        mdmntest.execution.main_executioner(order_5)
        mdmntest.execution.main_executioner(order_6)
        mdmntest.execution.main_executioner(order_7)
        mdmntest.execution.main_executioner(order_8)
        mdmntest.execution.main_executioner(order_9)
        mdmntest.execution.main_executioner(order_10)
        mdmntest.execution.main_executioner(order_11)
        mdmntest.execution.main_executioner(order_12)
        mdmntest.execution.main_executioner(order_13)
        mdmntest.execution.main_executioner(order_14)
        mdmntest.execution.main_executioner(order_15)
        mdmntest.execution.main_executioner(order_16)


        self.assertEqual(order_1._answer,"Reserve karbar 4 baraye belit airplane model Normal movafagh bood.")
        self.assertEqual(order_2._answer,"Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid.")
        self.assertEqual(order_3._answer,"Reserve karbar 3 baraye belit train model Normal movafagh bood.")
        self.assertEqual(order_4._answer,"Reserve karbar 4 baraye belit airplane model VIP1 movafagh bood.")
        self.assertEqual(order_5._answer ,"Na Movafagh. Reserve vojood nadarad.")
        self.assertEqual(order_7._answer,f"Reserve karbar {order_7._user_id} baraye {order_7._vehicle_model} ba movafaghiat cancel shod.‍‍")
        self.assertEqual(order_8._answer,f"Darkhast cancel reserve karbar {order_8._user_id} baraye belit {order_8._vehicle_model} VIP{order_8._level} sabt shod.",)
        self.assertEqual(order_9._answer,"Reserve karbar 3 baraye belit airplane model VIP1 movafagh bood. Hamchenin Reserve karbar 4 baraye in belit cancel shod.")
        self.assertEqual(order_10._answer,f"Reserve karbar {order_10._user_id} baraye belit {order_10._vehicle_model} model Normal movafagh bood.")
        self.assertEqual(order_11._answer,f"Reserve karbar {order_11._user_id} baraye belit {order_11._vehicle_model} model VIP{order_11._level} movafagh bood.")
        self.assertEqual(order_12._answer,"Qanoon shomareye 1 ba movafaghiat sabt shod.\nReserve karbar 5 baraye train model VIP1 be dadil qanoon 1 cancel shod.")
        self.assertEqual(order_13._answer,"Reserve karbar 4 baraye belit airplane model Normal movafagh bood.")
        self.assertEqual(order_14._answer,"Reserve karbar 5 baraye belit train model VIP1 movafagh bood.")
        self.assertEqual(order_15._answer,"Darkhast cancel reserve karbar 5 baraye belit train VIP1 sabt shod.")
        self.assertEqual(order_16._answer,"Na Movafagh. Emkan reserve vojood nadarad.")


    def test_2(self) :
        importlib.reload(mdmntest)


        mdmntest.vehicle(*["Train" ,"Tehran","Rasht" ,"1402/03/06-08:00 " ,'5','2','1','1'])
        mdmntest.vehicle(*["airplane" ,"Tehran","Rasht" ,"1402/03/07-04:32 " ,'6','3','1','1','1'])
        mdmntest.vehicle(*["Airplane" ,"Qom","mashhad" ,"1402/02/24-21:00 " ,'2','1','1'])


        order_1 =  mdmntest.Order(*["1402/01/05-10:35", "10","Tehran","Masht","Airplane","32"])
        order_2 = mdmntest.Order(*["1402/01/06-12:45", "11","Tehran","Rasht","Train","56",'3'])
        order_3 = mdmntest.Order(*["1402/01/06-16:53", "12","Tehran","Rasht","Train","48",'1'])
        order_4 = mdmntest.Order(*["1402/01/07-09:12", "13","Tehran","Rasht",'32','3'])
        order_5 = mdmntest.Order(*["1402/01/07-14:50", "13","Tehran","Rasht",'Train','33','0'])
        order_6 = mdmntest.Order(*["1402/01/08-23:01", "13","Tehran","Rasht",'33','3'])
        order_7 = mdmntest.Order(*["1402/01/08-23:01", "13","Tehran","Rasht","airplane",'3','cancel'])
        order_8 =  mdmntest.Order(*["1402/01/08-23:45", "10","Tehran","Rasht","Airplane","34","3"])
        order_9 = mdmntest.Order(*["1402/01/08-23:33", "13","Tehran","Rasht","train",'cancel'])
        order_10 = mdmntest.Order(*["1402/01/09-23:33", "8","Tehran","Sari","train",'cancel'])
        order_11 = mdmntest.Order(*["1402/01/10-23:45", "13","Tehran","Rasht","airplane",'3','cancel'])
        order_12 = mdmntest.Order(*["1402/01/12-04:45", "2","Qom","mashhad","airplane",'23'])
        order_13 = mdmntest.Order(*["1402/01/13-06:45", "5","Qom","mashhad","airplane",'26'])
        order_14 = mdmntest.Order(*["1402/01/13-08:45", "6","Qom","mashhad","airplane",'26'])
        order_15 = mdmntest.Order(*["1402/01/13-09:53", "2","Qom","mashhad","45","1"])
        order_16 = mdmntest.Order(*["1402/01/13-10:57", "5","Qom","mashhad","airplane","47","1"])
        order_17 = mdmntest.Order(*["1402/01/14-01:58", "2","Qom","mashhad","airplane","1",'cancel'])
        order_18 = mdmntest.Order(*["1402/01/14-05:03", "7","Qom","mashhad","airplane","0"])
        order_19 = mdmntest.Order(*["1402/01/14-07:03", "7","Tehran","Rasht","train","0"])
        order_20 = mdmntest.Order(*["1402/02/25-07:03", "7","Qom","Mashhad","airplane","34","1"])


        mdmntest.execution.main_executioner(order_1)
        mdmntest.execution.main_executioner(order_2)
        mdmntest.execution.main_executioner(order_3)
        mdmntest.execution.main_executioner(order_4)
        mdmntest.execution.main_executioner(order_5)
        mdmntest.execution.main_executioner(order_6)
        mdmntest.execution.main_executioner(order_7)
        mdmntest.execution.main_executioner(order_8)
        mdmntest.execution.main_executioner(order_9)
        mdmntest.execution.main_executioner(order_10)
        mdmntest.execution.main_executioner(order_11)
        mdmntest.execution.main_executioner(order_12)
        mdmntest.execution.main_executioner(order_13)
        mdmntest.execution.main_executioner(order_14)
        mdmntest.execution.main_executioner(order_15)
        mdmntest.execution.main_executioner(order_16)
        mdmntest.execution.main_executioner(order_17)
        mdmntest.execution.main_executioner(order_18)
        mdmntest.execution.main_executioner(order_19)
        mdmntest.execution.main_executioner(order_20)


        self.assertEqual(order_1._answer,"Na Movafagh. Masir vojood nadarad.")
        self.assertEqual(order_2._answer,"Na Movafagh. Zarfiat vojood nadarad.")
        self.assertEqual(order_3._answer,"Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid.")
        self.assertEqual(order_4._answer,"Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid.")
        self.assertEqual(order_5._answer,'Reserve karbar 13 baraye belit train model Normal movafagh bood.')
        self.assertEqual(order_6._answer,'Reserve karbar 13 baraye belit airplane model VIP3 movafagh bood.')
        self.assertEqual(order_7._answer,f"Darkhast cancel reserve karbar {order_7._user_id} baraye belit {order_7._vehicle_model} VIP{order_7._level} sabt shod.")
        self.assertEqual(order_8._answer,"Na Movafagh. Shoma reserve qabli nadarid va nemitavanid VIP reserve konid.")
        self.assertEqual(order_9._answer,"Na Movafagh. Shoma dar 1 sa'at akhir darkhast cancel dashtid.")
        self.assertEqual(order_10._answer,"Na Movafagh. Reserve vojood nadarad.")
        self.assertEqual(order_11._answer,"Na Movafagh. Darkhast cancel shoma qablan sabt shode ast.")
        self.assertEqual(order_12._answer,'Reserve karbar 2 baraye belit airplane model Normal movafagh bood.')
        self.assertEqual(order_13._answer,'Reserve karbar 5 baraye belit airplane model Normal movafagh bood.')
        self.assertEqual(order_14._answer,'Na Movafagh. Zarfiat vojood nadarad.')
        self.assertEqual(order_15._answer,'Reserve karbar 2 baraye belit airplane model VIP1 movafagh bood.')
        self.assertEqual(order_16._answer,"Na Movafagh. Zarfiat vojood nadarad.")
        self.assertEqual(order_17._answer,f"Darkhast cancel reserve karbar {order_17._user_id} baraye belit {order_17._vehicle_model} VIP{order_17._level} sabt shod.")
        self.assertEqual(order_18._answer,"Na Movafagh. Zarfiat vojood nadarad.")
        self.assertEqual(order_19._answer,"Reserve karbar 7 baraye belit train model Normal movafagh bood.")
        self.assertEqual(order_20._answer,"Na Movafagh. Masir vojood nadarad.")

    def test_3(self) :
        importlib.reload(mdmntest)

        vehicle_1 = mdmntest.vehicle(*["Train" ,"Tehran","Rasht" ,"1402/02/06-08:00 " ,'5','2','2','2'])
        vehicle_2 = mdmntest.vehicle(*["airplane" ,"Yasoj" ,"Khorramabad" ,"1402/02/07-09:15" ,'5'])



        order_1 = mdmntest.Order(*["1402/01/05-10:35", "1","Tehran","Rasht","Train","32"])
        order_2 = mdmntest.Order(*["1402/01/06-12:45", "2","Tehran","Rasht","Train","56"])
        order_3 = mdmntest.Order(*["1402/01/06-16:53", "3","Tehran","Rasht","Train","32"])
        order_4 = mdmntest.Order(*["1402/01/07-09:12", "1","Tehran","Rasht",'52','1'])
        order_5 = mdmntest.Order(*["1402/01/07-14:50", "2","Tehran","Rasht",'Train','45','1'])
        order_6 = mdmntest.Order(*["1402/01/08-23:01", "3","Tehran","Rasht",'55','2'])
        order_7 = mdmntest.order_laws("1402/01/10-23:13 Zarfiat reserve baraye train be 50 darsad taghir kard.".split())
        order_8 = mdmntest.Order(*["1402/01/08-23:01", "1","Tehran","Rasht",'train','cancel'])
        order_9 = mdmntest.Order(*["1402/01/09-12:01", "5","Tehran","Rasht",'train',"32"])
        order_10 = mdmntest.order_laws("1402/01/10-12:21 Reserve train baraye afrad balaye 50 sal mamnoo ast.".split())
        order_11 = mdmntest.order_laws("1402/01/10-23:13 Reserve airplane dar sa'at 8 ta 12 momken nist.".split())
        order_12 = mdmntest.Order(*["1402/01/11-08:04", "6","Yasoj","Khorramabad",'airplane',"32"])
        order_13 = mdmntest.Order(*["1402/01/11-13:04", "6","Yasoj","Khorramabad",'airplane',"56"])
        order_14 = mdmntest.Order(*["1402/01/11-13:07", "9","Yasoj","Khorramabad",'airplane',"62"])
        order_15 = mdmntest.order_laws("1402/01/11-21:15 Emkan reserve baraye airplane bish az 2 bar dar rooz momken nist.".split())
        order_16 = mdmntest.Order(*["1402/01/11-13:30", "3","Yasoj","Khorramabad",'airplane',"21"])
        order_17 = mdmntest.Order(*["1402/01/12-13:30", "3","Yasoj","Khorramabad",'airplane',"21"])
        order_18 =  mdmntest.Order(*["1402/01/12-18:30", "8","Yasoj","Khorramabad",'airplane',"21"])
        order_19 =  mdmntest.Order(*["1402/01/12-19:30", "10","Yasoj","Khorramabad",'airplane',"21"])


        mdmntest.execution.main_executioner(order_1)
        mdmntest.execution.main_executioner(order_2)
        mdmntest.execution.main_executioner(order_3)
        mdmntest.execution.main_executioner(order_4)
        mdmntest.execution.main_executioner(order_5)
        mdmntest.execution.main_executioner(order_6)
        mdmntest.execution.main_executioner(order_7)
        mdmntest.execution.main_executioner(order_8)
        mdmntest.execution.main_executioner(order_9)
        mdmntest.execution.main_executioner(order_10)
        mdmntest.execution.main_executioner(order_11)
        mdmntest.execution.main_executioner(order_12)
        mdmntest.execution.main_executioner(order_13)
        mdmntest.execution.main_executioner(order_14)
        mdmntest.execution.main_executioner(order_15)
        mdmntest.execution.main_executioner(order_16)
        mdmntest.execution.main_executioner(order_17)
        mdmntest.execution.main_executioner(order_18)
        mdmntest.execution.main_executioner(order_19)



        self.assertEqual(order_1._answer,'Reserve karbar 1 baraye belit train model Normal movafagh bood.')
        self.assertEqual(order_2._answer,'Reserve karbar 2 baraye belit train model Normal movafagh bood.')
        self.assertEqual(order_3._answer,'Reserve karbar 3 baraye belit train model Normal movafagh bood.')
        self.assertEqual(order_4._answer,'Reserve karbar 1 baraye belit train model VIP1 movafagh bood.')
        self.assertEqual(order_5._answer,'Reserve karbar 2 baraye belit train model VIP1 movafagh bood.')
        self.assertEqual(order_6._answer,'Reserve karbar 3 baraye belit train model VIP2 movafagh bood.')
        self.assertEqual(order_7._answer,"Qanoon shomareye 1 ba movafaghiat sabt shod.\nReserve karbar 3 baraye train model Normal be dadil qanoon 1 cancel shod.\nReserve karbar 2 baraye train model VIP1 be dadil qanoon 1 cancel shod.")
        self.assertEqual(vehicle_1._const_sits,{0 : 2,1:1 , 2:1})
        self.assertEqual(order_8._answer,f"Reserve karbar {order_8._user_id} baraye {order_8._vehicle_model} ba movafaghiat cancel shod.‍‍")
        self.assertEqual(order_9._answer,'Reserve karbar 5 baraye belit train model Normal movafagh bood.')
        self.assertEqual(order_10._answer,"Qanoon shomareye 2 ba movafaghiat sabt shod.\nReserve karbar 3 baraye train model VIP2 be dadil qanoon 2 cancel shod.\nReserve karbar 2 baraye train model Normal be dadil qanoon 2 cancel shod.")
        self.assertEqual(order_11._answer,"Qanoon shomareye 3 ba movafaghiat sabt shod.")
        self.assertEqual(order_12._answer,"Na Movafagh. Emkan reserve vojood nadarad.")
        self.assertEqual(order_13._answer,'Reserve karbar 6 baraye belit airplane model Normal movafagh bood.')
        self.assertEqual(order_14._answer,'Reserve karbar 9 baraye belit airplane model Normal movafagh bood.')
        self.assertEqual(order_15._answer,"Qanoon shomareye 4 ba movafaghiat sabt shod.")
        self.assertEqual(order_16._answer,"Na Movafagh. Emkan reserve vojood nadarad.")
        self.assertEqual(order_17._answer,"Reserve karbar 3 baraye belit airplane model Normal movafagh bood.")
        self.assertEqual(order_18._answer, 'Reserve karbar 8 baraye belit airplane model Normal movafagh bood.')
        self.assertEqual(order_19._answer, "Na Movafagh. Emkan reserve vojood nadarad.")






    def test_vehicles(self) :
       
        vehicle_1 = mdmntest.vehicle(*["Train" ,"Tehran","Rasht" ,"1402/03/06-08:00 " ,'6','3','4','5','3'])
        vehicle_2 = mdmntest.vehicle(*["AiRPLAne" ,"Tehran","Rasht" ,"1402/03/21-09:01 " ,'2','1','1'])
        vehicle_3 = mdmntest.vehicle(*["Train" ,"Mashhad","Qom" ,"1402/03/23-10:21 " ,'6','0'])
        vehicle_4 = mdmntest.vehicle(*["TRaIn" ,"Rasht","BandarAbbas" ,"1402/03/23-12:21" ,'10','5','1','1','1','1','1'])
        vehicle_5 = mdmntest.vehicle(*["airPlanE" ,"Tehran","Rasht" ,"1402/03/23-14:23 " ,'4','2','1','1'])


        self.assertEqual(vehicle_1._vehicle_model,"train")
        self.assertEqual(vehicle_1._sits,{0:6, 1:4, 2:5, 3:3})

        self.assertEqual(vehicle_2._vehicle_model,"airplane")
        self.assertEqual(vehicle_2._sits,{0:2, 1:1})

        self.assertEqual(vehicle_3._vehicle_model,"train")
        self.assertEqual(vehicle_3._sits,{0:6})

        self.assertEqual(vehicle_4._vehicle_model,"train")
        self.assertEqual(vehicle_4._sits,{0:10, 1:1, 2:1, 3:1 ,4:1 ,5:1})

        self.assertEqual(vehicle_5._vehicle_model,"airplane")
        self.assertEqual(vehicle_5._sits,{0:4, 1:1, 2:1})

    def test_orders(self) :
        order_1 = mdmntest.Order(*["1402/01/05-10:35", "4","Tehran","Rasht","20"])
        order_2 = mdmntest.Order(*["1402/01/05-10:56", "2","Tehran","Qom","airplane",'1',"cancel"]) 
        order_3 = mdmntest.Order(*["1402/01/05-11:35", "3","Bandarabbas","abadan","Train","cancel"]) 
        order_4 = mdmntest.Order(*["1402/01/06-02:35", "4","bandartorkaman","qazvin","Airplane","48",'1']) 
        order_5 = mdmntest.Order(*["1402/01/07-10:56", "3","sari","babolsar","Airplane","48"])
        order_6 = mdmntest.Order(*["1402/01/07-10:56", "5","mashhad","shiraz","48","1"])

        self.assertEqual(order_1._origin,"Tehran")
        self.assertEqual(order_1._destination,"Rasht")
        self.assertEqual(order_1._user_id,4)
        self.assertEqual(order_1._vehicle_model,None)
        self.assertEqual(order_1._level,0)
        self.assertEqual(order_1._rule,"quickway")
        self.assertEqual(order_1._age,20)

        self.assertEqual(order_2._origin,"Tehran")
        self.assertEqual(order_2._destination,"Qom")
        self.assertEqual(order_2._user_id,2)
        self.assertEqual(order_2._vehicle_model,"airplane")
        self.assertEqual(order_2._level,1)
        self.assertEqual(order_2._rule,"cancel")

        self.assertEqual(order_3._origin,"Bandarabbas")
        self.assertEqual(order_3._destination,"abadan")
        self.assertEqual(order_3._user_id,3)
        self.assertEqual(order_3._vehicle_model,"train")
        self.assertEqual(order_3._level,0)
        self.assertEqual(order_3._rule,"cancel")

        self.assertEqual(order_4._origin,"bandartorkaman")
        self.assertEqual(order_4._destination,"qazvin")
        self.assertEqual(order_4._user_id,4)
        self.assertEqual(order_4._vehicle_model,"airplane")
        self.assertEqual(order_4._level,1)
        self.assertEqual(order_4._rule,"reserve")
        self.assertEqual(order_4._age,48)

        self.assertEqual(order_5._origin,"sari")
        self.assertEqual(order_5._destination,"babolsar")
        self.assertEqual(order_5._user_id,3)
        self.assertEqual(order_5._vehicle_model,"airplane")
        self.assertEqual(order_5._level,0)
        self.assertEqual(order_5._rule,"reserve")
        self.assertEqual(order_5._age,48)

        self.assertEqual(order_6._origin,"mashhad")
        self.assertEqual(order_6._destination,"shiraz")
        self.assertEqual(order_6._user_id,5)
        self.assertEqual(order_6._vehicle_model,None)
        self.assertEqual(order_6._age ,48)
        self.assertEqual(order_6._rule,"quickway")
        self.assertEqual(order_6._level,1)
        

       



if __name__ == '__main__' :
   unittest.main()
