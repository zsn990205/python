
# 2.实现单词的逆序
def reverseWords(s: str):
    # 使用空格对字符串进行分隔
    tokens = s.split(' ')
    # 对上述分隔好的列表进行反转
    tokens.reverse()
    # 把用空格分隔并且反转好的列表进行拼接
    return ' '.join(tokens)


# print(f'反转后的结果是{reverseWords("i am a student")}')


# 3.旋转字符串
def retortStr(s, goal):
# 假如说要旋转的字符串和目标字符串的长度不一致直接判错
    if len(s) != len(goal):
        return False
# 合并后的字符串是否有目标字符串
    return goal in s + s

# print(retortStr('abcde', 'eabcd'))
# print(retortStr('abcde', 'ewbcd'))


# 4.统计字符串前缀
def countPreStr(words: list, s: str):
    count = 0
    for word in words:
    # s是以word开头
       if s.startswith(word):
           count += 1
    return count

print(countPreStr(['a', 'b', 'c', 'ab', 'bc', 'abc'], 'abc'))
print(countPreStr(['a', 'a'], 'aa'))