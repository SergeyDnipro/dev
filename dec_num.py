import decimal
from decimal import Decimal, getcontext

k = 100
precision = 1 / (10 ** k)
print(precision)
getcontext().prec = k

temp_res = Decimal('1') / Decimal('3')

res = temp_res.quantize(Decimal(str(precision)))
print(res)
