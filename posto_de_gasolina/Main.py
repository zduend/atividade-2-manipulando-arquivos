
from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

# ==========================================
# COMBUSTÍVEIS
# ==========================================
etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# ==========================================
# VEÍCULOS
# ==========================================
carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")
caminhao = Veiculo("Carreta","VGJ-1547" )
mobilete = Veiculo("Mobilete", "GDA-4725")
chevvete = Veiculo("Chevvete", "VGK-4255")
fusca = Veiculo("Fusca", "VFD-4712")
omega = Veiculo("Omega", "ADS-5624")

# ==========================================
# ABASTECIMENTOS
# ==========================================
abastecimento1 = Abastecimento(carro,etanol,50)
abastecimento2 = Abastecimento(moto,gasolina,25)
abastecimento3 = Abastecimento(van,diesel,200)
abastecimento4 = Abastecimento(caminhao,diesel,300)
abastecimento5 = Abastecimento(mobilete, gasolina,50)
abastecimento6 = Abastecimento(chevvete, etanol, 200)
abastecimento7 = Abastecimento(fusca, gasolina, 120)
abastecimento8 = Abastecimento(omega, gasolina, 500)

# ==========================================
# LISTA DE ABASTECIMENTOS
# ==========================================
abastecimentos = [abastecimento1, abastecimento2, abastecimento3, abastecimento4, abastecimento5, abastecimento6, abastecimento7, abastecimento8]

# ==========================================
# MOSTRANDO OS ABASTECIMENTOS
# ==========================================
print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()

# ==========================================
# TOTAL DE VENDAS POR COMBUSTÍVEL
# ==========================================
total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

# ==========================================
# TOTAL DO DIA
# ==========================================
total_dia = (total_etanol + total_gasolina + total_diesel)

#===================RESOLUÇÃO===================#

with open("recibo_posto.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("=========== POSTO DE GASOLINA ==========\n")
    for abastecimento in abastecimentos:
        arquivo.write(f"{abastecimento.veiculo.modelo} - {abastecimento.veiculo.placa}\n")
        arquivo.write(f"Combustivel: {abastecimento.combustivel.nome}\n")
        arquivo.write(f"Valor: R$ {abastecimento.valor:.2f}\n")
        arquivo.write("\n")
        arquivo.write("")
    arquivo.write("========================================\n")
    arquivo.write(f"Etanol: R$ {total_etanol:.2f}\n")
    arquivo.write(f"Gasolina: R$ {total_gasolina:.2f}\n")
    arquivo.write(f"Diesel: R$ {total_diesel:.2f}\n")
    arquivo.write(f"TOTAL DO DIA: R$ {total_dia:.2f}\n")

with open("recibo_posto.txt",'r',encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

    index_etanol = conteudo.find("Etanol: R$")
    fim_index_etanol = conteudo.find("\n",index_etanol)
    valor_etanol = conteudo[index_etanol:fim_index_etanol]
    print(f"valor total gasto em {valor_etanol}")

    index_gasolina = conteudo.find("Gasolina: R$")
    fim_index_gasolina = conteudo.find("\n",index_gasolina)
    valor_gasolina = conteudo[index_gasolina:fim_index_gasolina]
    print(f"valor total gasto em {valor_gasolina}")

    index_diesel = conteudo.find("Diesel: R$")
    fim_index_diesel = conteudo.find("\n",index_diesel)
    valor_diesel = conteudo[index_diesel:fim_index_diesel]
    print(f"valor total gasto em {valor_diesel}")
    print(f"Valores gastos no dia: R$ {total_dia}")



