principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start = 61
extra_payment_end = 108
total_paid = 0.0
month = 0
Num = 0

while principal > 0:
    if  month >= extra_payment_start and month <= extra_payment_end:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    month = month + 1
    Num = Num + 1
    
    print(Num, total_paid)

if principal < 0:
    total_paid = total_paid + principal
    principal = 0
    print(Num, total_paid, '(refunded from extra payment)')