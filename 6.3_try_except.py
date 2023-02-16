#inne bledy

#x = 1 / 0

try:
    x = 1 / 0
    print(x)
except ZeroDivisionError:
    print('X niezdeterminowany')