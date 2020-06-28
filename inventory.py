# Computer CPU Inventory 

#Descriptions of all CPU's we sell assigned to a variable
cpu1_descripton = "Intel Core i7 9700K 3.6GHz Octa Core LGA1151 CPU"
cpu2_descripton ="Intel Core i5-10600K (Base Clock 4.10GHz, Socket LGA1200, 125 Watt)"
cpu3_descripton ="Intel CORE I5-9600K 3.7 GHZ SKT1151 9MB"

# List every item in the CPU Inventory
lists_cpu_inventory = cpu1_descripton,cpu2_descripton,cpu3_descripton

# Prices for CPU's in the invetory
cpu1_price = 332.00 
cpu2_price = 272.99 
cpu3_price = 184.99 
# Print items descriptions to screen
inventory_desc = cpu1_descripton,cpu2_descripton,cpu3_descripton
print("Products Descriptions:",inventory_desc)
# Totals Value of Inventory
inventory_total_price = cpu1_price + cpu2_price + cpu3_price 
print("Total price in inventory =",'£',inventory_total_price)

# Ordering System - Allows orders to be placed from our invetory

# Customer Places order 
order_one = cpu1_price + cpu3_price + cpu3_price

# Add tax of 8.8% to total
order_one += order_one * .100

# print summary to screen
print('Order Price:','£',order_one)


