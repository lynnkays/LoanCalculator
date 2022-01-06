#!/usr/bin/python
# -*- coding: utf-8 -*-
print('Welcome to the loan payment calculator!\n')
principle = input('Please enter the principle amount of your loan:  ')
if principle[0:1] == '$':
    principle = float(principle[1:])
else:
    principle = float(principle)

rate = input('Please enter the interest rate of your loan:  ')
if rate[-1] == '%':
    rate = float(rate[:-1]) / 100
else:
    rate = float(rate)

years = \
    int(input('Please enter the number of years you have to pay off this loan:  '
        ))
annual_income = input('Please enter your annual income:  ')
if annual_income[0:1] == '$':
    annual_income = float(annual_income[1:])
else:
    annual_income = float(annual_income)

annual_payment = (1 + rate) ** years * principle * rate / ((1 + rate)
        ** years - 1)
monthlypayment = annual_payment / 12

print '\nYour annual payment is ${:,.2f}'.format(annual_payment)
print 'Your monthly payment is ${:,.2f}'.format(monthlypayment)
print 'The total amount you will pay for the life of the loan is ${:,.2f}\n'.format(annual_payment
        * years)

if monthlypayment > annual_income / 12:
    if rate > .05:
        print "It doesn't look like you can afford this loan, you should refinance"
    else:
        print 'You should seek financial counseling before acquiring this loan.'
else:
    print 'Everything looks great! You should be able to afford this loan and get it paid off in time!'
