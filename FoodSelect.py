# -*- coding: utf-8 -*-
import random

foodSelect = ["감성골", "국밥", "부리또", "양식당", "종이밥", "맘스터치"]


# 음식 선택
def Choice():
    return random.choice(foodSelect)


# 음식 추가():
def addFood(Food):
    if Food in foodSelect:
        return Food + "가 이미 있습니다."
    else:
        foodSelect.append(Food)
        return Food + "을(를) 추가했습니다."


# 음식 제거():
def removeFood(Food):
    if Food in foodSelect:
        foodSelect.remove(Food)
        return Food + "을(를) 제거했습니다."
    else:
        return Food + "을(를) 찾을 수 없습니다."
