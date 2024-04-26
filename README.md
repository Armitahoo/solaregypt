# solaregypt
Shining a Light on Egypt's Energy Future: Transitioning from Fossil Fuels to Solar Power
# The process of this analysis
##1.	Data Collection
First, I wanted to know how Egypt generates electricity and how much of it is from fossil fuel. So I got the data I needed from [here](https://ourworldindata.org/energy) and [here]( https://www.iea.org/countries/egypt)
If you want to take a look at the raw data you can find them [here](https://github.com/Armitahoo/solaregypt/blob/main/owid-energy-data.csv) and [here](https://github.com/Armitahoo/solaregypt/blob/main/International%20Energy%20Agency%20-%20Domestic%20energy%20production%2C%20Egypt%2C%202021.csv)
##2.Data Filtering
[Filtered data](https://github.com/Armitahoo/solaregypt/blob/main/Fuel.py): The data contains information about all countries from 1900 to 2022. So, I wanted to remove the information about Egypt from 2000 to 2022, so I needed to filter the data. 
##3.	Made charts
After successfully filtering the data, I made the charts illustrated below to present the energy situation in Egypt.
![Chart1](https://github.com/Armitahoo/solaregypt/blob/main/Production.png)
![Chart2](https://github.com/Armitahoo/solaregypt/blob/main/Fuel%20Type.png)
##4.	[Computed information about electricity](https://github.com/Armitahoo/solaregypt/blob/main/Electricity%20demand.py)
I gathered information about [electricity price](https://www.global-climatescope.org/markets/eg/) and [subsidization](https://www.tni.org/en/article/the-imf-and-ending-energy-subsidies-in-egypt) in Egypt after making the charts. Then, I computed the total electricity cost per capita based on the total electricity produced per capita. 
##5.	Gathered information about externalities 
from [here](https://aps.aucegypt.edu/en/articles/767/the-social-impact-of-air-pollution-in-egypt-the-contradictions-of-environmental-policy-in-egypt) and [here](https://www.greenpeace.org/static/planet4-southeastasia-stateless/2020/02/21b480fa-toxic-air-report-110220.pdf) and took the information into account for total cost calculation
##6.	[Made the heatmap](https://github.com/Armitahoo/solaregypt/blob/main/Heatmap.qgz )
I collected data about solar power potential from Global Solar Atlas and made the illustrated heatmap below.
heatmap
##7. Gathered information about the cost of CSP 
from [here](https://helioscsp.com/cost-of-concentrated-solar-power-csp-projects-fell-from-usd-0-38-kwh-to-usd-0-118-kwh-a-decline-of-69/#:~:text=Between%202010%20and%202022%2C%20the,)%20to%20USD%200.118%2FkWh)
##8.	[Computed the cost of installation and net present value](https://github.com/Armitahoo/solaregypt/blob/main/Solar.py)
The present value represents the current worth of a future amount, taking into account a specific discount rate or interest rate. This concept is useful for understanding the value of money over time, acknowledging that a dollar today is worth more than a dollar in the future due to factors like inflation, risk, and opportunity costs.
###Present Value Formula
The general formula for calculating the present value of a future sum is:
𝑃𝑉=𝐹𝑉(1+𝑟)𝑛PV=(1+r)nFV
PV is the present value.
FV is the future value—the sum you're considering.
r is the interest rate (expressed as a decimal).
n is the number of periods (often years) into the future.

##9.	[Computed the break-even point](https://github.com/Armitahoo/solaregypt/blob/main/yes%20or%20no.py)
To calculate the break-even point, the key concept is the Present Value (PV), which helps determine the value of a future cash flow today by considering the time value of money and the interest rate.
Here's a breakdown of how we calculated the break-even point in this case:
###Present Value Formula:
The formula for the present value of an annuity is:
𝑃𝑉=𝐶×(1−(1+𝑟)−𝑛𝑟)PV=C×(r1−(1+r)−n)
C is the annual cash flow, 𝑟r is the discount rate (or interest rate), and n is the number of years.
###Equating the Present Values:
+We wanted to find out at what point the PV of solar equals the PV of the current production method.
+We set up a symbolic expression with the annual cash flow of the current method and found the time 𝑡t where its present value would be equal to the PV of the CSP (Concentrated Solar Power).
###Solving for Break-Even Time:
+We used a symbolic algebra library to solve for 𝑡t when the PV of the current method (with or without externalities) becomes equal to the PV of the CSP installation.
+If the solution has imaginary numbers, it suggests that a break-even point doesn't occur within a realistic time frame, making it "Not Viable."
###These steps led us to conclude that:
+The break-even point with externalities is about 1.74 years.
+The break-even point without externalities isn't viable, indicating that the CSP installation would not break even with the current method within a reasonable timeframe.
