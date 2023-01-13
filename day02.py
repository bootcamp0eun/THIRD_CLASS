# Chapter 04 IF

limits = 20
tweets = "pass" * 6
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f"글자 수 {abs(diff)} 초과")


a = []
print(bool([a]))
a.append(5)
print(bool(set(a)))
# print(bool(dict(a)))
