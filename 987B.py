from decimal import Decimal
x, y = map(int, raw_input().split())
aux = (Decimal(x) ** (Decimal(float(y))/Decimal(float(x))))
if aux == y:
    print "="
elif aux > y:
    print ">"
else:
    print "<"
