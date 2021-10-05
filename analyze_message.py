

data=[]
count = 0 
with open('reviews.txt','r') as f:
 	for line in f:
 		data.append(line)
 		count += 1
 		x = count / 10000
 		if count % 10000 == 0:
 			print(x,'%')

print (len(data[0]))

