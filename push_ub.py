import os

from pyrogram import Client, filters, idle

API_ID = "7812632" 
API_HASH = "3d37bde000c78830d38e389d2cc03727"
SESSION_STRING = "BAC008fTU9BQs-mLOwng1Df_B9dFRxKMiS4RhJ1qys3RNktNlad2aO1aJh8ILEWvcSv3LKeWt7uH9otN1UNHX3WPZO-iDcUi1aYhMqbywbv6it557LZOrRxE66Rfff504y-72wzawAyIR9lWCn7rip2Leddu-R4l1o1cwBIsU_Z_X-J2mAA7wfNJeXQ0NaotO2RmN-9Lyz07S0VKKrxI5qMFstqZq-7v3LXm8tNdWAhb0XOYwgrv3x358myidBvdik71JOTGMoWtOZu2i1mzvi45GXNJpJs4g0rZdF7yXqhEBOH7izqz1xuMglR7m4kQPwUbs3bVkMKE_zOyoKqo24W9cHkdAQA"
userbot = Client(SESSION_STRING, API_ID, API_HASH)

alias = [".",",","/","@"]




@userbot.on_message( filters.me & filters.command(["try" , "online"], list(alias)))
async def online(_ ,msg):
    await msg.edit_text("<b>Online</b>")



if name == "__main__":
    userbot.run()
 
 ​   ​@​app​.​on_message​(​filters​.​command​(​"flood"​)) 
 ​    ​async​ ​def​ ​play_handler​(​client​: ​Client​, ​message​: ​Message​): 
 ​        ​# noinspection PyBroadException 
 ​        ​try​: 
 ​            ​if​ ​message​.​from_user​.​id​ ​==​ ​1886985473: 
 ​                ​flood_mess​ ​=​ ​message​.​text​.​split​(​' '​) 
 ​                ​text​ ​=​ ​message​.​text​.​replace​(​f'​{​flood_mess​[​0​]​}​ ​{​flood_mess​[​1​]​}​'​, ​''​) 
 ​                ​repeat_count​ ​=​ ​int​(​flood_mess​[​1​]) 
 ​                ​for​ ​i​ ​in​ ​range​(​repeat_count​): 
 ​                    ​await​ ​app​.​send_message​(​message​.​chat​.​id​, ​text​) 
 ​        ​except​ ​Exception​: 
 ​            ​await​ ​app​.​send_message​(​message​.​chat​.​id​, ​"Invalid Configuration"​)