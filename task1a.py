def hist(book):
	d=dict()
	fin=open(book)
	for lines in fin:
		line=lines.strip()
		for c in line.split():
			if c not in  d:

				d[c]=1
			else:
				d[c]+=1
	return d



def unique_words(book):
	fin=open(book)
	d=dict()
	for lines  in fin:
		line=lines.strip()
		for c in line.split():
			if c not in  d:

				d[c]=1
		else:
			d[c]+=1	
	mylist=list(d.keys())
	return(mylist)
print(unique_words('Book1.txt'))
print(unique_words('Book2.txt'))
print(unique_words('Book3.txt'))


f1=unique_words('Book1.txt')
f2=unique_words('Book2.txt')
f3=unique_words('Book1.txt')



def count_words():
	print('Total words in Book1: ',len(f1),'Total words in Book2: ',len(f2),'Total words in Book3: ',len(f3),sep='\n')
count_words()


def sorted_words():
	l1=sorted(f1,key=len)
	print(l1[::-1])
	l2=sorted(f2,key=len)
        print(l2[::-1])
	l3=sorted(f3,key=len)
        print(l3[::-1]
sorted_words()


def character_word_count():
	print(hist('Book1.txt')
	print(hist('Book2.txt')
	print(hist('Book3.txt')
character_word_count()


def starts_with_vow(file):
	mylist=[]
	t=(a,e,i,o,u)
	for char in t:
		for words in file:
			if words[0]==char:
				mylist.append(words)
			else:
				pass
	print(len(mylist))
starts_with_vow(f1)
starts_with_vow(f2)
starts_with_vow(f3)
