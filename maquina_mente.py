recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100
}
dinheiro = 0

MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "custo": 1.50,
    },
    
    "latte": {
        "ingredientes": {
            "agua": 200,
            "cafe": 24,
            "leite": 150, },
        "custo": 2.50,
    },
    
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "cafe": 24,
            "leite": 100,
        },
        "custo": 3.0
    }
}

moedas = {
    "penny": 0.01,
    "dime": 0.10,
    "nickle": 0.05,
    "quarter": 0.25
}


def recursos_reporte():
    print(f"{recursos['agua']}ml")
    print(f"{recursos['leite']}ml")
    print(f"{recursos['cafe']}g")
    print(f"Dinheiro: ${dinheiro}")

    
def recursos_suficientes(ingredientes_pedido):
    """Verifica se exite recurso suficientes para a bebida"""
    for item in ingredientes_pedido:
        if ingredientes_pedido[item] >= recursos[item]:
            print(f"Desculpa não tem {item} suficiente.")
            return False
    return True
    
def inserindo_moedas():
    """Recebe e calcula as moedas"""
    print("Por favor insira as moedas.")
    total = float(input("Quantos quarters?: ")) * moedas["quarter"]
    total += float(input("Quantos dimes?: ")) * moedas["dime"]
    total += float(input("Quantos nickles?: ")) * moedas["nickle"]
    total += float(input("Quantos pennies?: ")) * moedas["penny"]
    return round(total, 2)


def pagamento(dinheiro_inserido, valor_bebida):
    """Verifica se o dinheiro é suficiente e retorna o troco"""
    if dinheiro_inserido >= valor_bebida:
        troco = round(dinheiro_inserido - valor_bebida, 2)
        print(f"Aqui está o troco ${troco}")
        global dinheiro
        dinheiro += valor_bebida
        return True
    else:
        print("Desculpa não tem dinheiro suficiente. Coloque mais dinheiro.")
        return False
    
def fazer_cafe(nome_bebida, ingrediente_pedido):
    """Reduz os ingrediente e faz o café"""
    for item in ingrediente_pedido:
        recursos[item] -= ingrediente_pedido[item]
    print(f"Aqui está sua bebida {nome_bebida}, aproveite")
    
    