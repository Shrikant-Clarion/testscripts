nums = [1, 2, 3, 4, 5]
words = ['one', 'two', 'three', 'four', 'five']

d = dict(zip(nums, words))

print(d)
print(type(d))

d1 = {}
for i, val in enumerate(nums):
    d1[val] = words[i]

print(d1)
print(type(d1))


def listtodict(list1, list2):
    return dict(max(vars(__builtins__).items())[1](list1, list2))

d3 = listtodict(nums, words)

print(d3)
print(type(d3))