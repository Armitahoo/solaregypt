# Constants for the calculation
electricity_consumption_per_capita = 1851.14  # kWh per capita
cost_per_kwh = 0.118  # USD per kWh
lifespan = 30  # Lifespan of the CSP installation in years
interest_rate = 0.05  # Discount rate for present value calculation

# Step 1: Cost of electricity per capita per year
cost_per_capita_per_year = electricity_consumption_per_capita * cost_per_kwh

# Step 2: Total cost over the lifespan per capita
total_cost_over_lifespan_per_capita = cost_per_capita_per_year * lifespan

# Step 3: Calculate the present value
# Formula for the present value of an annuity: PV = C * (1 - (1 + r)^-n) / r
present_value = cost_per_capita_per_year * ((1 - (1 + interest_rate) ** -lifespan) / interest_rate)


print("\nThe Present Value of the CSP for 30 years is:", round(present_value,2))

# Updated population and energy demand per capita
population = 121000000  # 121 million people

# Step 1: Determine total energy demand with the new population size
total_energy_demand = population * electricity_consumption_per_capita  # Total annual energy demand in kWh

# Step 2-3: (These stay the same as before)
# Capacity factor for CSP and energy output per kW

capacity_factor = 0.25
energy_output_per_kw_per_year = 365 * 24 * capacity_factor  # kWh/kW per year

# Step 4: Estimate required capacity with the new population size
required_capacity = total_energy_demand / energy_output_per_kw_per_year  # in kW

print("\nThe Required Capacity Needed for Electricity is:", round(required_capacity,2)) 

# Installation cost for CSP
installation_cost_per_kw = 4379  # USD/kW

# Given the required capacity in kW
required_capacity = 102277598.17351598  # in kW

# Calculate the total installation cost
total_installation_cost = required_capacity * installation_cost_per_kw  # in USD

print("\nThe total installation cost for year 2030 is:", round(total_installation_cost,2))

present_value = total_installation_cost / ((1 + interest_rate) ** lifespan)

net = present_value+present_value

print("\nNet Present value for CSP:", round(net))

Total_pro = 55.53 * population
print("\nTotal production cost with current methods:", round(Total_pro))

total_w_ex = 1055 * population
print("\nTotal production cost with externalities:", round(total_w_ex))

PV = Total_pro* ((1 - (1 + interest_rate) ** -lifespan) / interest_rate)
PV1 = total_w_ex* ((1 - (1 + interest_rate) ** -lifespan) / interest_rate)

print(PV)
print(PV1)


