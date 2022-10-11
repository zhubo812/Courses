line = '今天 我们 继续 学习 语料库 建设 方面 的 内容'
wordlist = line.split()

def getNGrams(wordlist, n):
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]


def counter(ngrams):
	kwicdict = {}
	for n in ngrams:
		if n[2] not in kwicdict:
			kwicdict[n[2]] = [n]
		else:
			kwicdict[n[2]].append(n)

	# print(kwicdict )
	return kwicdict

# Finally, we will want to do a bit of formatting so that our results are printed in a way that is easy to read. The code below gets all of the contexts for the keyword 'Iroquois'.

def searchWord(kwicdict):
	for key in sorted(kwicdict.keys()): 
		for val in kwicdict[key]:
			# print(type(val))
			# print(val)
			# print(val[:2])
			outstring = ' '.join(val[:2]).rjust(20)
			outstring += ' '
			outstring += ' '.join(str(val[2]).center(len(val[2])+6))
			outstring +=' '
			outstring += ' '.join(val[3:])
			print(outstring)


nglist = getNGrams(wordlist,5)
print(nglist)
counters = counter(nglist)
for counter in counters:
	print(counter,':',counters[counter])
# for k, w in countrs.items():
# 	print(k,w)

searchWord(counters)