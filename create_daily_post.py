from api.completion import generate_txt
from api.process_prompt import Prompt
from datetime import datetime

f = open("results/profile.txt",'r', encoding="utf-8")
profile = f.readlines()
f.close()

f = open("results/monthly_plan.txt",'r', encoding="utf-8")
monthly_plan = f.readlines()
f.close()

current_time = datetime.now().strftime("Day %d")
daily_post = generate_txt(Prompt.daily_post(current_time, profile, monthly_plan), 0.9)

f = open("results/daily_post.txt", 'w', encoding='utf-8')
print(daily_post, end = '', file = f)
f.close()