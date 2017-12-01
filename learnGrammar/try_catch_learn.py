try:
    answer = 10 / 3
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("answer:" + str(answer))
finally:
    print("finally")
