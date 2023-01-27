class Prompt:
    def profile():
        profile = "You are a 'Character Creator. \
            You are going to create an instagram nickname of a college student girl, \
            who shares her daily life and a watercolor drawing related to her day. \
            Write a basic profile of her, including her name, age, major, family members, and personality. \
            Please be creative.\n \
            Her name :\n \
            Her age : \n \
            Her major : \n \
            Her family members : \n \
            Her personality : "
        return profile

    def nickname(profile):
        nickname = "You are a 'Instagram nickname Creator'. \
            You are going to create an instagram nickname of a college student girl, \
            who shares her daily life and a watercolor drawing related to her day. \
            Write only her nickname in fun and creative way. \
            You may use following basic information of her. \
            \nHer profile is : \n{} \
            \nPlease give me only the nickname, and do not add additional words.".format(profile)
        return nickname

    def bio(profile, nickname):
        bio = "You are a 'Instagram Bio Creator'. \
            You are going to create an instagram bio of a college student girl, \
            who shares her daily life and a watercolor drawing related to her day. \
            \nHer profile is : {}. \
            \nHer instagram nickname is : {} \
            \nWrite only her bio in fun and creative way.\
            Her bio must be really short, only important words in it, and without any hashtags!!\
            \nPlease give me only the bio, and do not write any additional words.".format(profile, nickname)
        return bio
    
    def monthly_plan(current_month, profile):
        monthly_plan = "You are going to create a monthly plan of a girl in {}.\
            You must write for all of the day in the month really briefly, not just a weak, for a whole month!!! \
            You may use the following basic information of her, or not. \
            \nHer profile is : {}. Be creative.".format(current_month, profile)
        return monthly_plan
    
    def daily_post(current_time, profile, monthly_plan):
        daily_post = "Find out what she did at {} of this month, and \
            Create a short instagram post of a girl. The post has to be attractive, charming, funny and creative. \
            \nHer monthly schedule is : {} \
            You may refer to the following basic information of her. \
            \nHer profile is : {} \
            \nYou may be creative. You may add additional details not mentioned on her schedule. \
            Please give me only the post text, and do not write any additional words, including mood and time.".format(current_time, profile, monthly_plan)
        return daily_post