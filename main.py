from zipfile import ZipFile
from pandas_plink import read_plink
import pandas as pd

# download data
DATA_URL = "https://easygwas.ethz.ch/down/dataset/download/1/"


def extract():
    with ZipFile("AtPolyDB_(call_method_75__Horton_et_al).zip") as myzip:
        myzip.extractall()


# plink --file genotype


def phenotypes():
    return pd.read_csv("phenotypes.pheno", sep=" ")


def main():
    g = read_plink("plink")
    return g


if __name__ == "__main__":
    main()
