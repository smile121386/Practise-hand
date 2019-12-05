import random

number = random.randint(1, 100)
guess = 0
while True:
    number_input = input("请输入1-100的整数:")
    guess += 1
    if not number_input.isdigit():
        print("请输入数字!")
    elif int(number_input) < 1 or int(number_input) > 100:
        print("请输入1-100的整数!")
    else:
        if int(number_input) == number:
            print("恭喜猜对了!")
            print("总共猜了%s次" % guess)
            break
        elif int(number_input) > number:
            print("猜大了!")
            # print("目前猜了%s次" % guess)
            continue
        else:
            print("猜小了!")
            # print("目前猜了%s次" % guess)
            continue
