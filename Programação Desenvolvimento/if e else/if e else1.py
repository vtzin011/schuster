idade = int(input("Digite sua idade: "))
ingresso = (input("possui ingresso senho(a)"))

if idade >= 18 and ingresso == "sim":
    print("Pode entrar")
else:
    print("não pode entrar")


estudante=(input("voce e estudante"))
idade2= int(input("voce idoso e tem mas de 60"))

if estudante == "sim" or idade > 60:
    print("Tem direito ao desconto")
else:
    print("não tem desconto")
    
login = input("qual seu login")
senha = input("qual sua senha")
bld = input("vace esta bloqueado")

if login == "admin" and senha == "1234" and bld == "nao":
    print("Acesso permitido")
else:
    print("Acesso negado")


media=float(input("qual sua media?"))
frequencia=float(input("qual sua frquencia?"))

if media >= 7 and frequencia >= 75:
    print("aprovado")
else:
    print("reprovado")

temperatura=float(input("qual a temperatura"))
pressao=float(input("qual a pressao"))
sistema=float(input("o sistema esta ativado"))
if temperatura <= 50 or pressao >= 100 and sistema == "sim":
    print("alerta ativado")
else:
    ("sistema normal")


senha2=(input("a senha esta correta?"))
funcionario=(input("voce é um funcionario"))
visitante=(input("voce é um visitante autorizado?"))
if senha2 == "sim" and (funcionario== "sim" or visitante == "sim"):
    print("voce esta conectado")
else:
    print("voce nao esta conectado")

saldo=float(input("digite seu saldo"))
valor=float(input("qual o valor da compra"))
cartao=(input("o cartao esta bloquado"))
if saldo>= valor and cartao == "nao":
    print("compra aprovada")
else:
    print("compra nao aprovada")

idade3=int(input("digite sua idade"))
auto=(input('voce tem autoriazaçao?'))
acom=(input("esta acompanhado dos pais?"))
if idade3 >= 16 or (auto == "sim" and acom == "sim"):
    print("voce pode entrar")
else:
    print("voce pode nao entrar")