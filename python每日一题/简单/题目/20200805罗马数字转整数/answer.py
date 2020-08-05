

def romanToInt(s):
  val = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
  num = 0
  for i in range(len(s)):
    if i < len(s) - 1 and val[s[i]] < val[s[i+1]]:
      num -= val[s[i]]
    else:
      num += val[s[i]]

  print(num)
  return num


romanToInt('IL')

"""
JavaScript 方法

array.reduce(function(total, currentValue, currentIndex, arr), initialValue)

参数	描述
total	 必需。初始值, 或者计算结束后的返回值。
currentValue	必需。当前元素
currentIndex	可选。当前元素的索引
arr	 可选。当前元素所属的数组对象。
initialValue	可选。传递给函数的初始值


var romanToInt = function(s) {
    const val = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 }
    return s.split('').reduce((prev, next, idx, arr) => val[next] < val[arr[idx + 1]] ? 
    prev - val[next] : prev + val[next], 0)
};

"""



