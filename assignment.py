# define the function to calculate the simple interest in python 
#simple interest=(principal amount * rate amount * the number of year )/100
def simple_interest_calculator(p , r , t):
   simple_interest=(p * r * t)/100
   return simple_interest
p = float(input('Enter Principal Amount'))
r = float(input('Enter Rate Amount')) 
t = float(input('Enter The Number Of year' ))

print('Simple Interest: {0}'.format(simple_interest_calculator(p,r,t)))







    




