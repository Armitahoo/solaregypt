import sympy as sp

# Variables for the calculation
lifespan = 30
interest_rate = 0.05

# Given values
total_production_cost = 6719130000  # Current production cost
total_with_externalities = 17424000000  # Production cost with externalities

# Present Value formula
# C = Total annualized cost
# r = Discount rate
# n = lifespan

# Present Value of current production cost
PV_current = total_production_cost * ((1 - (1 + interest_rate) ** -lifespan) / interest_rate)
PV_with_externalities = total_with_externalities * ((1 - (1 + interest_rate) ** -lifespan) / interest_rate)

# Present Value of CSP
PV_CSP = 207255702888  # Given net present value of CSP

# Break-even calculation
# Equate the Present Values
# The point at which PV of CSP is equal to PV of current production with externalities
t = sp.symbols('t')  # Time variable
PV_current_expr = total_with_externalities * ((1 - (1 + interest_rate) ** -t) / interest_rate)

# Solve for t when the present value of CSP is equal to the present value of current methods with externalities
break_even_time = sp.solve(PV_current_expr - PV_CSP, t)

break_even_time = "Not Viable" if sp.im(break_even_time[0]) != 0 else break_even_time[0]

print(break_even_time)  

# Present Value of current production cost without externalities
PV_current_expr_without_externalities = total_production_cost * ((1 - (1 + interest_rate) ** -t) / interest_rate)

# Solve for t when the present value of CSP is equal to the present value of current methods without externalities
break_even_time_without_externalities = sp.solve(PV_current_expr_without_externalities - PV_CSP, t)

break_even_time_without_externalities

# Determine if break-even point exists for present value of current production without externalities
# If there is an imaginary part, return "Not Viable"
break_even_point_without_externalities = "Not Viable" if sp.im(break_even_time_without_externalities[0]) != 0 else break_even_time_without_externalities[0]

print(break_even_point_without_externalities) 
