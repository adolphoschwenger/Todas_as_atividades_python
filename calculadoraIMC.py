# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para categorizar o IMC
def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Função principal
def main():
    print("Calculadora de IMC")
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        imc = calcular_imc(peso, altura)
        categoria = categoria_imc(imc)
        
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Categoria: {categoria}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos para peso e altura.")

# Executa a função principal
if __name__ == "__main__":
    main()