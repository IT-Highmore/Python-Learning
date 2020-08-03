# 第一种方法 取余
# def reverse(num):
#   newValue = 0
#   if num == 0:
#     return 0
#   if num > 0:
#     while num != 0:
#       newValue = newValue*10 + num%10
#       num = int(num/10)
#   else:
#     num = -num
#     while num != 0:
#       newValue = newValue*10 + num%10
#       num = int(num/10)
#     newValue = -newValue
#
#   print(newValue)
#   if newValue > pow(-2,31) and newValue < pow(2,31)-1:
#     return newValue
#   else:
#     print(newValue > pow(-2,31),newValue < pow(2,31)-1)
#     return 0


# 第二种方法  转成字符串
# join 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
def reverse(num):
  chars = list(str(num))  # 将输入数字转换成为字符串列表
  if num < 0:
    chars.remove('-')  # 去除负号
    chars.reverse()  # 逆序
    r = ''.join(chars)  # 合并成字符串
    r = - int(r)  # 返回结果

  else:
    chars.reverse()  # 逆序
    r = ''.join(chars)  # 合并成字符串
    r = int(r)  # 返回结果

  if not -pow(2, 31) <= r <= pow(2, 31) - 1:
    r = 0
  print(r)
  return r



reverse(-123)





"""
JavaScript 方法
var reverse = function(num){
   var flag = num > 0,
       newValue = 0;
   !flag && (num = -num);
   while (num > 0) {
       newValue = newValue * 10 + num % 10;
       num = Math.floor(num / 10);
   }
   !flag && (newValue = -newValue);
   return (newValue > Math.pow(2, 31) - 1 || newValue < Math.pow(2, 31) * -1) ?
                                   0 :
                                   newValue;
}

"""



