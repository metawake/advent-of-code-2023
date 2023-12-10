def find_first_last_digit(row):
    result = None

    digits = [n for n in row if n.isdigit()]
    result = '0'
    if len(digits) >= 2:
        result = digits[0] + digits[-1]
    elif len(digits) == 1:
        result = digits[0] + digits[0]

    result = int(result)

    return result

with open('data/1.data','r') as f:
    data = f.readlines()
    nums = []

    data = [d.rstrip('\n') for d in data]
    for row in data:
        n = find_first_last_digit(row)
        nums.append(n)
    print(sum(nums))
