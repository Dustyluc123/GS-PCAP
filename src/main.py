# ====================================================================
# MISSION CONTROL AI - FIAP A MARTE
# ====================================================================

# Configurações Globais da Missão
NOME_MISSAO = "FIAP a Marte"
EQUIPE = "AstroDusty Barreto"

AREAS_MONITORADAS = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

NOMES_CURTOS = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]

# 1. FUNÇÃO: Obter Dados da Missão
def obter_dados_missao():
    return [
        [24, 92, 88, 96, 90],
        [27, 80, 72, 94, 85],
        [31, 65, 58, 91, 70],
        [36, 42, 38, 87, 55],
        [39, 28, 19, 78, 35],
        [34, 55, 32, 82, 50]
    ]

# 2. FUNÇÃO: Classificar Parâmetro Individual
def classificar_parametro(indice, valor):
    """
    Retorna uma tupla: (Status, Pontuação, Mensagem de Status, Recomendação)
    """
    # 0: Temperatura
    if indice == 0:
        if valor < 18: return "ATENÇÃO", 1, "Temperatura baixa", "Ajustar aquecimento térmico"
        elif valor <= 30: return "NORMAL", 0, "Temperatura estável", ""
        elif valor <= 35: return "ATENÇÃO", 1, "Temperatura elevada", "Verificar controle térmico da missão"
        else: return "CRÍTICO", 2, "Risco de superaquecimento", "Acionar resfriamento de emergência"
        
    # 1: Comunicação
    elif indice == 1:
        if valor < 30: return "CRÍTICO", 2, "Comunicação com a base em nível crítico", "Priorizar restauração de sinal"
        elif valor <= 59: return "ATENÇÃO", 1, "Comunicação instável", "Realinhar antenas de transmissão"
        else: return "NORMAL", 0, "Comunicação estável", ""
        
    # 2: Bateria
    elif indice == 2:
        if valor < 20: return "CRÍTICO", 2, "Bateria em nível crítico", "Desativar módulos não essenciais"
        elif valor <= 49: return "ATENÇÃO", 1, "Bateria abaixo do recomendado", "Reduzir consumo de energia"
        else: return "NORMAL", 0, "Energia estável", ""
        
    # 3: Oxigênio
    elif indice == 3:
        if valor < 80: return "CRÍTICO", 2, "Oxigênio em nível crítico", "Acionar tanques de O2 reservas"
        elif valor <= 89: return "ATENÇÃO", 1, "Oxigênio abaixo do ideal", "Inspecionar purificadores de ar"
        else: return "NORMAL", 0, "Oxigênio adequado", ""
        
    # 4: Estabilidade
    elif indice == 4:
        if valor < 40: return "CRÍTICO", 2, "Estabilidade operacional crítica", "Ativar giroscópios de emergência"
        elif valor <= 69: return "ATENÇÃO", 1, "Estabilidade operacional reduzida", "Ajustar propulsores de manobra"
        else: return "NORMAL", 0, "Estabilidade operacional adequada", ""

# 3. FUNÇÃO: Formatação Visual de Medidas
def formatar_medida(indice, valor):
    if indice == 0:
        return f"{valor} °C"
    return f"{valor}%"

