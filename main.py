import math
import argparse

parser = argparse.ArgumentParser(description="This program is loan calculator.")

parser.add_argument("--type", choices=['annuity', 'diff'])
parser.add_argument("--principal", )
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()
ingredients = [args.type, args.principal, args.periods, args.interest, args.payment]

def na(loan_principal, a, y):
    i = y / (12 * 100)
    total_months = math.ceil(math.log(a / (a - i * loan_principal), i + 1))
    return total_months

def ap(loan_principal, d, y):       #   annuity payment               a
    i = y / (12 * 100)
    annuity_payment = loan_principal * i * math.pow(1 + i, d) / (math.pow((1 + i), d) - 1)
    annuity_payment = math.ceil(annuity_payment)  # A
    print(f"Your monthly payment = {annuity_payment}!")
    overpayment_a = int((loan_principal - (annuity_payment * d)))
    print("Overpayment = " + str(abs(overpayment_a)))

def payment(loan_principal, d, y, m):
    p = loan_principal
    n = d
    i = y / (12 * 100)

    d1 = (p / n) + i * (p - ((p * (m - 1)) / n))
    d1 = math.ceil(d1)  # A
    return d1
def principal(annuity_payment, d, y):
    i = y / (12 * 100)
    p = annuity_payment / ((i * math.pow(1 + i, d)) / (math.pow(1 + i, d) - 1))
    return p

stop = True
how_many_none = -1
for i in ingredients:    # None two arguments
    if i == None:
        how_many_none += 1
if how_many_none > 0 or args.interest == None:
    print("Incorrect parameters.")
    stop = False

while stop:
    if args.periods == None: #  x == "n":
        loan_principal = int(args.principal)
        a = float(args.payment)
        y = float(args.interest)
        t_monts = na(loan_principal, a, y)
        if t_monts % 12 != 0:
            second = t_monts % 12
            first = int(t_monts / 12)
            print("It will take " + str(first) + " years and " + str(second) + " months to repay this loan!")
        if t_monts % 12 == 0:
            first = int(t_monts / 12)
            print("It will take " + str(first) + " to repay this loan!")
            overpayment_a = int(loan_principal - (a * t_monts))
            print("Overpayment = " + str(abs(overpayment_a)))

    if args.payment == None: # x == "a":
        loan_principal = int(args.principal)
        d = float(args.periods)
        y = float(args.interest)
        if args.type == "annuity":
            nowy = ap(loan_principal, d, y)     #  --type=annuity
        m = 0
        overpayment_a = loan_principal
        if args.type == "diff":
            for i in range(int(d)):    #      --type=diff
                m += 1
                rate = payment(loan_principal, d, y, m)
                overpayment_a -= rate
                print(f"Month {i + 1}: payment is " + str(rate))
            print()
            print("Overpayment = " + str(abs(overpayment_a)))

    if args.principal == None: # x == "p":
        annuity_payment = float(args.payment)
        d = float(args.periods)
        y = float(args.interest)
        loan_principal = int(principal(annuity_payment, d, y))
        print(f"Your loan principal = {loan_principal}!")
        overpayment_a = int(loan_principal - (d * annuity_payment))
        print("Overpayment = " + str(abs(overpayment_a)))
    stop = False
