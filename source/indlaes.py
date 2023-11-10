# Import af standard pakker
import pandas as pd
import numpy as np
import re

from os.path import join
from shutil import copy2

# Import af egne pakker
import constants.constants as c
from source.help_funcs import maaned, pdf_exist


# Function der modtager en serie->række fra månedsstatistik oversigten
# cellen rk[c.NAVNEKOL] indeholder medarbejdernavn og -initialer i parentes
# Funktionen returnere initialerne i småbogstaver
# returnere "xxx" hvis der ikke er initialer i parentes i rk[c.NAVNEKOL]
def ini(rk):
    match = re.search(r"\((.*?)\)", rk[c.NAVNEKOL])

    if match:
        tekst_i_parentes = match.group(1)
        return tekst_i_parentes.upper()
    else:
        return "xxx"


def laes_excelark(filnavn):
    return pd.read_excel(filnavn, sheet_name=c.SHEETNAVN)


def tilpas_df(df):
    df.fillna(0, inplace=True)
    df[c.AARKOL] = df[c.AARKOL].astype(int)
    filt = df[c.NAVNEKOL] == 0
    skalslettes = df.loc[filt]
    df.drop(skalslettes.index, inplace=True)
    df[c.INIKOL] = df.apply(ini, axis=1)
    return df


def lav_udtrak_df(df):
    filt = df[c.AARKOL] == c.AARSTAL

    return df.loc[filt]


def lav_navne_list(df):
    navne_list = []
    kol_list = df.columns
    kol_jan = 0  # Kolonne nr. for Januar-måned

    for kol in kol_list:
        if kol.lower() == c.JANKOL:
            break
        kol_jan += 1

    for rk in df.index:
        for kol in kol_list[kol_jan : kol_jan + 12]:
            if df.loc[rk, kol] > 0:
                navne_list.append(
                    df.loc[rk, c.INIKOL]
                    + "_"
                    + maaned(kol)
                    + "_"
                    + str(df.loc[rk, c.AARKOL])
                )

    return navne_list


def lav_kopi_timesedler(project):
    findesikke = 0
    kopieret = 0
    for navn in project.navneliste:
        sourcefil = join(project.sourcepath, navn + ".pdf")
        if not pdf_exist(sourcefil):
            findesikke += 1
            print(f"****\t{navn}  -- findes ikke i MaandesStatistik\t****")
        else:
            destinafil = join(project.destinationpath, navn + ".pdf")
            if not pdf_exist(destinafil):
                kopieret += 1
                print(f"{navn} kopieret til bilagsmappen")
                copy2(sourcefil, destinafil)

    print(f"I alt mangler der: {findesikke} timesedler i MaandesStatistik")
    print(f"I alt blev: {kopieret} timesedler kopieret")
    return


def kontroller_timesedler(project):
    findesikke = 0
    for navn in project.navneliste:
        sourcefil = join(project.sourcepath, navn + ".pdf")
        if not pdf_exist(sourcefil):
            findesikke += 1
            print(navn + " -- findes ikke i MaandesStatistik")
    print(f"I alt mangler der: {findesikke} timesedler")
    return


def kor(proj="test"):
    match proj.lower():
        case "kontrol":
            project = c.Kontrol()
        case "bet":
            project = c.Bet()
        case "coast":
            project = c.Coast()
        case "hoj":
            project = c.Hoj()
        case "wad":
            project = c.Wadsea()
        case _:
            print(
                "Ugyldig projektnavn - Kontrol/Bet/Coast/4Fit/Hoj/Natman/Open/Orchid/Wad"
            )
            return

    maanedsstatistik = laes_excelark(project.filpath)
    maanedsstatistik = tilpas_df(maanedsstatistik)
    udtrak = lav_udtrak_df(maanedsstatistik)
    project.navneliste = lav_navne_list(udtrak)

    if proj.lower() == "kontrol":
        kontroller_timesedler(project)
    else:
        lav_kopi_timesedler(project)

    return
