# mortgage.py
#
# Exercise 1.7/1.8/1.9/1.10/1.11/1/12

extra_payment_start_month = 61
extra_payment_end_month = extra_payment_start_month + (12 * 4) 
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 1 

while principal > 0:
    extra = 0
    if extra_payment_start_month <= month < extra_payment_end_month:
        extra = extra_payment

    principal = principal * (1+rate/12)

    monthly_payment = payment + extra

    if monthly_payment > principal:
        monthly_payment = principal

    principal = principal - monthly_payment

    total_paid = total_paid + monthly_payment 

    print(f'{month} {total_paid:0.2f} {principal:0.2f}')
    month = month + 1

print(f'Total paid: {total_paid: 0.2f}')
print(f'Months: {month - 1}')

# 1.9
# Total paid 880074.1
# Months: 310

# 1.12
# Since the false string is not empty we get True