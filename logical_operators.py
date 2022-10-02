high_income = True
good_credit = False
student = True

# and operator
if high_income and good_credit:
    print("Eligiable")
else:
    print("Not eligiable")

# or operator
if high_income or good_credit:
    print("Eligiable")
else:
    print("Not eligiable")

#not opetator
if not student:
    print("Eligiable")
else:
    print("Not eligiable")

# Complex Example
if(high_income or good_credit) and not student:
    print("Eligiable")
else:
    print("Not eligiable")

# Short Circuit
if high_income and good_credit or not student:
    print("Eligiable")
else:
    print("Not eligiable")
