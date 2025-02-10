import numpy as np

def detecOutlier(data, lim):
    """
    Detecta outliers no conjunto de dados com base em um limite.
    
    Parâmetros:
    - data: array-like -> Dados de entrada.
    - lim: float -> Limite para considerar um valor como outlier.

    Retorna:
    - Um array indicando 0 (não outlier) ou 1 (outlier).
    """
    if not isinstance(data, np.ndarray):
        data = np.array(data)  # Garantir que a entrada seja um array NumPy
    return (data > lim).astype(int)

import numpy as np

def rule_nelson_2(data, mean, std):
    """
    Nelson Rule 2: Se 2 dos últimos 3 pontos estão acima de (mean + 2σ), um alarme é acionado.

    Retorna um array de 0s e 1s indicando onde o alarme foi ativado.
    """
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    alarms = np.zeros(len(data), dtype=int)
    threshold = mean + 2 * std  # Limite para considerar anomalia

    for i in range(2, len(data)):  # Começa a análise a partir do índice 2 (pelo menos 3 pontos)
        last_3 = data[i-2:i+1]  # Pega os últimos 3 pontos

        if np.sum(last_3 > threshold) >= 2:  # Se 2 dos 3 estiverem acima do limite
            alarms[i] = 1  # Dispara o alarme no último ponto da sequência
            alarms[i-1] = 0  # Garante que o alarme não seja acionado no ponto anterior

    return alarms