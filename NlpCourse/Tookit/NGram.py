
wordlist = ['1','2','3','4','5','6']

def getNGrams(wordlist, n):
    return [ wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

nglist = getNGrams(wordlist,3)
print(nglist)

for item in nglist:
    print(''.join(item))