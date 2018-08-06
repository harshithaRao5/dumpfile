"""# Functions | Assignment-1 - Paying Debt off in a Year
# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the
# credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#For each month, calculate statements on the monthly payment and remaining balance.At the end
# of 12 months, print out the remaining
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135
#So your program only prints out one thing: the remaining balance at
# the end of the year in the format:
# Remaining balance: 4784.0"""

def paying_debt_offinayear(balance, annual_interest_rate, monthly_payment_rate):
    """# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = \
#(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)"""
    monthly_interest_rate = (annual_interest_rate)/12.0
    updated_balance = balance
    i = 1
    while i <= 12:
        minimum_monthly_payment = monthly_payment_rate * updated_balance
        monthly_unpaid_balance = updated_balance - minimum_monthly_payment
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        i += 1
    print("Remaining balance:", round(updated_balance, 2))
def main():
    """#main function call"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debt_offinayear(data[0], data[1], data[2])
if __name__ == "__main__":
    main()
