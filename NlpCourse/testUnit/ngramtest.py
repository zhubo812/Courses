line = '今天 我们 继续 学习 语料库 建设 方面 的 内容'
wordlist = line.split()

def getNGrams(wordlist, n):#wordlist词表，n就是ngram的N
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

ngrams = getNGrams(wordlist,5)

print(ngrams)
 
