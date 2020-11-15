import datetime as dt

class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount ## денежная сумма или количество килокалорий
        self.date = date
        self.comment = comment
       
    ##def __str__ (self):
     ##   print (f'{self.amount}')

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.amount = 0
        self.date = 0
        self.comment = 0
        self.records = []
        self.new_record = 0
        

    def add_record(self, new_record): ##Сохраняет новую запись о расходах 
        self.new_record = Record(self.amount,self.date,self.comment)
        self.records.append(self.new_record)
        ##print(self.records)
        ##new_record_sring =','.join(self.new_record)
        
    def __str__(self):
        print (', '.join(self.records))



    
    ##def get_today_stats(self,limit,amount): ## Считает сколько денег потрачено сегодня, дату прописывать не нужно тк СЕГОДНЯ
   
        

##class CashCalculator:
    ##def __init__(self,limit,amount,unit,date,comment):
        ##self.limit = limit
        ##self.amount = amount
        ##self.unit = unit
        ##self.date = date
        ##self.comment = comment
    
  
    
        

    ##def get_today_cash_remained(currency): ## Определяет сколько ещё денег можно потратить сегодня в рублях, долларах или евро
       ## USD_RATE = 77,39
      ##  EURO_RATE = 91,58
        
        ##if currency = USD, тогда 
           ## return остаток = лимит - потрачено *77,39
       # elif если currency = EURO, тогда
        #     return остаток = лимит = потрачено * 91,58
       # else:
           # return остаток = лимит - потрачено


        ##get_week_stats(): ## Считает сколько денег потрачено за последние 7 дней

##class CaloriesCalculator(Calculator):

    ##add_record(): ##Сохраняет новую запись о приеме пищи 

    ##get_today_stats(): ## Считает сколько пищи съедено сегодня

    ##get_calories_remained(): ## Определяет сколько ещё калорий можно/нужно получить сегодня

    ##get_week_stats(): ## Считает сколько калорий получено за последние 7 дней





calc = Calculator(1000)
##r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
##r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
##r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

calc.add_record(Record(amount=145, comment="Безудержный шопинг", date="08.03.2019"))
calc.add_record(Record(amount=156, comment="Наполнение потребительской корзины", date="09.03.2019"))
calc.add_record(Record(amount=691, comment="Катание на такси", date="08.03.2019"))




