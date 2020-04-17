#Author: Lucas Pereira Torres de Araujo
#Lista 4 - FUP's Class - 2016.1
#Item 6

vetor = []
sen = 0

x = input("Digite o valor de X: ")

x = x * (float(3.141592))/180

for i in xrange(1,16):
	fat = 1
	for j in xrange(2,(2*i-1)):
		fat = fat*j

	if i%2 == 0:
		sen = sen - (x**(2*i-1))/fat #TermoPAR
		vetor.insert(i, (-(x**(2*i-1))/fat))
	else:
		sen = sen + (x**(2*i-1))/fat #TermoIMPAR
		vetor.insert(i, (+(x**(2*i-1))/fat))

print "Sen(",x*180/(float(3.141592)),") = ",sen
