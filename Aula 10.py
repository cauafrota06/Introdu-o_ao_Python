#lista mista

listaMista = [1,"oi", 3.14, True]
listasDeListas = [listaMista [ 1, 2, 3]]


lista_vazia = list ()
outraListaVAzia = []
listaNumeros = list(range(4))
listaCaracteres = list('Python')
#Resultado = [ 'P','y', 't', 'h', 'o', 'n')

listaCaracteres [2] #acessa a letra 't'
listaCaracteres [-1] #acessa o último

#metodos de listas

listaNumeros.append(4) #acrescenta (int 4) no final
listaNumeros.remove(0) #remove o item pelo valor (1°que achar por padrao, por vc não ter colocado um valor index)
listaNumeros.pop(1) #retira porém vcpode guardar o número retirado
listaNumeros.pop() #por padrao, deleta o último item

listaCaracteres.index('y') #me diz qual a posição do Y/ dá o numero do index do Y

len(listaCaracteres) #retorna o numero de elementos da lista
print(len(listaCaracteres))

print('-'*30)

#TUPLAS (Imutáveis)

tuplaNumeros = tuple(listaNumeros)
outraTuplaNumeros = (5, 6, 7, 8, 9)
tuplaMista = (1, "oi", 3.14, True)

#Metodos de Tupla
tuplaNumeros.count(1) #conta quantos (1) tem na tupla
tuplaMista.index('oi')

#DICIONÁRIOS
# pares de   'chave':'valor'
dictPessoa = {"nome": "Gustavo", "idade":25} #tem 2 elementos
dictPessoa["nome"] #acessa o valor através da chave
dictPessoa [cidade] = "Manaus"
dictPessoa.get('idade') #mais seguro, não quebra se não houver

#Metodos de dict
dictPessoa.get('idade',0) # caso não ache o valor padrão será 0
dictPessoa.keys() #retorna todas as chaves
#resposta = ['nome', 'idade', 'cidade']
dictPessoa.values () #retorna os valores
#resposta= ('Gustavo', 25, 'Manaus')
dictPessoa.itens() #retorna pares (chaves, valor)
#resposta = [( 'nome', 'Gustavo'), ('idade',25), ('cidade', Manaus)
