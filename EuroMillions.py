import random

main_numbers = []
bonus_numbers = []
main_numbers_count=0
bonus_numbers_count=0

while main_numbers_count<5:
    number=random.randint(1,50)
    if number not in main_numbers:
         main_numbers.append(number)
         main_numbers_count+=1
while bonus_numbers_count<2:
    number=random.randint(1,12)
    if number not in bonus_numbers:
        bonus_numbers.append(number)
        bonus_numbers_count+=1

print(main_numbers,bonus_numbers)

        
