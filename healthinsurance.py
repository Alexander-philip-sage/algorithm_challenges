##wrote this to simulate the cost of one health plan vs another
hd = 113
ppo = 244
def go_to_therapy(freq= 0, cost = 100):
    '''freq is frequency per month'''
    total_ppo = 0
    total_hd = 0
    for i in range(12):
        for j in range(freq):
            total_ppo = monthly_charge(500, 2500, total_ppo, cost)
            total_hd = monthly_charge(2000, 3000, total_hd, cost)
        #print(i, "hdhp", total_hd)
        #print(i, "ppo", total_ppo)
    print("\nfreq",freq)
    print("total cost HDHP", total_hd+12*hd)
    print("total cost PPO", total_ppo+12*ppo)
def monthly_charge(deductible, oopm, running_charges, cost):
    if running_charges< deductible:
        running_charges += cost
    elif oopm > running_charges>= deductible:
        running_charges += cost*0.2
    elif oopm <= running_charges:
        running_charges += 0
    return running_charges


go_to_therapy(freq= 0, cost = 100)
go_to_therapy(freq= 2, cost = 100)
go_to_therapy(freq= 4, cost = 100)