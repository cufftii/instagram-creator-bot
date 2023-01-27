from api.completion import generate_txt
from api.process_prompt import Prompt
from datetime import datetime

current_year = datetime.now().year
current_month = datetime.now().month
current_year_month = "Year {}, Month {}".format(current_year, current_month)

f = open("results/profile.txt",'r', encoding="utf-8")
profile = f.readlines()
f.close()

monthly_plan = generate_txt(Prompt.monthly_plan(current_year_month, profile), 0.9)
monthly_plan = "Plan for {}\n".format(current_year_month) + monthly_plan

f = open("results/monthly_plan.txt", 'w', encoding='utf-8')
print(monthly_plan, end = '', file = f)
f.close()