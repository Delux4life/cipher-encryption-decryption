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
