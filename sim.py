meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "67":"ser chato sem sentido",
            "BOBÃO": "chingamento muito forte e de baixo calão",
            "OK": "ela com certeza esta brava",
            "S" abreviação de uma palavra DE 3 LETRAS JA QUE A PESSOA QUE ESCREVE ISSO NÃO TEM TEMPO O SUFICIENTE DE MANDA UMA PALAVRA DESSE INCRIVEL TAMANHO (a palavra é sim)"
            }
word= input ("digite uma palavra moderna que voce nao entende (escreva todas as palavras em letras maiusculas")
if word in meme_dict.keys():
    # O que devemos fazer se a palavra for encontrada?
    print(meme_dict[word])
else:
    # O que devemos fazer se a palavra não for encontrada?
    print("palavra nao encontrada no dicionario")
