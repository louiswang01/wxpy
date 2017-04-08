from wxpy import *

bot=Bot()

my_friend = bot.friends().search('amy', sex=FEMALE)

my_friend = ensure_one(my_friend)
tuling = Tuling(api_key='13bc782fee384cf3a87931e2af4bd9bf')

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

embed()