# Constants for the calculation
electricity_consumption_per_capita = 1851.14  # kWh per capita
cost_per_kwh = 0.118  # USD per kWh
lifespan = 25  # Lifespan of the CSP installation in years
interest_rate = 0.05  # Discount rate for present value calculation

# Step 1: Cost of electricity per capita per year
cost_per_capita_per_year = electricity_consumption_per_capita * cost_per_kwh

# Step 2: Total cost over the lifespan per capita
total_cost_over_lifespan_per_capita = cost_per_capita_per_year * lifespan

# Step 3: Calculate the present value
# Formula for the present value of an annuity: PV = C * (1 - (1 + r)^-n) / r
present_value = cost_per_capita_per_year * ((1 - (1 + interest_rate_rate) ** -lifespan) / discount_rate)

present_value  # Return the present value
