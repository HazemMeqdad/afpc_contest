customers = [15, 2, 1, 5, 3] 
customers.sort() 
satisfied_customers = 0

cumulative_waittime = 0 
for i in customers:
    if cumulative_waittime<= i :
        satisfied_customers += 1
        cumulative_waittime+=i

print(satisfied_customers)
