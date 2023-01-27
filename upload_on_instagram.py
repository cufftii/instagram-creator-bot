from instagram_bot.upload import upload_on_instagram

f = open("results/nickname.txt",'r', encoding="utf-8")
nickname = f.readline()
f.close()

upload_on_instagram(nickname)