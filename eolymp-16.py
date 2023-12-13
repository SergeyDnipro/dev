one_head_insect_leg_count, dragon_head_count, all_head, all_legs = map(int, input().split())
dragon_numbers = 1
insect_numbers = 1

while True:
    insect_heads = all_head - dragon_head_count * dragon_numbers
    total_insect_legs = insect_heads * one_head_insect_leg_count
    if insect_heads <= 0 or \
            dragon_head_count >= all_head or \
            one_head_insect_leg_count >= all_legs:
        dragon_legs = -1
        break
    if total_insect_legs < all_legs and (all_legs - total_insect_legs) % dragon_numbers == 0:
        dragon_legs = (all_legs - total_insect_legs) // dragon_numbers
        break
    dragon_numbers += 1


print(dragon_legs)

