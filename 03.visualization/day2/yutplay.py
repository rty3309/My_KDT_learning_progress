# Python 과제 #01
# KDT 12기 이재헌

print("-----윷놀이 게임 프로그램-----")

import random
import time

# 1. 윷 초기상태 지정
sticks = [0, 0, 0, 0]

def throw_sticks():
    global sticks
    for i in range(4):
        sticks[i] = random.randint(0, 1)

def get_result():
    yut = sticks.count(0)
    # 점수와 명칭 리턴
    if yut == 1: return 1, "도"
    if yut == 2: return 2, "개"
    if yut == 3: return 3, "걸"
    if yut == 4: return 4, "윷"
    if yut == 0: return 5, "모"
    return 0, ""

# 2. 게임 구조
# 흥부, 놀부 0점에서 시작
heungbu = 0
nolbu = 0

while True:
    # --- 흥부 턴 ---
    while True:
        throw_sticks()
        score, name = get_result()
        heungbu += score
        if heungbu >= 20:
            heungbu = 20 # 20점 초과 시 20점으로 고정
        print(f"흥부 {sticks}: {name} ({score}점)/(총 {heungbu}점) ->")
        time.sleep(0.5)
        if heungbu >= 20 or score < 4:
            break # 20점 달성 혹은 윷/모가 아니면 중단
    if heungbu >= 20:
        break

    # --- 놀부 턴 ---
    while True:
        throw_sticks()
        score, name = get_result()
        nolbu += score
        if nolbu >= 20:
            nolbu = 20
        print(f"{' '*20} <- 놀부 {sticks}: {name} ({score}점)/(총 {nolbu}점)")
        time.sleep(0.5)
        if nolbu >= 20 or score < 4:
            break
    if nolbu >= 20:
        break

# 3. 결과 출력
print("-" * 70)
if heungbu >= 20:
    winner = "흥부"
else:
    winner = "놀부"
print(f"{winner} 승리 => 흥부 : {heungbu} , 놀부 : {nolbu}")
