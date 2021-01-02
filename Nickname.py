닉네임 = input("닉네임을 입력해주세요: ")

if len(닉네임) <= 6:
    print("반갑습니다. {0}님".format(닉네임))
else:
    while len(닉네임) > 6:
        닉네임 = input("닉네임이 너무 깁니다. 6자 이하로 입력해주세요: ")
        if len(닉네임) <= 6:
            print("반갑습니다. {0}님".format(닉네임))