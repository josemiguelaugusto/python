
sales = {
    "Jan":[120, 11, 434, 444, 200],
    "Feb":[200, 300, 2000, 450],
    "Mar": [230, 450, 1200, 300, 500],
    "Apr":[400, 69, 850, 1000,120],
    "May":[3000, 450, 200,800, 50],
    "Jun":[300, 344, 1233, 5460, 7000]
    }
month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]


global total
total = 0
for i in range(0, len(month_list)):
   total += int(f"{sum(sales[month_list[i]])}")
print(f"Total off all sales:  {float(total):.2f}£")
