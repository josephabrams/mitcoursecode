annual_salary=float(input("Enter your annual salary:"))#takes in and stores annual salary
portion_saved=0#takes in percent saved per month
portion_down_payment=.25 #percent of house cost for down payment
total_cost=1000000 #total cost of dream home
current_savings=0.07 #float storing savings
r=0.04 #annual rate of return on current savings*r/12

monthly_salary = annual_salary / 12
month=0
months=36
steps_in_search=0
semi_annual_raises=0.07
percent_integer=5000
test_salary=annual_salary
max_guess=10000
min_guess=0

#pick some number that is a 4 decimal long float, test it as portion_saved if higher than blah pick a number that is 1/2 that value and vice versa if lower
#maximum is 1.00 check this to see if savings are possible
# for i in range(months): #this checks maximum case 1
#     portion_saved=1.0
#     current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings * r / 12)
#     if i % 6 == 0:
#         test_salary = test_salary + test_salary * semi_annual_raises
#         monthly_salary = test_salary / 12
# if current_savings<(total_cost*portion_down_payment): #case 1
#     print("not possible you didn't go to MIT")
# else:
#     portion_saved=0.0

while abs(current_savings-(total_cost*portion_down_payment))>100:
    steps_in_search=steps_in_search+1
    portion_saved = percent_integer*.0001

    test_salary=annual_salary
    current_savings = 0.0
    monthly_salary=test_salary/12

    print("portion saved:",portion_saved)

    for i in range(months):
        print(i)
        print(current_savings)
        current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings * r / 12)
        if i % 6 == 0:
            test_salary = test_salary + test_salary * semi_annual_raises
            monthly_salary = test_salary / 12
        print("test_salary:", test_salary)
    #print(portion_saved)
    #print(current_savings)
    if current_savings < (total_cost * portion_down_payment) :
        min_guess=percent_integer
        percent_integer=percent_integer+((max_guess-percent_integer)/2)

    elif current_savings > (total_cost * portion_down_payment):
        max_guess=percent_integer
        percent_integer=percent_integer-((percent_integer-min_guess)/2)

print( "best savings rate: {}".format(portion_saved))
print("steps in bisection search",steps_in_search)
##########################







