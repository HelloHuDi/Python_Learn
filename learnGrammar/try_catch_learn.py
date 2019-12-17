"""异常"""

# 有异常的情况下 else 不会执行，finally 任何情况下都会执行
try:
    answer = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("answer:" + str(answer))
finally:
    print("finally")

print()

# 无异常的情况下 else 会执行，finally 任何情况下都会执行
try:
    answer = 10 / 3
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("answer:" + str(answer))
finally:
    print("finally")
