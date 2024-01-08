import math

c = 1576014706
l_t1_t2 = -2.71985*10**-6

for i in range(1, 1+10**10):

    activityPerCycle = c * (1 - math.exp(i*l_t1_t2))

    if i == 10:
        print(f"Activity = {activityPerCycle} Bq for 10 cycles.")
    if i == 10**2:
        print(f"Activity = {activityPerCycle} Bq for 10^2 cycles.")
    if i == 10**3:
        print(f"Activity = {activityPerCycle} Bq for 10^3 cycles.")
    if i == 10**4:
        print(f"Activity = {activityPerCycle} Bq for 10^4 cycles.")
    if i == 10**5:
        print(f"Activity = {activityPerCycle} Bq for 10^5 cycles.")
    if i == 10**6:
        print(f"Activity = {activityPerCycle} Bq for 10^6 cycles.")
    if i == 10**7:
        print(f"Activity = {activityPerCycle} Bq for 10^7 cycles.")
    if i == 10**8:
        print(f"Activity = {activityPerCycle} Bq for 10^8 cycles.")
    if i == 10**9:
        print(f"Activity = {activityPerCycle} Bq for 10^9 cycles.")
    if i == 10**10:
        print(f"Activity = {activityPerCycle} Bq for 10^10 cycles.")