import pandas as pd
import os

diretorio_atual = os.getcwd()

def extract_excel(name, **kwargs):
    file_path = os.path.join(diretorio_atual, "data", "input", name)
    df = pd.read_excel(file_path, **kwargs)

    return df