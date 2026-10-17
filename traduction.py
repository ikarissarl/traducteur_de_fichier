import pandas as pd
from pathlib import Path
import xarray as xr
import sqlite3

def verifier_table(table):
    if not table.isidentifier():
        raise ValueError("Nom de table invalide : lettres, chiffres et _ seulement")


class Traducteur_csv:

    def csv_json(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_json(nom, orient="records", indent=4, force_ascii=False)
        document = Path(nom)
        return document

    def csv_jsonline(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_json(nom, orient="records", lines=True, force_ascii=False)
        document = Path(nom)
        return document

    def csv_excel(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_excel(nom, index=False)
        document = Path(nom)
        return document

    def csv_xml(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_xml(nom, index=False)
        document = Path(nom)
        return document

    def csv_html(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_html(nom, index=False)
        document = Path(nom)
        return document

    def csv_parquet(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_parquet(nom, index=False)
        document = Path(nom)
        return document

    def csv_feather(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_feather(nom)
        document = Path(nom)
        return document

    def csv_orc(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_orc(nom, index=False)
        document = Path(nom)
        return document

    def csv_hdf5(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_hdf(nom, key="hdf5")
        document = Path(nom)
        return document

    def csv_sql(self, cs, table, nom):
        bf = pd.read_csv(cs)
        connexion = sqlite3.connect(nom)
        bf.to_sql(table, connexion, if_exists="replace", index=False)
        connexion.close()
        document = Path(nom)
        return document

    def csv_stata(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_stata(nom, write_index=False)
        document = Path(nom)
        return document

    def csv_tsv(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_csv(nom, sep="\t", index=False)
        document = Path(nom)
        return document

    def csv_markdown(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_markdown(nom, index=False)
        document = Path(nom)
        return document

    def csv_latex(self, cs, nom):
        bf = pd.read_csv(cs)
        bf.to_latex(nom, index=False)
        document = Path(nom)
        return document


class Traducteur_json:

    def json_csv(self, js, nom):
        bf = pd.read_json(js)
        bf.to_csv(nom, index=False)
        document = Path(nom)
        return document

    def json_jsonline(self, js, nom):
        bf = pd.read_json(js)
        bf.to_json(nom, orient="records", lines=True, force_ascii=False)
        document = Path(nom)
        return document

    def json_excel(self, js, nom):
        bf = pd.read_json(js)
        bf.to_excel(nom, index=False)
        document = Path(nom)
        return document

    def json_xml(self, js, nom):
        bf = pd.read_json(js)
        bf.to_xml(nom, index=False)
        document = Path(nom)
        return document

    def json_html(self, js, nom):
        bf = pd.read_json(js)
        bf.to_html(nom, index=False)
        document = Path(nom)
        return document

    def json_parquet(self, js, nom):
        bf = pd.read_json(js)
        bf.to_parquet(nom, index=False)
        document = Path(nom)
        return document

    def json_feather(self, js, nom):
        bf = pd.read_json(js)
        bf.to_feather(nom)
        document = Path(nom)
        return document

    def json_orc(self, js, nom):
        bf = pd.read_json(js)
        bf.to_orc(nom, index=False)
        document = Path(nom)
        return document

    def json_hdf5(self, js, nom):
        bf = pd.read_json(js)
        bf.to_hdf(nom, key="hdf5")
        document = Path(nom)
        return document

    def json_sql(self, js, table, nom):
        bf = pd.read_json(js)
        connexion = sqlite3.connect(nom)
        bf.to_sql(table, connexion, if_exists="replace", index=False)
        connexion.close()
        document = Path(nom)
        return document

    def json_stata(self, js, nom):
        bf = pd.read_json(js)
        bf.to_stata(nom, write_index=False)
        document = Path(nom)
        return document

    def json_tsv(self, js, nom):
        bf = pd.read_json(js)
        bf.to_csv(nom, sep="\t", index=False)
        document = Path(nom)
        return document

    def json_markdown(self, js, nom):
        bf = pd.read_json(js)
        bf.to_markdown(nom, index=False)
        document = Path(nom)
        return document

    def json_latex(self, js, nom):
        bf = pd.read_json(js)
        bf.to_latex(nom, index=False)
        document = Path(nom)
        return document


class Traducteur_sql:

    def sql_csv(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_csv(nom, index=False)
        document = Path(nom)
        return document

    def sql_json(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_json(nom, orient="records", indent=4, force_ascii=False)
        document = Path(nom)
        return document

    def sql_jsonline(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_json(nom, orient="records", lines=True, force_ascii=False)
        document = Path(nom)
        return document

    def sql_excel(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_excel(nom, index=False)
        document = Path(nom)
        return document

    def sql_xml(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_xml(nom, index=False)
        document = Path(nom)
        return document

    def sql_html(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_html(nom, index=False)
        document = Path(nom)
        return document

    def sql_parquet(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_parquet(nom, index=False)
        document = Path(nom)
        return document

    def sql_feather(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_feather(nom)
        document = Path(nom)
        return document

    def sql_orc(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_orc(nom, index=False)
        document = Path(nom)
        return document

    def sql_hdf5(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_hdf(nom, key="hdf5")
        document = Path(nom)
        return document

    def sql_stata(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_stata(nom, write_index=False)
        document = Path(nom)
        return document

    def sql_tsv(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_csv(nom, sep="\t", index=False)
        document = Path(nom)
        return document

    def sql_markdown(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_markdown(nom, index=False)
        document = Path(nom)
        return document

    def sql_latex(self, bd, table, nom):
        verifier_table(table)
        connexion = sqlite3.connect(bd)
        bf = pd.read_sql_query(f"SELECT * FROM {table}", connexion)
        connexion.close()
        bf.to_latex(nom, index=False)
        document = Path(nom)
        return document


class Traducteur_netcdf4:

    def netcdf_csv(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_csv(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_json(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_json(nom, orient="records", indent=4, force_ascii=False)
        document = Path(nom)
        return document

    def netcdf_jsonline(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_json(nom, orient="records", lines=True, force_ascii=False)
        document = Path(nom)
        return document

    def netcdf_excel(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_excel(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_xml(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_xml(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_html(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_html(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_parquet(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_parquet(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_feather(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_feather(nom)
        document = Path(nom)
        return document

    def netcdf_orc(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_orc(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_hdf5(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_hdf(nom, key="hdf5")
        document = Path(nom)
        return document

    def netcdf_sql(self, nc, table, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        connexion = sqlite3.connect(nom)
        bf.to_sql(table, connexion, if_exists="replace", index=False)
        connexion.close()
        document = Path(nom)
        return document

    def netcdf_stata(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_stata(nom, write_index=False)
        document = Path(nom)
        return document

    def netcdf_tsv(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_csv(nom, sep="\t", index=False)
        document = Path(nom)
        return document

    def netcdf_markdown(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_markdown(nom, index=False)
        document = Path(nom)
        return document

    def netcdf_latex(self, nc, nom):
        ds = xr.open_dataset(nc)
        bf = ds.to_dataframe().reset_index()
        bf.to_latex(nom, index=False)
        document = Path(nom)
        return document


class Traducteur_parquet:

    def parquet_csv(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_csv(nom, index=False)
        document = Path(nom)
        return document

    def parquet_json(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_json(nom, orient="records", indent=4, force_ascii=False)
        document = Path(nom)
        return document

    def parquet_jsonline(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_json(nom, orient="records", lines=True, force_ascii=False)
        document = Path(nom)
        return document

    def parquet_excel(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_excel(nom, index=False)
        document = Path(nom)
        return document

    def parquet_xml(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_xml(nom, index=False)
        document = Path(nom)
        return document

    def parquet_html(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_html(nom, index=False)
        document = Path(nom)
        return document

    def parquet_feather(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_feather(nom)
        document = Path(nom)
        return document

    def parquet_orc(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_orc(nom, index=False)
        document = Path(nom)
        return document

    def parquet_hdf5(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_hdf(nom, key="hdf5")
        document = Path(nom)
        return document

    def parquet_sql(self, pq, table, nom):
        bf = pd.read_parquet(pq)
        connexion = sqlite3.connect(nom)
        bf.to_sql(table, connexion, if_exists="replace", index=False)
        connexion.close()
        document = Path(nom)
        return document

    def parquet_stata(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_stata(nom, write_index=False)
        document = Path(nom)
        return document

    def parquet_tsv(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_csv(nom, sep="\t", index=False)
        document = Path(nom)
        return document

    def parquet_markdown(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_markdown(nom, index=False)
        document = Path(nom)
        return document

    def parquet_latex(self, pq, nom):
        bf = pd.read_parquet(pq)
        bf.to_latex(nom, index=False)
        document = Path(nom)
        return document