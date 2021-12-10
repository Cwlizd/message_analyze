

data=[]
count = 0 
with open('reviews.txt','r') as f:
 	for line in f:
 		data.append(line)
 		count += 1
 		x = count / 10000
 		if count % 10000 == 0:
 			print(x,'%')
print(data[0])

wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1


for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

while True:
	word = input('請輸入你想要查詢的字:')
	if word == '結束':
		break
	if word in wc:
		print(word,'出現的次數為:',wc[word])
	else:
		print('沒有這個東西歐')
print('感謝你的查詢')
	




















# print (len(data))

# new = []
# for line in data:
# 	if len(line) >= 100:
# 		new.append(line)
# print(len(new))

# good = []
# for line in data:
# 	if 'good' in line:
# 		good.append(line)
# print(len(good))
