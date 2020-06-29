# FireClothes Shop cart

# Variables of Descriptions
outline_hoodie = "A cosy material-mix hoodie"
outline_joggers = "Soft material-mix sweat pants ."
sst_track_hoodie = "Floral adidas track jacket ."
crew_sweatshirt = "An adidas pullover"

# Variables of prices of products
outline_hoodie_price = 20.97
outline_joggers_price = 17.97 
sst_track_hoodie_price = 20.97
crew_sweatshirt_price = 34.98

# Shopping cart - Adding customer one shop
customer_one_cart = crew_sweatshirt_price * 2 + crew_sweatshirt_price * 8 + outline_hoodie_price

# Shopping cart total
cart_summary = "You have picked : " + crew_sweatshirt + " , " + sst_track_hoodie + ' , ' + outline_hoodie
print(cart_summary)

Total_message = "SubTotal: £" + str(customer_one_cart)
print(Total_message)



