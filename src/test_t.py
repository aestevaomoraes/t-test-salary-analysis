import numpy as np
from scipy.stats import ttest_ind


def executar_teste(grupo_child, grupo_adult, alpha=0.05):
    """
    Teste t unilateral:
    H0: média_child = média_adult
    H1: média_child > média_adult
    """

    t_stat, p_value_bilateral = ttest_ind(
        grupo_child, grupo_adult, equal_var=False
    )

    p_value = p_value_bilateral / 2

    decisao = "Rejeitar H0" if p_value <= alpha else "Não rejeitar H0"

    return t_stat, p_value, decisao


if __name__ == "__main__":
    np.random.seed(42)

    salarios_child = np.random.normal(132000, 255000, 885)
    salarios_adult = np.random.normal(111000, 271000, 1376)

    t_stat, p_value, decisao = executar_teste(
        salarios_child, salarios_adult
    )

    print(f"t-stat: {t_stat:.4f}")
    print(f"p-value: {p_value:.6f}")
    print(f"Decisão: {decisao}")
