odd = [i for i in range(46,124) if i%2 !=0]
print(odd)

square= [x**2 for x in range(1, 6)]
print(square)

words = ("cat","elephant","dog","python")
lengths = [len(word) for word in words]
print(lengths)