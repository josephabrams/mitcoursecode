annual_salary=float(input("Enter your annual salary:"))#takes in and stores annual salary
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:")) #takes in percent saved per month
portion_down_payment=.25 #percent of house cost for down payment
total_cost=1000000#total cost of dream home
current_savings=0.0 #float storing savings
r=0.04 #annual rate of return on current savings*r/12

monthly_salary = annual_salary / 12

month=0
semi_annual_raises=float(input("Enter your semi_annual raise, as a decimal: "))
while current_savings<(total_cost*portion_down_payment):
    month=month+1
    current_savings=current_savings+(monthly_salary*portion_saved)+(current_savings*r/12)
    if month%6==0:
        annual_salary=annual_salary+annual_salary*semi_annual_raises
        monthly_salary = annual_salary / 12
print( "Number of months: {}".format(month))