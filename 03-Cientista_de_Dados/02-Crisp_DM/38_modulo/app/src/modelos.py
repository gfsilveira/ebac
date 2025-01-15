import pandas as pd
import statsmodels.formula.api as smf
from joblib import load

class Modelos:
    def __init__(self, df_final: pd.DataFrame) -> None:
        self.df_final = df_final

    def regrecao_linear(self):
        # Obtendo a primeira regreção com todas as variáveis
        formula = '''
                    renda_log ~
                    one +
                    two +
                    zero +
                    three +
                    four +
                    tempo_emprego_lowess
        '''
        reg_redc_pca = smf.ols(formula=formula, data=self.df_final).fit()

        return reg_redc_pca
    
    def load_reg_linear(self):
        link = "03-Cientista_de_Dados/02-Crisp_DM/38_modulo/app/data/reg_redc_pca"
        reg_redc_pca = load(link)
        return reg_redc_pca
        