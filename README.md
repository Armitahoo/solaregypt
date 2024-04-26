# Solar Egypt
Shining a Light on Egypt's Energy Future: Transitioning from Fossil Fuels to Solar Power

# The process of this analysis
##	Data Collection
First, I wanted to know how Egypt generates electricity and how much of it is from fossil fuel. So I got the data I needed from [here](https://ourworldindata.org/energy) and [here]( https://www.iea.org/countries/egypt)
If you want to take a look at the raw data you can find them [here](https://github.com/Armitahoo/solaregypt/blob/main/owid-energy-data.csv) and [here](https://github.com/Armitahoo/solaregypt/blob/main/International%20Energy%20Agency%20-%20Domestic%20energy%20production%2C%20Egypt%2C%202021.csv)
## Data Filtering
[Filtered data](https://github.com/Armitahoo/solaregypt/blob/main/Fuel.py): The data contains information about all countries from 1900 to 2022. So, I wanted to remove the information about Egypt from 2000 to 2022, so I needed to filter the data. 
## Made charts
After successfully filtering the data, I made the charts illustrated below to present the energy situation in Egypt.
![Chart1](https://github.com/Armitahoo/solaregypt/blob/main/Production.png)
![Chart2](https://github.com/Armitahoo/solaregypt/blob/main/Electricity.png)
## [Computed information about electricity](https://github.com/Armitahoo/solaregypt/blob/main/Electricity%20demand.py)
I gathered information about [electricity price](https://www.global-climatescope.org/markets/eg/) and [subsidization](https://www.tni.org/en/article/the-imf-and-ending-energy-subsidies-in-egypt) in Egypt after making the charts. Then, I computed the total electricity cost per capita based on the total electricity produced per capita. 
## Gathered information about externalities 
* Disclaimer: For simplicity, I did not take the current 35% inflation rate into account
from [here](https://aps.aucegypt.edu/en/articles/767/the-social-impact-of-air-pollution-in-egypt-the-contradictions-of-environmental-policy-in-egypt) and [here](https://www.greenpeace.org/static/planet4-southeastasia-stateless/2020/02/21b480fa-toxic-air-report-110220.pdf) and took the information into account for total cost calculation
## [Made the heatmap](https://github.com/Armitahoo/solaregypt/blob/main/Heatmap.qgz )
I collected data about solar power potential from Global Solar Atlas and made the illustrated heatmap below.
heatmap
## Gathered information about the cost of CSP 
from [here](https://helioscsp.com/cost-of-concentrated-solar-power-csp-projects-fell-from-usd-0-38-kwh-to-usd-0-118-kwh-a-decline-of-69/#:~:text=Between%202010%20and%202022%2C%20the%20to%20USD%200.118%2FkWh)
![Heatmap](https://github.com/Armitahoo/solaregypt/blob/main/Heatmap.png)
## [Computed the cost of installation and net present value](https://github.com/Armitahoo/solaregypt/blob/main/Solar.py)
The present value represents the current worth of a future amount, taking into account a specific discount rate or interest rate. This concept is useful for understanding the value of money over time, acknowledging that a dollar today is worth more than a dollar in the future due to factors like inflation, risk, and opportunity costs.
### Present Value Formula
The general formula for calculating the present value of a future sum is:
+ 𝑃𝑉= $𝐹𝑉/(1+𝑟)^𝑛$
+ PV is the present value.
+ FV is the future value—the sum you're considering.
+ r is the interest rate (expressed as a decimal).
+ n is the number of periods (often years) into the future.

## 	[Computed the break-even point](https://github.com/Armitahoo/solaregypt/blob/main/yes%20or%20no.py)
To calculate the break-even point, the key concept is the Present Value (PV), which helps determine the value of a future cash flow today by considering the time value of money and the interest rate.
Here's a breakdown of how we calculated the break-even point in this case:
### Present Value Formula:
The formula for the present value of an annuity is:
+ 𝑃𝑉= $𝐶×((1−(1/1+𝑟)^n)/𝑟)$
+ C is the annual cash flow, 𝑟r is the discount rate (or interest rate), and n is the number of years.
### Equating the Present Values:
+ We wanted to find out at what point the PV of solar equals the PV of the current production method.
+ We set up a symbolic expression with the annual cash flow of the current method and found the time 𝑡t where its present value would be equal to the PV of the CSP (Concentrated Solar Power).
### Solving for Break-Even Time:
+ We used a symbolic algebra library to solve for 𝑡t when the PV of the current method (with or without externalities) becomes equal to the PV of the CSP installation.
+ If the solution has imaginary numbers, it suggests that a break-even point doesn't occur within a realistic time frame, making it "Not Viable."
### These steps led us to conclude that:
+ The break-even point with externalities is about 18.5 years.
+ The break-even point without externalities isn't viable, indicating that the CSP installation would not break even with the current method within a reasonable timeframe.
# Conclusion: Shining a Light on Egypt's Energy Future
The analysis outlined above reveals a compelling case for Egypt to shift from fossil fuels to renewable energy sources, particularly solar power, to generate electricity. This shift is crucial not only from an economic perspective but also for public health and environmental sustainability.

## Impact of Fossil Fuels
The reliance on fossil fuels for electricity generation has significant externalities, including:

+ Premature Death Rate: Air pollution from burning fossil fuels contributes to respiratory and cardiovascular diseases, leading to increased mortality rates.
+ Healthcare Costs: The healthcare system bears a heavy burden due to the illnesses caused by air pollution, increasing costs for treatment and care.
+ Lost Working Days: Poor air quality results in lost productivity and working days due to sickness and related health issues.
  
## Economic and Environmental Incentives
Given these high externalities, the transition to renewable energy, especially solar power, becomes economically and environmentally advantageous. The data suggests that Egypt could achieve a break-even point with solar energy by 2049, considering the present value and cost of Concentrated Solar Power (CSP) installations.

## Benefits of Transitioning to Solar Energy
+ Reduced Air Pollution: Switching to solar power significantly reduces air pollution, improving public health and reducing healthcare costs.
+ Lower Greenhouse Gas Emissions: Solar energy is a cleaner alternative, contributing to a lower carbon footprint and aligning with global climate goals.
+ Long-Term Cost Savings: The break-even point analysis indicates that solar power can become more cost-effective than traditional fossil fuel-based methods, especially when externalities are considered.

## Moving Forward
Given the projected break-even point (2049), Egypt can focus on investment in solar infrastructure, policy incentives, and public awareness to facilitate the transition to renewable energy. The journey to renewable energy is not only about recovering costs but also about establishing a sustainable and healthier future.

## Conclusion
Considering the externalities and long-term benefits, Egypt should prioritize solar power for electricity generation. By the break-even point in 2049, the transition to renewable energy becomes economically advantageous, making it a beneficial and necessary shift for the country's health, environment, and economy.
