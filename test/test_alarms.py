import numpy as np
from bibmon._alarms import rule_nelson_2

def test_nelson_rule_2():
    """Testa a Regra 2 de Nelson: Se 2 dos últimos 3 pontos estão acima de 2σ, deve acionar o alarme."""
    
    data = np.array([10, 12, 14, 18, 19, 21])  # Últimos 3 pontos devem ser analisados
    mean = np.mean(data[:-3])  # Média dos primeiros pontos
    std = np.std(data[:-3])  # Desvio padrão dos primeiros pontos

    expected_output = np.array([0, 0, 0, 0, 0, 1])  # O último ponto deve acionar o alarme
    output = rule_nelson_2(data, mean, std)

    assert output.tolist() == expected_output.tolist(), f"Esperado {expected_output}, mas obtido {output}"