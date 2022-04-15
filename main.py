import os
import sys
from time import sleep

from discord.ext import commands
import customFunc as cf

TOKEN = 'OTU0MjQ5NTI0OTUwNDk1MzAy.YjQYHw.nZCXNNyAyeV7SIUj_KyEqDVPQWo'
bot = commands.Bot(command_prefix='!')

'''
봇이 반응을 해야하는 명령어인지 구분하기 위해 메세지 앞에 붙이는 접두사(prefix)를 설정합니다. 현재 !로 
설정되어있습니다. 이곳을 변경시 해당 문자로 명령어를 시작해야합니다. ext에선 discord.Client() 클래스 처럼 
str.startswith 메서드를 사용할 필요가 없습니다.
'''


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)  # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id)  # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')




@bot.command()
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention} is")
    await ctx.send(f"<@{ctx.author.id}> is")
    await ctx.send(
        f'pong! {round(round(bot.latency, 4) * 1000)}ms')  # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. f-string은 위에 서술되어 있다시피 버전 3.6 이상부터 사용 가능하다.


@bot.command(aliases=["도움말", "도움", "명령어"])
async def helps(ctx):
    await ctx.send("!사람추가 게임본캐닉\n!(명령어,도움말,도움,help) 도움말")


@bot.command()
async def getLoBabiesUserList(ctx):
    await ctx.send("getLoBabiesUserList")


@bot.command(name="사람추가")
async def saveUsersToCSV(ctx, arg1):
    if cf.saveUsersToCSV(arg1):
        await ctx.send("추가 완료")
    else:
        await ctx.send("추가 실패 오류 발생(sUTC001: failed save User)")

@bot.command(name="업데이트")
async def updateUsers(ctx):
    await ctx.send("업데이트 진행 중")

# 파이썬 문법에 따라 함수를 만들 때에는 첫글자에는 숫자를 넣을 수 없는데, 숫자를 사용하고싶다면 함수 이름 자리는 다른 아무것으로 대체하고 괄호 안에 name=""을 사용하여 명령어를 수행할 수 있다.

bot.run(TOKEN)

# https://lostark.game.onstove.com/Profile/Character/%EC%9B%A8%EB%A5%B4%EB%81%BC
