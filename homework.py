import datetime as dt


##class Calculator:

    ##self.records = []
   
    


class Record:
    def __init__(self,amount,unit,date,comment):
        self.amount = amount ## денежная сумма или количество килокалорий
        self.unit = unit
        self.date = date
        self.comment = comment
        self.new_record = 0
        
    

    def add_record(self, new_record): ##Сохраняет новую запись о расходах 
        self.records = []
        self.new_record = new_record
        ##self.unit = unit
        if self.unit == 'kal':
           print ('Вам в другой калькулятор')
        elif self.unit == 'rub':
            self.records.append(self.new_record)
        
        print(self.records)

        

    
class CashCalculator:
    def __init__(self,limit,amount,unit,date,comment):
        self.limit = limit
        self.amount = amount
        self.unit = unit
        self.date = date
        self.comment = comment
    
  
    def get_today_stats(self,limit,amount): ## Считает сколько денег потрачено сегодня, дату прописывать не нужно тк СЕГОДНЯ
        

    def get_today_cash_remained(currency): ## Определяет сколько ещё денег можно потратить сегодня в рублях, долларах или евро
        USD_RATE = 77,39
        EURO_RATE = 91,58
        
        if currency = USD, тогда 
            return остаток = лимит - потрачено *77,39
        elif если currency = EURO, тогда
             return остаток = лимит = потрачено * 91,58
        else:
            return остаток = лимит - потрачено


        
    
    ##get_week_stats(): ## Считает сколько денег потрачено за последние 7 дней

##class CaloriesCalculator(Calculator):

    ##add_record(): ##Сохраняет новую запись о приеме пищи 

    ##get_today_stats(): ## Считает сколько пищи съедено сегодня

    ##get_calories_remained(): ## Определяет сколько ещё калорий можно/нужно получить сегодня

    ##get_week_stats(): ## Считает сколько калорий получено за последние 7 дней






r1 = Record(amount=145, unit ="rub", comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568,unit ="rub", comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, unit ="kal", comment="Катание на такси", date="08.03.2019")

r1.add_record('145, "rub", "Безудержный шопинг","08.03.2019"')
r2.add_record('1568, "rub", "Наполнение потребительской корзины","09.03.2019"')
r3.add_record('691, "kal", "Наполнение потребительской корзины", "08.03.2019" ')



