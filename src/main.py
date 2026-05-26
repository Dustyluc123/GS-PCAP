# Módulo de Automação de Telemetria - GS FIAP

def coletar_dados():
    # Aqui vamos definir a matriz de dados (Ex: Ciclo 1, Temp, Com, Bat, Ox, Est)
    dados = [
        [1, 25.5, 98, 85, 21, 0.95],
        # ... outros ciclos
    ]
    return dados

def analisar_risco(dados):
    # Lógica de if/else para classificar os dados
    print("Analisando telemetria...")

def gerar_relatorio(dados_analisados):
    # Lógica para exibir o resultado final no terminal
    print("--- Relatório Final da Missão ---")

def main():
    print("Iniciando sistema de monitoramento...")
    telemetria = coletar_dados()
    analise = analisar_risco(telemetria)
    gerar_relatorio(analise)

if __name__ == "__main__":
    main()