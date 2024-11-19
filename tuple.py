inventory=[("laptop",20,50000),("monitor",5,10000),("smartphone",15,10000)]
highest_stock_value=0
item_with_highest_value=None
for item in inventory:
    item_name,quantity,stock_value=item
    print(item_name,quantity,stock_value)
for item in inventory:
    item_name,quantity,unit_price=item
    total_value=quantity*unit_price
    print(f"item name:{item_name},stock value is:{total_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_value=item
print(f"highest stock value is:{highest_stock_value}")
print(f"item with highest stock value is:{item_with_highest_value}")

