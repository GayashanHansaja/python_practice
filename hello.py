price=1000000
down_payment=0
is_good_credit = False

if is_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(down_payment )
