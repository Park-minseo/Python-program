from random import *
import time
import sys

class unit:
    def __init__(self, name):
        self.name = name
        self.hp = randrange(100, 501)
        self.attack = randrange(50, 101)
        self.defend = randrange(10, 51)
        self.pre = randrange(100)
        self.addatk = randrange(10, 26)
        print("{} 캐릭터가 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}, 방어력 : {2}, 추가데미지 : {4}, 선공 : {3}".format(self.hp, self.attack, self.defend, self.pre, self.addatk))

이름1 = input("첫번째 캐릭터의 이름을 적어주세요: ")
이름2 = input("두번째 캐릭터의 이름을 적어주세요: ")
선공 = 데미지 = 추가데미지 = 0

캐릭터1 = unit(이름1)
print("-"*50)
캐릭터2 = unit(이름2)
print("-"*50)
print("게임을 시작하겠습니다. 선공 수치가 높은 캐릭터부터 시작합니다. 공격 계산식 : 공격력 * (방어력 / 100) + 랜덤 추가데미지 ")

if 캐릭터1.pre > 캐릭터2.pre:
    선공 = 0
elif 캐릭터1.pre == 캐릭터2.pre:
        a = randrange(0,2)
        if a == 1:
            선공 = 0
        else:
            선공 = 1
elif 캐릭터1.pre < 캐릭터2.pre:
        선공 = 1

print("캐릭터의 정보를 확인해주세요. 5초 뒤 게임이 자동으로 시작됩니다.")
time.sleep(5)

if 캐릭터1.hp > 0 and 캐릭터2.hp > 0:
    while True:
        if 선공 == 0:
            추가데미지 = randrange(캐릭터1.addatk)
            print("-"*50)
            print("{} 캐릭터의 공격차례 입니다. 공격을 시작합니다.".format(캐릭터1.name))
            데미지 = round(캐릭터1.attack * (캐릭터2.defend / 100) + 추가데미지)
            캐릭터2.hp = 캐릭터2.hp - 데미지
            print("{0} 캐릭터의 공격! 추가데미지는 {1}로 총 {2}의 공격을 가했습니다. {3} 캐릭터의 남은 hp는 {4} 입니다. ".format(캐릭터1.name, 추가데미지,\
            데미지, 캐릭터2.name, 캐릭터2.hp))
            if 캐릭터2.hp <= 0:
                print("{0} 캐릭터가 쓰러졌습니다. {1} 캐릭터의 승리입니다! ".format(캐릭터2.name, 캐릭터1.name))
                sys.exit()
            elif 캐릭터2.hp > 0:
                선공 = 1
            time.sleep(2)
        if 선공 == 1:
            추가데미지 = randrange(캐릭터2.addatk)
            print("-"*50)
            print("{} 캐릭터의 공격차례 입니다. 공격을 시작합니다.".format(캐릭터2.name))
            데미지 = round(캐릭터2.attack * (캐릭터1.defend / 100) + 추가데미지)
            캐릭터1.hp = 캐릭터1.hp - 데미지
            print("{0} 캐릭터의 공격! 추가데미지는 {1}로 총 {2}의 공격을 가했습니다. {3} 캐릭터의 남은 hp는 {4} 입니다. ".format(캐릭터2.name, 추가데미지,\
            데미지, 캐릭터1.name, 캐릭터1.hp))
            if 캐릭터1.hp <= 0:
                print("{0} 캐릭터가 쓰러졌습니다. {1} 캐릭터의 승리입니다! ".format(캐릭터1.name, 캐릭터2.name))
                sys.exit()
            elif 캐릭터1. hp > 0:
                선공 = 0
            time.sleep(2)