# 4. FUNÇÃO PRINCIPAL E DE RELATÓRIOS
def main():
    dados = obter_dados_missao()
    total_ciclos = len(dados)
    
    pontuacoes_por_ciclo = []
    classificacoes_por_ciclo = []
    acumulado_por_area = [0, 0, 0, 0, 0]
    
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {EQUIPE}")
    print(f"Quantidade de ciclos analisados: {total_ciclos}")
    print("=" * 60)
    
    # Processamento dos Ciclos
    for c_idx, ciclo in enumerate(dados):
        print(f"CICLO {c_idx + 1}")
        print("-" * 60)
        
        pontuacao_ciclo = 0
        recomendacoes_ciclo = []
        teve_critico = False
        
        for i in range(len(ciclo)):
            valor = ciclo[i]
            status, pontos, msg, rec = classificar_parametro(i, valor)
            
            pontuacao_ciclo += pontos
            acumulado_por_area[i] += pontos
            
            if status == "CRÍTICO": teve_critico = True
            if rec != "": recomendacoes_ciclo.append(rec)
                
            nome_campo = NOMES_CURTOS[i]
            medida_formatada = formatar_medida(i, valor)
            print(f"{nome_campo}: {medida_formatada} | {status} | {msg}")
            
        # Classificação do Ciclo
        if pontuacao_ciclo >= 6 or teve_critico:
            classificacao = "MISSÃO CRÍTICA"
        elif pontuacao_ciclo >= 3 or (pontuacao_ciclo >= 1 and not teve_critico):
            # Para seguir exatamente seu exemplo: se tiver atenção sem crítico e for baixa pontuação
            # Ajustamos a regra: <= 2 pontos sem crítico é estável
            if pontuacao_ciclo <= 2:
                classificacao = "MISSÃO ESTÁVEL"
            else:
                classificacao = "MISSÃO EM ATENÇÃO"
        else:
            classificacao = "MISSÃO ESTÁVEL"
            
        pontuacoes_por_ciclo.append(pontuacao_ciclo)
        classificacoes_por_ciclo.append(classificacao)
        
        # Gerar Recomendação Concatenada
        if not recomendacoes_ciclo:
            texto_recomendacao = "Manter operação normal e continuar monitoramento."
        else:
            texto_recomendacao = " + ".join(recomendacoes_ciclo)
            
        print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {texto_recomendacao}")
        
    
    # ==========================================
    # CÁLCULOS FINAIS PARA O RELATÓRIO
    # ==========================================
    medias = []
    for i in range(5):
        soma_coluna = sum(ciclo[i] for ciclo in dados)
        medias.append(soma_coluna / total_ciclos)
        
    ciclo_mais_critico = pontuacoes_por_ciclo.index(max(pontuacoes_por_ciclo)) + 1
    maior_pontuacao = max(pontuacoes_por_ciclo)
    risco_medio = sum(pontuacoes_por_ciclo) / total_ciclos
    qtd_criticos = classificacoes_por_ciclo.count("MISSÃO CRÍTICA")
    
    # Tendência
    if pontuacoes_por_ciclo[-1] > pontuacoes_por_ciclo[0]:
        tendencia = "A missão apresentou tendência de piora."
    elif pontuacoes_por_ciclo[-1] < pontuacoes_por_ciclo[0]:
        tendencia = "A missão apresentou tendência de melhora."
    else:
        tendencia = "A missão manteve-se estável."
        
    # Área mais afetada
    max_acumulado = max(acumulado_por_area)
    indice_area_afetada = acumulado_por_area.index(max_acumulado)
    nome_area_afetada = AREAS_MONITORADAS[indice_area_afetada]
    
    # Conclusão dinâmica
    if classificacoes_por_ciclo[-1] == "MISSÃO ESTÁVEL":
        conclusao = "A missão ocorreu dentro dos parâmetros esperados com total controle dos sistemas."
    else:
        conclusao = "A missão apresentou instabilidade relevante durante a operação. Apesar da tentativa de recuperação no último ciclo, ainda existem sistemas em atenção e a equipe deve manter o plano de contingência ativo."

    # Impressão do Relatório Final
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {EQUIPE}")
    print(f"Quantidade de ciclos analisados: {total_ciclos}")
    print(f"Média de temperatura: {medias[0]:.2f} °C")
    print(f"Média de comunicação: {medias[1]:.2f}%")
    print(f"Média de bateria: {medias[2]:.2f}%")
    print(f"Média de oxigênio: {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_pontuacao}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")
    print("Tendência da missão:")
    print(tendencia)
    print("Pontuação acumulada por área:")
    for i in range(5):
        print(f"{AREAS_MONITORADAS[i]}: {acumulado_por_area[i]} pontos")
    print("Área mais afetada:")
    print(nome_area_afetada)
    print("Classificação final da missão:")
    print(classificacoes_por_ciclo[-1])
    print("Conclusão:")
    print(conclusao)

if __name__ == "__main__":
    main()