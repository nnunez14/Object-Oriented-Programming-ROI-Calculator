class returnOnInvestment:

    def __init__(self, income = 0, expenses = 0, cash_flow = 0, cash_cash_roi = 0):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.cash_cash_roi = cash_cash_roi

    def monthly_expenses(self):
        print('Please enter your monthly expenses: ')
    #In this method, I am making it to where The answers given in the input will be converted into a interget
    def convert_int(self, num):
        num = num.strip('$ ').replace(',', '')
        while not num.isnumeric():
            num = input("That entry is not correct. Please enter an number: ")
            num = num.strip('$ ').replace(',', '')
        return int(num)


    #This method is gathering the total monthly income 
    def roiIncome(self):
        monthly_income = self.convert_int(input("What is your monthly rental income? "))
        add_income = self.convert_int(input("What is the amount of your additional income? (If none, put 0) "))
        self.income = monthly_income + add_income
        return self.income


    #This method is gathering the total monthly expenses
    def roiExpenses(self):
        mortgage = self.convert_int(input("What are your monthly mortgage payments? "))
        insurance = self.convert_int(input("What are your monthly insurance costs? "))
        taxes = self.convert_int(input("What are your monthly taxes? "))
        utilites = self.convert_int(input("What are your monthly utilites expenses? (Electric, garbage, water, etc) "))
        additional_expenses = self.convert_int(input("What are your additional expenses? (If none, put 0) "))
        self.expenses = mortgage + insurance + taxes + utilites + additional_expenses
        return self.expenses
    

    #This method is the cash flow, which is just the money you have after your expenses are taken out of your income
    def roiCashFlow(self):
        self.cash_flow = self.income - self.expenses
        return self.cash_flow


    #This method is the investment that you put into the property at the beginning
    def roiCashOnCash(self):
        down_payment = self.convert_int(input("What is your Down Payment on this property? "))
        closing = self.convert_int(input("What are your closing costs? "))
        rehab = self.convert_int(input("What is your rehab budget? (budget for the repairs on the property) " ))
        additional = self.convert_int(input("Is there any additonal money you have spent for this property?  (If none, put 0) " ))
        self.cash_cash_roi = down_payment + closing + rehab + additional
        return self.cash_cash_roi


    # This method shows the final return on investment equation
    def roi(self):
        total_cash_flow = (self.income - self.expenses) * 12
        return f'{(total_cash_flow / self.cash_cash_roi) * 100}%'


def run():
    #This part runs through the income and collects it
    roi = returnOnInvestment()
    print("Enter the necessary information to find your ROI on your rental property. ")
    print("\nFirst, we will go over your income. \n")
    roi.roiIncome()
    
    #This part runs through the expenses, and collects it
    print("\nThank you for that information, now we will be going over your expenses. \n")
    roi.roiExpenses()

    #This part runs through the cash on cash/investments, and collects it
    print("\nThank you, just a little bit more. Now, we will be going over your total investment into your rental property. \n")
    roi.roiCashOnCash()

    #This part collects and gives the Return on investment
    print(f'\nThank you for all your information. Your ROI is {roi.roi()}. \nThank you for working with us, good luck making bank. ')
    roi.roi()

run()
