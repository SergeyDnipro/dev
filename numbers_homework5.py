from pywebio.input import input as pw_input
from pywebio.input import FLOAT
from pywebio.output import put_success, put_warning
from decimal import Decimal

# kKal/100gr of products

OSTRICH_EGG_KKAL = 118
RABBIT_KKAL = 197
SEA_FISH_KKAL = 123
RED_PEPPER_SWEET_KKAL = 26
GREEN_GRASS_KKAL = 45
BANANAS_KKAL = 87
WAFFLES_KKAL = 425
GRAIN_BREAD_FIRST_CLASS_KKAL = 246
PISTACHIO_KKAL = 555
KEFIR_25_KKAL = 51

total_kkal = 0

# ostrich_egg_weight = slider('Enter wight of ostrich eggs you want (gramm): ',
#                             value=0.0,
#                             min_value=0.0,
#                             max_value=1000.0)

ostrich_egg_weight = pw_input('Enter wight of ostrich eggs you want (gramm): ', type=FLOAT)
result = round(ostrich_egg_weight * OSTRICH_EGG_KKAL / 100, 2)
total_kkal += result
put_success(f'kCalories of your portion of eggs: {result} \n'
            f'Total calories: {total_kkal}')

rabbit_weight = pw_input('Enter weight of rabbit meat you want to eat (gramm): ', type=FLOAT)
result = round(rabbit_weight * RABBIT_KKAL / 100, 2)
total_kkal += result
put_success(f'kCalories of your portion of rabbit meat: {result} \n'
            f'Total calories: {total_kkal}')

sea_fish_weight = pw_input('Enter weight of sea fish you want to eat (gramm): ', type=FLOAT)
result = round(sea_fish_weight * SEA_FISH_KKAL / 100, 2)
total_kkal += result
put_success(f'kCalories of your portion of sea fish: {result} \n'
            f'Total calories: {total_kkal}')

if total_kkal < 1000:
    put_warning('You are still hungry')
elif total_kkal > 1500:
    put_warning('You ate to much')
else:
    put_success('All OK')

put_success(f'Your bill for dinner is: '
            f'{Decimal(total_kkal * 0.32541).quantize(Decimal("0.01"))} UAH')
