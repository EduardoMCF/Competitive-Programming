from sys import stdin,stdout
palavras = set(['P','S','B','J','Z','V','X','p','s','b','j','z','v','x'])
while True:
	try:
		for letra in stdin.readline(): stdout.write('f') if letra in palavras else stdout.write(letra)
	except EOFError:break