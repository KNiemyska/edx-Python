#Write a function that calculates and returns the monthly payments for a loan.
#This function accepts three parameters in the exact order
#(principal, annual_interest_rate, duration):
def monthly_payments_for_loan (x,y,z):
    principal=abs(float(x))
    annual_interest_rate=float(y/100)
    duration=int(z)
    r=annual_interest*12 #monthly interest rate
    n=duration*12 #total number of monthly payments for the entire duration of the loan
    monthly_payment=principal*((r*(1+r)**n)/((1+r)**n-1))
    if r==0:
     monthly_payment=principal/n
            
 return monhtly_payment
