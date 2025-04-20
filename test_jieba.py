import jieba

query = "Python"
tokens = list(jieba.cut_for_search(query.lower()))
print(tokens)
