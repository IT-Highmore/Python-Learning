
"""
字典 键值是惟一的，正好对应nums 不重复的值

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
一般用在 for 循环当中。
"""

def sum(nums, target):
  hashmap = {}
  for index, num in enumerate(nums):
    print(index,num)
    another_num = target - num
    if another_num in hashmap:
      print(hashmap[another_num], index)
      return [hashmap[another_num], index]
    hashmap[num] = index
    print(hashmap)
  return None

sum([2, 7, 11, 15,8,4], 6)

"""
运行结果
0 2
{2: 0}
1 7
{2: 0, 7: 1}
2 11
{2: 0, 7: 1, 11: 2}
3 15
{2: 0, 7: 1, 11: 2, 15: 3}
4 8
{2: 0, 7: 1, 11: 2, 15: 3, 8: 4}
5 4

0 5

"""