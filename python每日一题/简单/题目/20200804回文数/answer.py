# 第一种方法
# str(n)[::-1]实现字符串翻转
# def isPalindrome(num):
#   if x < 0:
#     return False
#   else:
#     y = str(x)[::-1]
#     if y == str(x):
#       return True
#     else:
#       return False

# 第二种方法  转成字符串

def isPalindrome(num):
  string = str(num)
  chars = list(str(num))  # 将输入数字转换成为字符串列表
  chars.reverse()  # 逆序
  r = ''.join(chars)  # 合并成字符串
  if string == r:
    return True
  else:
    return False


isPalindrome(-123)





"""
JavaScript 方法
var isPalindrome = function(num){
   var str = String(x)
    var reverse = str.split("").reverse().join("")
    if(str == reverse) {
        return true
    } else {
        return false
    }
}

"""



