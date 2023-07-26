from maquina_mente import *
dinheiro = 0

maquina_ligada = True
while maquina_ligada:
    escolha = input("Qual você gostaria? (espresso/latte/cappuccino): ")
    
    if escolha == "off":
        maquina_ligada = False
    elif escolha == "status":
        recursos_reporte()
    else:
        bebida = MENU[escolha]
        if recursos_suficientes(bebida["ingredientes"]):
            dinheiro = inserindo_moedas()
            if pagamento(dinheiro, valor_bebida=bebida["custo"]):
                fazer_cafe(escolha, bebida["ingredientes"])

print("Bye, bye")
