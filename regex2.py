"""
regex2.py
match 对象属性演示
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search('abcdefghi',0,8) # match对象
# 属性变量
# print("正则表达式",obj.re) # 正则
# print("目标字符串",obj.string) # 目标字符串
# print("起始位置",obj.pos) # 目标字符串开始位置
# print("结束位置",obj.endpos) # 目标字符串结束位置
# print('最后一组名称:',obj.lastgroup)
# print('最后一组序号:',obj.lastindex)

# 属性方法
print('匹配内容的位置:',obj.span(),obj.start(),obj.end())
print('子组内容:',obj.groups())
print('捕获组内容:',obj.groupdict())
print('对应内容:',obj.group())
print('对应内容:',obj.group(1))
print('对应内容:',obj.group('pig'))
