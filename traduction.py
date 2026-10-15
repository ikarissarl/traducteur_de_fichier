import pandas as pd
from pathlib import Path

class Traducteur:
    def csv_json(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_json(nom, orient="records", indent=4, force_ascii=False)

    def json_csv(self, js, nom):
        bf = pd.read_json(js)
        bf.to_csv(nom, index = False)

    def csv_excel(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_excel(nom)

    def json_excel(self, js, nom):
        bf = pd.read_json(js)
        bf.to_excel(nom, index = False)