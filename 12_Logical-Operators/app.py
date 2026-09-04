has_high_income = False
had_good_credit = True

if has_high_income and had_good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for loan")


if has_high_income or had_good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for loan")

# if applicant have a good credit and doesn't have a criminal  record.

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")