# Estimated yearly interest     

print('How many years will you be saving?')
years = int(raw_input('Enter Years:'))

print('How much money is currently in your account?')
principal = float(raw_input('Enter current amount in account: '))

print('How much money do you plan on investing monthly?')
monthly_invest = float(raw_input('Enter amount: '))

print('What do you estimate will be the yearly interest of this investment?')
interest = float(raw_input('Enter interest in decimal numbers (10% = 0.1):'))

print(' ')

monthly_invest = monthly_invest * 12 
final_amount = 0 

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal 

   