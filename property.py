# property: class
# income: rental income, laundry income, storage income, misc
# expenses: mortgage, tax, insurance, utilities( electric, water, sewer, garbage, gas), HOA, lawn, vacnacy, repairs, cap_ex, prop_mngt,mortgage
# cash_flow :income minus total monthly cash flow
# cash_roi: down_payment, closing_costs, repair, misc

# x1 = rental_income
# rental_income = input("Enter Rental Income ")
# laundry_income = input("Enter Laundry Income ")
# x2 = laundry_income
# storage_income = input("Enter Storage Income ")
# x3 = storage_income
# misc_income = input("Enter Misc Income ")
# x4 = misc_income
# income = (x1 + x2 + x3 + x4)
# x = income
# tax_expenses = input("Enter Tax Income ")
# y1 = tax_expenses
# insurance_expenses = input("Enter Insurance Expenses ")
# y2 = insurance_expenses
# utilities_expenses = input("Enter Utility Expenses ")
# y3 = utilities_expenses
# hoa_expenses = input("Enter HOA Expenses ")
# y4 = hoa_expenses
# lawn_expenses: input("Enter Lawn Expenses ")
# y5 = lawn_expenses
# vacancy_expenses = input("Enter Vacancy Expenses ")
# y6 = vacancy_expenses
# repairs_expenses = input("Enter Repair Expenses ")
# y7 = repairs_expenses
# cap_ex_expenses = input("Enter Capital Expenses ")
# y8 = cap_ex_expenses
# prop_mngt_expenses = input("Enter Property Management Expenses ")
# y9 = prop_mngt_expenses
# mortgage_expenses = input("Enter Mortgage Expenses ")
# y10 = mortgage_expenses
# expenses = (y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10)
# y = expenses
# cash_flow = (x - y)
# a = cash_flow
# # income - expenses: x - y = a
# cash_down = input("Enter Cash Down ")
# z1 = cash_down
# cash_closing = input("Enter Cash Closing ")
# z2 = cash_closing
# cash_repair = input("Enter Cash Repair ")
# z3 = cash_repair
# cash_misc = input("Enter Cash Misc ")
# z4 = cash_misc
# total_investment = (z1 + z2 + z3 + z4)
# z = total_investment
# total_roi = (a * 12)/z
# b = total_roi

# create a user class and a property class
# the purpuse of the property class is to return the ROI
# the purpuse of the user class is to provide the value of each input

class Property:
    def __init__(self, income, expenses, investment):
        self.investment = investment
        self.incomes = []
        self.expenses = []


    def incomes(self, income_key, income_value):
        self.incomes.append(income_key, income_value)

    def expenses(self, expenses_key, expenses_value):
        self.expenses.append(expenses_key, expenses_value)

    def cash_flow(self, total_income, total_expenses):
        total_income = sum(income_value)
        total_expenses = sum(expenses_value)
        cash_flow = total_income - total_expenses

        return cash_flow
    
    def investment(self, investment_key, investment_value):
        self.investment.append(investment_key, investment_value)
        total_investment = sum(investment_value)


    def roi(self, cash_flow, total_investment):
        roi = float((cash_flow * 12) / total_investment) * 100


class User:
    def __init__(self, name):
        self.name = name
        self.properties = []
        
    def add_property(self, property):
        self.properties.append(property)


def run():
    self.users = []

    while True:
        print("\nOptions:")
        print("1. add User")
        print("2. Add a Property")
        print("3. Add an Expenses")
        print("4. Add an Income")
        print("5. Calculate ROI")
        print("6. Quit")

        response= input("What would like to do? Load/Unload/Change Driver/Check Seats/Admire Bus/Exit").lower()
        if response == "6":
            print("Thank you for visiting!")
            break
        elif response == "1":
            users.append(user)
        elif response == "change user":
            pass
        elif response == "add property":
            reponse 2 = "now it's time to input values"
            

