msg=list()
mcount=list()
txt=input('Enter Text : ')
txt=txt.lower()
for i in range(1,26):
	fname='cipher'+str(i)+'.txt'
	cipher=''
	for letter in txt:
		if letter == ' ' or letter=='.' or letter == '!' or letter == '@' or letter == '#' or letter == '$' or letter == '%' or letter == '&' or letter == '*' or letter == '(' or letter == ')' or letter == '[' or letter == ']' or letter == '{' or letter == '}' or letter == '?' or letter == ',' or letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9' or letter == '0':
			cipher=cipher+letter
		else:
			count=0
			fhand=open('cipher0.txt')
			for word in fhand:
				word=word.strip()
				letter=letter.strip()
				if word == letter:
					fhand1=open(fname)
					count1=0
					for word1 in fhand1:
						word1=word1.strip()
						if count1==count:
							cipher=cipher+word1
						count1+=1
					fhand1.close()
				count+=1
			fhand.close()
	print(26-i,' Original text :',cipher)
	temp=cipher.split(' ')
	pcount=0
	symbols=['!','@','#','$','%','&','*','(',')','-','_','+','=','{','}','[',']',':','1','2','3','4','5','6','7','8','9','0',',','.','?']
	for item in temp:
		for symbol in symbols:
			if symbol in item:
				item1=item.split(symbol)
				for item2 in item1:
					fword=open('word.txt')
					for fword1 in fword:
						fword1=fword1.strip()
						if fword1==item2:
							pcount+=1
					fword.close()
		fword=open('word.txt')
		for fword1 in fword:
			fword1=fword1.strip()
			if fword1==item:
				pcount+=1
		fword.close()
	print('Accuracy : ',pcount,'\n')
	msg.append(cipher)
	mcount.append(pcount)

temp=0
for count in mcount:
	if count>temp:
		temp=count
print()
print('Most Accurate Message :')
print()
ap=0
for count in mcount:
	if count==temp:
		print('Shift : ',26-(ap+1))
		print('Message : ',msg[ap])
		print('Accuracy : ',mcount[ap])
		print()
	ap+=1
