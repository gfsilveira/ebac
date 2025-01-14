import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from scipy.stats import t, ks_2samp
from scipy.interpolate import interp1d
import statsmodels.api as sm


class PepilineProprio:
    def modifica_variaveis(self, df_modif: pd.DataFrame) -> pd.DataFrame:
        df_modif['renda_log'] = np.log(df_modif['renda'])

        # Define a suavização dos dados na variável lowess
        lowess_train = sm.nonparametric.lowess(df_modif['renda_log'], df_modif['tempo_emprego'], frac=1/9)

        # Valores de X e Y suavizados
        f_train = interp1d(lowess_train[:, 0], lowess_train[:, 1], bounds_error=False)

        df_modif.loc[:, 'tempo_emprego_lowess'] = f_train(df_modif['tempo_emprego'])

        return df_modif

    def substitui_nulos(self, valores_substituir: list) -> list:
        # Substituir nulos
        df_copy_sub = valores_substituir[0]
        variavel_sub = "tempo_emprego"
        df_copy_sub.fillna({variavel_sub: np.mean(df_copy_sub[variavel_sub])}, inplace=True),
        retorno = (
            df_copy_sub,
            valores_substituir[1]
        )
        return retorno

    def remove_outliers(self, valores_remove: list) -> pd.DataFrame:
        # Remoção de outliers
        df_train_val = valores_remove[0]
        reg_redc_summary_frame = valores_remove[1]
        remov_index_max = reg_redc_summary_frame['hat_diag'].max()
        remov_index = reg_redc_summary_frame[reg_redc_summary_frame['hat_diag'] == remov_index_max]['hat_diag'].index
        try:
            df_train_outliers = df_train_val.drop(remov_index)
        except:
            df_train_outliers = df_train_val.copy()

        return df_train_outliers


    def cria_dummies(self, df_train_outliers: pd.DataFrame) -> list:
        # Criação de Dummie
        selecionar = [
            "sexo",
            "posse_de_veiculo",
            "posse_de_imovel",
            "tipo_renda",
            "educacao",
            "estado_civil",
            "tipo_residencia",
        ]
        df_train_outliers_dummies = pd.get_dummies(df_train_outliers[selecionar], drop_first=True)
        df_train_outliers = self.modifica_variaveis(df_train_outliers)
        return (df_train_outliers_dummies, df_train_outliers)

    def cria_pca(self, valores_pca: list):
        # PCA
        df_train_outliers_dummies = valores_pca[0]
        df_train_outliers = valores_pca[1]
        pca = pd.DataFrame(PCA(n_components=5).fit_transform(df_train_outliers_dummies))
        pca['tempo_emprego_lowess'] = df_train_outliers['tempo_emprego_lowess'].values
        pca['renda_log'] = df_train_outliers['renda_log'].values
        pca.rename(
                columns={
                    0: "zero",
                    1: "one",
                    2: "two",
                    3: "three",
                    4: "four",
                },
                inplace=True    
        )
        return pca
    
    def inicia_rotina(self) -> None:
        rotina_pipe = Pipeline(
            steps=[
                ("substitui_nulos", FunctionTransformer(self.substitui_nulos)),
                ("remove_outliers", FunctionTransformer(self.remove_outliers)),
                ("cria_dummies", FunctionTransformer(self.cria_dummies)),
                ("cria_pca", FunctionTransformer(self.cria_pca))
            ]
        )
        return rotina_pipe