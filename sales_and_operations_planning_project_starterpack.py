# Week 10 Lab Work 


# Ask user to enter the initial stock level, cast to integer and save as initial_stock_level

init_stock_level = int(input("Please Enter The Initial Stock Level: "))

# Ask user to enter the planning horizon (number of months to plan), cast to integer and save as no_of_months

no_of_months =int(input("Please Enter The Planning Horizon: "))

# Set an Accumulator for the dictionary of monthly sales

monthly_sales = {}

# For each month, ask user to enter the forecasted sale
# To do this loop through the month using a range

for month in range(1, no_of_months+1):
# for month in range(1, no_of_months+1):
#       Ask user to enter the forecasted sale for the month, cast to integer and save as forecast

        forecasted_sale =int(input(f"Please Enter The Forecasted Sale For Month {month}: "))

#      Add the forecast to the dictionary of monthly sales
        monthly_sales[month] = forecasted_sale  

# print(monthly_sales)        


# Print the resulting production quantities for each month

# Loop through the dictionary of monthly sales:

for month, forecast_sale in monthly_sales.items():
#       Check if forecast_sales > Initial Stock
    if init_stock_level > forecasted_sale:
        
        print(f"Production Quantity for Month {month} is Zero")
#           Reduce the stock level by the production Amount
        init_stock_level -= forecast_sale

#      Else:
    else:

#        How much do you have to produce for this month?
         qnty_produced =forecast_sale - init_stock_level
#        Print the Production Quantity
         print(f"Production Quantity For Month { month } is {qnty_produced}")
#        Update the stock level
         init_stock_level += qnty_produced - forecast_sale 
