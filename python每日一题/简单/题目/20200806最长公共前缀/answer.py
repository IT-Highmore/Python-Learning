

def longestCommonPrefix(strs):
  if not strs: return ""
  s1 = min(strs)
  s2 = max(strs)
  for i, x in enumerate(s1):
    if x != s2[i]:
      return s2[:i]
  return s1


longestCommonPrefix("flower","flow","flight")

"""
JavaScript 方法

var longestCommonPrefix = function(strs) {
    if(strs.length == 0) {
        return ""
    }
    let res = strs.reduce((x,y) =>{
        let temp = ''
        for (let i=0, j=0, leni=x.length, lenj=y.length; i<leni & j<lenj; i++,j++) {
            if (x[i] === y[j]) { temp += x[i] }
            else { break; }
        }
        return temp;
    })
    return res
};

"""



