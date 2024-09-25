salary = int(input("Enter your salary here:"))
loan = int(input("Enter your desired loan:"))

if (salary >= 30000.00) and (loan <= salary*10):

    print ("you are eligible for loan")

    months = int(input("how many months to pay?"))
    monthly_interest= float(loan*0.10)
    interest= float(loan+monthly_interest)
    payment = float(interest*months)

    print ("your amount to pay is:" , payment)

else:
    if (salary < 30000.00):
     print ("loan is denied due to low salary")
    
    if (loan > salary*10):
       print ("loan is denied due to high loan request")