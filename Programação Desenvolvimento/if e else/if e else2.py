nota_prova=float(input("qual sua nota da prova"))
nota_projeto=float(input("qual sua nota do projeto"))
frequencia=int(input("qual sua frequencia"))
media= (nota_prova+nota_projeto) / 2

if media >= 7 and frequencia >= 75:
    print("aprovado com merito")

elif frequencia < 75:
    print("vooce foi reprovado, por falta, volte a escola ")

else:
    print("voce esta na recuperacao, se esforce ")

idade=int(input("qual sua idade meu chegado"))
parabens=(input("voce possui o premium"))

if parabens == "sim":
    print("voce em acesso a conteudos deliciosos")
elif idade <= 12 :
    print("voce pode assistir conteudo de criança")
elif idade <= 17:
    print("voce pode assistir conteudo de adolecente")
elif idade >= 18:
    print("voce ja pode assistir conteudo adulto")


