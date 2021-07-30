import sys

def ler_arquivo(file_name):
	file_text = open(file_name)
	simple_string = file_text.read()
	file_text.close()
	return simple_string 

def ordenar_freq_ngram(freq, ngram):
  for i in range(len(ngram)):
    for j in range(i+1,len(ngram)):
      if freq[j] > freq[i]:
        freq_aux, ngram_aux = freq[j], ngram[j]
        freq[j], ngram[j] = freq[i], ngram[i]
        freq[i], ngram[i] = freq_aux, ngram_aux

  return freq, ngram 

def imprimir_freq_ngram(freq,ngram):
  for i in range(len(freq)):
    print(str(freq[i]) + ' - ' + ngram[i])
  
def main(file_name, n):
	string = ler_arquivo(file_name)
	ngram = []
	freq = []

	string = string.replace('\n', ' ')
	string = string.split(' ')

	for y in range(len(string)-n):
	  n_gram_aux = string[y]
	  for x in range(1,n):
	    n_gram_aux = n_gram_aux + " " + string[y+x] 
	  if n_gram_aux in ngram:
	    indice = ngram.index(n_gram_aux)
	    freq[indice] = freq[indice] + 1
	  else:
	    ngram.append(n_gram_aux)
	    freq.append(1)

	freq, ngram = ordenar_freq_ngram(freq, ngram)

	imprimir_freq_ngram(freq,ngram)

	
if __name__ == "__main__":
	n_args = len(sys.argv)
	
	if n_args != 3:
		sys.stderr.write("Não foi passado nenhum argumento\n")
		exit(1)
	elif int(sys.argv[2])<=0:
		sys.stderr.write("N menor ou igual a 0\n")
		exit(1)		
	else:
		main(sys.argv[1], int(sys.argv[2]))
