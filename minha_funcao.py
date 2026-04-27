# geral = "Essa variável posso chamar onde quiser"
# def minha_funcao():
#     print("Essa é minha função")
#     local = "Essa váriavel só pode ser só pode ser utilizada na função"
    

# #  chamando minha função
# minha_funcao()
# # print(local)
# print(geral)

# nome = "Alan" # Global

# def saudacao():
#     sobrenome = "Code" # Local
#     print(f"Olá, {nome} {sobrenome}")

# saudacao()
# print(sobrenome)

# def somar(n1, n2): # n1 e n2 são parâmetros
#     print(f"A soma é {n1 + n2}")

# somar(6, 40) # 6 e 40 são argumentos
import locale
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", ".").replace(".", ",").replace("X", ".")

# Uso:
preco_hospedagem = 1234.50
print(formatar_real(preco_hospedagem)) # R$ 49,90