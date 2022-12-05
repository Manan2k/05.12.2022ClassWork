import random
safe_code = []
while len(safe_code) < 3:
    code = random.randint(3, 12)
    if code not in safe_code:
        safe_code.append(code)
print(safe_code)

codesCracked = 0
while codesCracked < len(safe_code):
    for i in safe_code:
        print('Please input a number that divides to %d' % code)
        try:
            num1 = int(input('1st number'))
            num2 = int(input('2nd number'))
            result = num1/num2
            if result == code:
                print('Code unlocked')
                codesCracked += 1
        except ValueError:
            print('That is not a number!')
            break
else:
    print('You have opened the safe!')