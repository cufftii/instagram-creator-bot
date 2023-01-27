from api.completion import generate_txt
from api.process_prompt import Prompt

profile = generate_txt(Prompt.profile(), temperature=0.7)
nickname = generate_txt(Prompt.nickname(profile), temperature=0.7)
bio = generate_txt(Prompt.bio(profile, nickname), temperature=0.7)

f = open("results/profile.txt", 'w', encoding='utf-8')
print(profile, bio, sep = '\n', end = '', file = f)
f.close()

f = open("results/nickname.txt", 'w', encoding='utf-8')
print(nickname, end = '', file = f)
f.close()
