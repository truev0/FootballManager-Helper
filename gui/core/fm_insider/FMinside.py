# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import warnings

import numpy as np
import pandas as pd

from gui.core.dicts import en, es
from gui.core.models.CustomNestedNamespace.py_CustomNestedNamespace import (
    NestedNamespace,
)

# INITIAL CONFIGURATION TO PROCESS
# ///////////////////////////////////////////////////////////////
warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
# List for interpretation, if wanna add another lang should be here
text = {}
text.update({"en": NestedNamespace(en.column_headers)})
text.update({"es": NestedNamespace(es.column_headers)})


# SETTING PANDAS
# Load file to create the dataframe
# ///////////////////////////////////////////////////////////////
def setting_up_pandas(path_file):
    """
    This function sets up the pandas dataframe for the squad and scouting files

    :param path_file: This is the path to the file you want to load
    :return: The dataframe is being returned.
    """
    pd.set_option("styler.render.max_columns", 100)
    pd.set_option("styler.render.max_rows", 100)
    pd.set_option("styler.format.precision", 0)
    # LOADING FILE
    try:
        droppers = ["Inf", "Rec"]
        html_filename = f"{path_file}"
        df_fmi = pd.read_html(html_filename, encoding="utf-8")[0]

        if "Inf" in df_fmi.columns:
            prevent_dash = [
                df_fmi.columns[i] for i in range(46, 93)
            ]
            prevent_dash.append(df_fmi.columns[2])
            for _, element in enumerate(prevent_dash):
                if element == df_fmi.columns[2]:
                    n = df_fmi[element].str.split(' - ', expand=True)
                    df_fmi[element] = n[0]
                else:
                    s = df_fmi[element].astype(str).str.split('-', expand=True)
                    df_fmi[element] = np.floor(s[s != ''].astype(float).mean(1).fillna(0))
            for _, element in enumerate(droppers):
                if element in df_fmi.columns:
                    df_fmi.drop(element, axis=1, inplace=True)

    except ValueError:
        return None
    except FileNotFoundError:
        return None
    return df_fmi


# CONVERT VALUES TO ITS RESPECTIVE TYPE
# Convert value to str, float, int / replace text in number cells
# ///////////////////////////////////////////////////////////////
def convert_values(df):
    """
    It converts the values in the dataframe to the correct data type

    :param df: the dataframe you want to convert
    :return: A dataframe with the columns converted to the correct data type.
    """
    for column in [df.columns[9], df.columns[10], df.columns[35]]:
        if column in [df.columns[35]]:
            df[column] = df[column].astype(str).str.replace("km", "")
            df[column] = df[column].str.replace("-", "0")
            df[column] = df[column].str.replace(",", ".")
        else:
            df[column] = df[column].str.replace("N/A", "0")
            df[column] = df[column].str.replace("N/D", "0")
            df[column] = df[column].str.replace("$", "")
            df[column] = df[column].str.replace("£", "")
            df[column] = df[column].str.replace("¥", "")
            df[column] = df[column].str.replace("€", "")
            df[column] = df[column].str.replace("₺", "")
            df[column] = df[column].str.replace("₽", "")
            df[column] = df[column].str.replace("AED", "")
            df[column] = df[column].str.replace("BGN", "")
            df[column] = df[column].str.replace("CHF", "")
            df[column] = df[column].str.replace("Â", "")
            df[column] = df[column].str.replace("p/a", "")
            df[column] = df[column].str.replace("p/m", "")
            df[column] = df[column].str.replace("p/s", "")
            df[column] = df[column].str.replace("p/w", "")
            df[column] = df[column].str.replace(",", "")
            df[column] = df[column].str.replace("K", "000")
            df[column] = df[column].str.replace(".", "")
            df[column] = df[column].str.replace("M", "00000")
            df[column] = df[column].str.replace("m", "000")

    for column in [
        df.columns[17],
        df.columns[14],
        df.columns[13],
        df.columns[26],
        df.columns[30],
        df.columns[33],
        df.columns[21],
        df.columns[25],
        df.columns[23],
        df.columns[12],
        df.columns[27],
        df.columns[28],
        df.columns[34],
        df.columns[15],
        df.columns[40],
        df.columns[41],
        df.columns[39],
        df.columns[16],
        df.columns[19],
        df.columns[22],
        df.columns[29],
        df.columns[31],
        df.columns[32],
        df.columns[43],
        df.columns[20],
        df.columns[38],
        df.columns[42],  # Here N
        df.columns[11],
        df.columns[18],  # Here N
        df.columns[24],  # Here N
        df.columns[36],  # Here N
        df.columns[37],  # Here N
        df.columns[10],
    ]:
        df[column] = df[column].astype(str).str.replace("-", "0")
        if column in [
            df.columns[16],
            df.columns[19],
            df.columns[22],
            df.columns[29],
            df.columns[32],
        ]:
            df[column] = (
                             df[column].astype(str).str.rstrip("%").astype(float)) / 100

    for column in [
        df.columns[17],
        df.columns[32],
        df.columns[22],
        df.columns[19],
        df.columns[16],
        df.columns[31],
        df.columns[41],
        df.columns[30],
        df.columns[40],
        df.columns[35],
        df.columns[28],
        df.columns[34],
        df.columns[27],
        df.columns[26],
        df.columns[25],
        df.columns[23],
        df.columns[21],
        df.columns[29],
        df.columns[43],
        df.columns[20],
    ]:
        df[column] = df[column].apply(lambda x: float(x))
        df[column] = pd.to_numeric(df[column], downcast="float")

    df[df.columns[10]] = df[df.columns[10]].astype(str).str.replace("nan", "0")
    for column in [
        df.columns[12],
        df.columns[13],
        df.columns[14],
        df.columns[15],
        df.columns[33],
        df.columns[39],
        df.columns[10],
        df.columns[38],
        df.columns[11],
        df.columns[18],
        df.columns[24],
        df.columns[36],
        df.columns[37],
        df.columns[42],
    ]:
        df[column] = df[column].apply(lambda x: int(x))
        df[column] = pd.to_numeric(df[column], downcast="integer")
    return df


# CREATE METRICS FOR GOALKEEPERS
# Create columns and process values to create KPI for goalkeepers
# ///////////////////////////////////////////////////////////////
def create_metrics_for_gk(df):
    """
    It takes a dataframe and a language as input, and returns the dataframe with the following metrics added:

    - Tot_Sav: total saves made
    - Per_90: minutes played per 90 minutes
    - Saves_90: saves made per 90 minutes
    - Shots_Faced: shots faced
    - Faced_90: shots faced per 90 minutes

    The function is used in the following way:

    :param df: the dataframe you want to create the metrics for
    :return: A dataframe with the new metrics added.
    """
    # Create Saves_90 metric (saves made per 90)
    df["Tot_Sav"] = df[df.columns[12]] + df[df.columns[13]] + df[df.columns[14]]
    df["Per_90"] = df[df.columns[11]] / 90
    df["Saves_90"] = df["Tot_Sav"] / df["Per_90"]
    # Create Faced_90 metric (shots faced per 90)
    df["Shots_Faced"] = df[df.columns[15]] + df["Tot_Sav"]
    df["Faced_90"] = df["Shots_Faced"] / df["Per_90"]
    return df


# ROUND DATA
# Round all float values to 2 decimals
# ///////////////////////////////////////////////////////////////
def round_data(df):
    """
    It takes a dataframe as input, finds all the columns that are numeric, and rounds them to 2 decimal places

    :param df: the dataframe to be rounded
    :return: A dataframe with all the numeric columns rounded to 2 decimal places.
    """
    tmp = df.select_dtypes(include=[np.number, np.float])
    df.loc[:, tmp.columns] = np.round(tmp, decimals=2)
    return df


# DATA FOR RANKINGS
# Load data to make metrics for rankings
# ///////////////////////////////////////////////////////////////
def data_for_rankings(df, language):
    """
    It takes a dataframe and a language, and returns a dataframe with the same columns,
    but with the addition of a column for each position, and a column for the global score

    :param df: the dataframe that contains the data
    :param language: The language of the dataframe
    :return: A dataframe with the values of the rankings.
    """
    js_positions = None
    if language == "en":
        js_positions = {
            "positionEvaluation": [
                {
                    "position": "GK-De",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[54],
                                    df.columns[47], df.columns[67], df.columns[60], df.columns[87], df.columns[81],
                                    df.columns[56], df.columns[78], df.columns[88]],
                    "coef1": 13,
                    "coef2": 0.000001
                },
                {
                    "position": "SW-De",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[73],
                                    df.columns[58], df.columns[54], df.columns[53], df.columns[67], df.columns[60],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[46], df.columns[82], df.columns[44], df.columns[88], df.columns[47]],
                    "coef1": 19,
                    "coef2": 0.00000002
                },
                {
                    "position": "SW-Su",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[73],
                                    df.columns[58], df.columns[54], df.columns[53], df.columns[67], df.columns[60],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[46], df.columns[82], df.columns[44], df.columns[88], df.columns[47]],
                    "coef1": 19,
                    "coef2": 0.000003
                },
                {
                    "position": "SW-At",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[73],
                                    df.columns[58], df.columns[54], df.columns[53], df.columns[67], df.columns[60],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[46], df.columns[82], df.columns[44], df.columns[88], df.columns[47],
                                    df.columns[75]],
                    "coef1": 20,
                    "coef2": 0.00004
                },
                {
                    "position": "BPD-De",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[50], df.columns[63], df.columns[58],
                                    df.columns[48], df.columns[89], df.columns[87], df.columns[56], df.columns[81],
                                    df.columns[78], df.columns[82], df.columns[85], df.columns[46],
                                    df.columns[68], df.columns[59], df.columns[51]],
                    "coef1": 17,
                    "coef2": 0.00005
                },
                {
                    "position": "BPD-Co",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[50], df.columns[63], df.columns[58],
                                    df.columns[48], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[46],
                                    df.columns[68], df.columns[59], df.columns[51]],
                    "coef1": 16,
                    "coef2": 0.000006
                },
                {
                    "position": "BPD-St",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[50], df.columns[63], df.columns[58],
                                    df.columns[48], df.columns[89], df.columns[87], df.columns[56], df.columns[81],
                                    df.columns[78], df.columns[82], df.columns[85], df.columns[46],
                                    df.columns[68], df.columns[51]],
                    "coef1": 16,
                    "coef2": 0.000007
                },
                {
                    "position": "CD-De",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68], df.columns[59]],
                    "coef1": 13,
                    "coef2": 0.000008
                },
                {
                    "position": "CD-Co",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[87], df.columns[56],
                                    df.columns[81], df.columns[78], df.columns[82], df.columns[85], df.columns[51],
                                    df.columns[68], df.columns[59]],
                    "coef1": 12,
                    "coef2": 0.0000008
                },
                {
                    "position": "CD-St",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68]],
                    "coef1": 12,
                    "coef2": 0.000009
                },
                {
                    "position": "L-Su",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[63], df.columns[50], df.columns[58],
                                    df.columns[76], df.columns[48], df.columns[87], df.columns[56], df.columns[81],
                                    df.columns[78], df.columns[49], df.columns[82], df.columns[46],
                                    df.columns[72], df.columns[85], df.columns[88], df.columns[68], df.columns[51],
                                    df.columns[86]],
                    "coef1": 20,
                    "coef2": 0.000000101
                },
                {
                    "position": "WCB-De",
                    "sumElements": [df.columns[69], df.columns[79], df.columns[63], df.columns[50], df.columns[89],
                                    df.columns[76], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[45], df.columns[68],
                                    df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 17,
                    "coef2": 0.0000011
                },
                {
                    "position": "WCB-Su",
                    "sumElements": [df.columns[69], df.columns[79], df.columns[63], df.columns[50], df.columns[89],
                                    df.columns[76], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[45], df.columns[68],
                                    df.columns[51], df.columns[52], df.columns[59], df.columns[61]],
                    "coef1": 17,
                    "coef2": 0.0000012
                },
                {
                    "position": "WCB-At",
                    "sumElements": [df.columns[69], df.columns[79], df.columns[63], df.columns[50], df.columns[89],
                                    df.columns[76], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[45], df.columns[68],
                                    df.columns[51], df.columns[52], df.columns[59], df.columns[61]],
                    "coef1": 17,
                    "coef2": 0.00000013
                },
                {
                    "position": "NCB-De",
                    "sumElements": [df.columns[69], df.columns[50], df.columns[63], df.columns[89], df.columns[81],
                                    df.columns[56], df.columns[87], df.columns[85], df.columns[68], df.columns[51],
                                    df.columns[59]],
                    "coef1": 11,
                    "coef2": 0.00000014
                },
                {
                    "position": "NCB-Co",
                    "sumElements": [df.columns[69], df.columns[50], df.columns[63], df.columns[87], df.columns[81],
                                    df.columns[56], df.columns[85], df.columns[68], df.columns[59], df.columns[51]],
                    "coef1": 10,
                    "coef2": 0.000015
                },
                {
                    "position": "NCB-St",
                    "sumElements": [df.columns[69], df.columns[50], df.columns[63], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[68], df.columns[51]],
                    "coef1": 9,
                    "coef2": 0.000000016
                },
                {
                    "position": "CWB-Su",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[58], df.columns[48],
                                    df.columns[76], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[82], df.columns[45], df.columns[72], df.columns[44],
                                    df.columns[88], df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.00000017
                },
                {
                    "position": "CWB-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[58], df.columns[48],
                                    df.columns[76], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[82], df.columns[45], df.columns[72], df.columns[44],
                                    df.columns[88], df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.0000018
                },
                {
                    "position": "WB-De",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[63], df.columns[50],
                                    df.columns[76], df.columns[48], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[88],
                                    df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.000019
                },
                {
                    "position": "WB-Su",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[63], df.columns[76],
                                    df.columns[48], df.columns[58], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[56], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[88],
                                    df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.00000201
                },
                {
                    "position": "WB-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[58], df.columns[63],
                                    df.columns[76], df.columns[48], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[61], df.columns[78], df.columns[49], df.columns[45], df.columns[72],
                                    df.columns[44],
                                    df.columns[88], df.columns[52], df.columns[59]],
                    "coef1": 19,
                    "coef2": 0.00000021
                },
                {
                    "position": "IWB-De",
                    "sumElements": [df.columns[73], df.columns[63], df.columns[58], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[45], df.columns[44], df.columns[88],
                                    df.columns[52]],
                    "coef1": 16,
                    "coef2": 0.000000022
                },
                {
                    "position": "IWB-Su",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[63], df.columns[58], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[78], df.columns[56],
                                    df.columns[61], df.columns[49], df.columns[45], df.columns[82], df.columns[44],
                                    df.columns[88],
                                    df.columns[52]],
                    "coef1": 17,
                    "coef2": 0.00000023
                },
                {
                    "position": "IWB-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[63], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[65], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[82],
                                    df.columns[72],
                                    df.columns[44], df.columns[88], df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.0000024
                },
                {
                    "position": "NFB-De",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[49], df.columns[85], df.columns[51]],
                    "coef1": 10,
                    "coef2": 0.00000025
                },
                {
                    "position": "FB-De",
                    "sumElements": [df.columns[79], df.columns[50], df.columns[58], df.columns[63], df.columns[87],
                                    df.columns[81], df.columns[78], df.columns[56], df.columns[49], df.columns[82],
                                    df.columns[52], df.columns[59]],
                    "coef1": 12,
                    "coef2": 0.0000026
                },
                {
                    "position": "FB-Su",
                    "sumElements": [df.columns[79], df.columns[50], df.columns[58], df.columns[63], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[49], df.columns[82], df.columns[45], df.columns[52], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000027
                },
                {
                    "position": "FB-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[52], df.columns[59], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[45], df.columns[82], df.columns[79], df.columns[73], df.columns[50],
                                    df.columns[63],
                                    df.columns[76], df.columns[58], df.columns[48]],
                    "coef1": 19,
                    "coef2": 0.0000028
                },
                {
                    "position": "A-De",
                    "sumElements": [df.columns[50], df.columns[63], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[49], df.columns[82], df.columns[51]],
                    "coef1": 9,
                    "coef2": 0.000029
                },
                {
                    "position": "HB-De",
                    "sumElements": [df.columns[68], df.columns[51], df.columns[52], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[85], df.columns[69], df.columns[63], df.columns[58],
                                    df.columns[50]],
                    "coef1": 16,
                    "coef2": 0.0000301
                },
                {
                    "position": "DM-De",
                    "sumElements": [df.columns[63], df.columns[58], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[51], df.columns[52]],
                    "coef1": 13,
                    "coef2": 0.000031
                },
                {
                    "position": "DM-Su",
                    "sumElements": [df.columns[63], df.columns[58], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[51], df.columns[52], df.columns[73]],
                    "coef1": 14,
                    "coef2": 0.000032
                },
                {
                    "position": "REG-Su",
                    "sumElements": [df.columns[58], df.columns[73], df.columns[76], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[49], df.columns[82],
                                    df.columns[72], df.columns[46], df.columns[86]],
                    "coef1": 13,
                    "coef2": 0.000033
                },
                {
                    "position": "VOL-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[50], df.columns[63], df.columns[74],
                                    df.columns[65], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[61], df.columns[45], df.columns[82], df.columns[44], df.columns[86],
                                    df.columns[51],
                                    df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.000034
                },
                {
                    "position": "VOL-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[50], df.columns[63], df.columns[74],
                                    df.columns[65], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[61], df.columns[45], df.columns[82], df.columns[44], df.columns[86],
                                    df.columns[51],
                                    df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.000035
                },
                {
                    "position": "DLP-De",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[48], df.columns[87],
                                    df.columns[56], df.columns[78], df.columns[49], df.columns[45], df.columns[46],
                                    df.columns[82], df.columns[86]],
                    "coef1": 12,
                    "coef2": 0.000036
                },
                {
                    "position": "DLP-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[48], df.columns[87], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[45], df.columns[46], df.columns[82],
                                    df.columns[86]],
                    "coef1": 11,
                    "coef2": 0.000037
                },
                {
                    "position": "BWM-De",
                    "sumElements": [df.columns[56], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[49], df.columns[45], df.columns[85], df.columns[88],
                                    df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 13,
                    "coef2": 0.000038
                },
                {
                    "position": "BWM-Su",
                    "sumElements": [df.columns[58], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[49], df.columns[45], df.columns[85], df.columns[88],
                                    df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 13,
                    "coef2": 0.000039
                },
                {
                    "position": "CM-De",
                    "sumElements": [df.columns[73], df.columns[63], df.columns[58], df.columns[50], df.columns[48],
                                    df.columns[89], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.0000401
                },
                {
                    "position": "CM-Su",
                    "sumElements": [df.columns[52], df.columns[87], df.columns[81], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[46], df.columns[45], df.columns[82], df.columns[48],
                                    df.columns[58], df.columns[73], df.columns[50]],
                    "coef1": 13,
                    "coef2": 0.000041
                },
                {
                    "position": "CM-At",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[46], df.columns[44], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.000042
                },
                {
                    "position": "CAR-Su",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[48], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[45], df.columns[82], df.columns[46], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.000043
                },
                {
                    "position": "BBM-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[50], df.columns[76], df.columns[74],
                                    df.columns[48], df.columns[65], df.columns[89], df.columns[87], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[82],
                                    df.columns[44],
                                    df.columns[86], df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.000044
                },
                {
                    "position": "RPM-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[65], df.columns[48],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[46], df.columns[82], df.columns[44],
                                    df.columns[88],
                                    df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 19,
                    "coef2": 0.000045
                },
                {
                    "position": "MEZ-Su",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[87], df.columns[78], df.columns[61], df.columns[45],
                                    df.columns[82], df.columns[46], df.columns[44], df.columns[86], df.columns[52]],
                    "coef1": 15,
                    "coef2": 0.000046
                },
                {
                    "position": "MEZ-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[87], df.columns[78], df.columns[61], df.columns[45],
                                    df.columns[46], df.columns[72], df.columns[82], df.columns[44], df.columns[86],
                                    df.columns[52]],
                    "coef1": 16,
                    "coef2": 0.000047
                },
                {
                    "position": "AT-Su",
                    "sumElements": [df.columns[88], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[46], df.columns[72], df.columns[82], df.columns[73], df.columns[58],
                                    df.columns[48], df.columns[76]],
                    "coef1": 12,
                    "coef2": 0.000048
                },
                {
                    "position": "AT-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[87], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[46], df.columns[72], df.columns[82], df.columns[73],
                                    df.columns[58], df.columns[48], df.columns[76]],
                    "coef1": 13,
                    "coef2": 0.000049
                },
                {
                    "position": "WM-De",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[63], df.columns[79],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.00000501
                },
                {
                    "position": "WM-Su",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[61], df.columns[79],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[52], df.columns[46]],
                    "coef1": 15,
                    "coef2": 0.0000051
                },
                {
                    "position": "WM-At",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[61], df.columns[79],
                                    df.columns[48], df.columns[87], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[52], df.columns[46]],
                    "coef1": 13,
                    "coef2": 0.0000052
                },
                {
                    "position": "DW-De",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[63], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[89], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[52]],
                    "coef1": 16,
                    "coef2": 0.0000053
                },
                {
                    "position": "DW-Su",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[63], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[89], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[52],
                                    df.columns[58], df.columns[82]],
                    "coef1": 18,
                    "coef2": 0.0000054
                },
                {
                    "position": "WP-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[48], df.columns[76], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[82], df.columns[46], df.columns[88]],
                    "coef1": 10,
                    "coef2": 0.0000055
                },
                {
                    "position": "WP-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[48], df.columns[76], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[44], df.columns[88]],
                    "coef1": 13,
                    "coef2": 0.00056
                },
                {
                    "position": "EG-Su",
                    "sumElements": [df.columns[88], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[46], df.columns[72], df.columns[82], df.columns[73], df.columns[58],
                                    df.columns[48], df.columns[76]],
                    "coef1": 12,
                    "coef2": 0.0000057
                },
                {
                    "position": "AM-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[82], df.columns[46],
                                    df.columns[72], df.columns[88]],
                    "coef1": 12,
                    "coef2": 0.0000058
                },
                {
                    "position": "AM-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[82], df.columns[46],
                                    df.columns[72], df.columns[88], df.columns[74]],
                    "coef1": 13,
                    "coef2": 0.0000059
                },
                {
                    "position": "T-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[48],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[46], df.columns[82],
                                    df.columns[72], df.columns[44], df.columns[88], df.columns[86]],
                    "coef1": 14,
                    "coef2": 0.00000601
                },
                {
                    "position": "SS-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[48],
                                    df.columns[87], df.columns[81], df.columns[78], df.columns[61], df.columns[45],
                                    df.columns[82], df.columns[44], df.columns[88], df.columns[86], df.columns[52],
                                    df.columns[59]],
                    "coef1": 16,
                    "coef2": 0.0000061
                },
                {
                    "position": "W-Su",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[61], df.columns[45], df.columns[44], df.columns[88], df.columns[52],
                                    df.columns[59]],
                    "coef1": 11,
                    "coef2": 0.0000062
                },
                {
                    "position": "W-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[87], df.columns[61], df.columns[72], df.columns[44], df.columns[88],
                                    df.columns[59]],
                    "coef1": 11,
                    "coef2": 0.0000063
                },
                {
                    "position": "IF-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[65],
                                    df.columns[48], df.columns[87], df.columns[61], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[44], df.columns[88], df.columns[86], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000064
                },
                {
                    "position": "IF-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[59], df.columns[87],
                                    df.columns[61], df.columns[82], df.columns[72], df.columns[58], df.columns[73],
                                    df.columns[74], df.columns[76], df.columns[48], df.columns[65]],
                    "coef1": 14,
                    "coef2": 0.0000065
                },
                {
                    "position": "IW-Su",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[78], df.columns[61], df.columns[45], df.columns[82],
                                    df.columns[46], df.columns[44], df.columns[88], df.columns[52], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000066
                },
                {
                    "position": "IW-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[87], df.columns[78], df.columns[61], df.columns[82],
                                    df.columns[72], df.columns[46], df.columns[44], df.columns[88], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000067
                },
                {
                    "position": "RMD-At",
                    "sumElements": [df.columns[73], df.columns[48], df.columns[74], df.columns[87], df.columns[81],
                                    df.columns[78], df.columns[61], df.columns[45], df.columns[82], df.columns[44],
                                    df.columns[86], df.columns[52]],
                    "coef1": 12,
                    "coef2": 0.0000068
                },
                {
                    "position": "WT-Su",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[69], df.columns[87], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[85], df.columns[68], df.columns[51],
                                    df.columns[86], df.columns[52]],
                    "coef1": 12,
                    "coef2": 0.0000069
                },
                {
                    "position": "WT-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[69], df.columns[87], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[85], df.columns[68], df.columns[51],
                                    df.columns[86], df.columns[52], df.columns[74]],
                    "coef1": 13,
                    "coef2": 0.00000701
                },
                {
                    "position": "TF-Su",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[74], df.columns[89], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68], df.columns[86]],
                    "coef1": 13,
                    "coef2": 0.0000071
                },
                {
                    "position": "TF-At",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[74], df.columns[89], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68], df.columns[86]],
                    "coef1": 13,
                    "coef2": 0.0000072
                },
                {
                    "position": "DLF-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[48], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[86], df.columns[51]],
                    "coef1": 13,
                    "coef2": 0.0000073
                },
                {
                    "position": "DLF-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[48], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[86], df.columns[51], df.columns[76]],
                    "coef1": 14,
                    "coef2": 0.0000074
                },
                {
                    "position": "PF-De",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[51], df.columns[52],
                                    df.columns[59], df.columns[89], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[49], df.columns[82], df.columns[45], df.columns[85], df.columns[73]],
                    "coef1": 15,
                    "coef2": 0.0000075
                },
                {
                    "position": "PF-Su",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[51], df.columns[52],
                                    df.columns[59], df.columns[89], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[82], df.columns[45], df.columns[85],
                                    df.columns[73],
                                    df.columns[58]],
                    "coef1": 17,
                    "coef2": 0.0000076
                },
                {
                    "position": "PF-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[51], df.columns[52],
                                    df.columns[59], df.columns[89], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[82], df.columns[45], df.columns[85],
                                    df.columns[73],
                                    df.columns[74]],
                    "coef1": 17,
                    "coef2": 0.0000077
                },
                {
                    "position": "CF-Su",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[58], df.columns[76], df.columns[74],
                                    df.columns[65], df.columns[48], df.columns[87], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[46], df.columns[44],
                                    df.columns[88],
                                    df.columns[68], df.columns[86], df.columns[51], df.columns[59], df.columns[52]],
                    "coef1": 21,
                    "coef2": 0.0000078
                },
                {
                    "position": "CF-At",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[58], df.columns[76], df.columns[74],
                                    df.columns[65], df.columns[48], df.columns[87], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[46], df.columns[44],
                                    df.columns[88],
                                    df.columns[68], df.columns[86], df.columns[51], df.columns[59], df.columns[52]],
                    "coef1": 21,
                    "coef2": 0.0000079
                },
                {
                    "position": "P-At",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[74], df.columns[48], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[82], df.columns[44]],
                    "coef1": 9,
                    "coef2": 0.00000801
                },
                {
                    "position": "AF-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[76], df.columns[48],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[45], df.columns[82],
                                    df.columns[44], df.columns[88], df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000081
                },
                {
                    "position": "F9-Su",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[48],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[49], df.columns[72],
                                    df.columns[82], df.columns[46], df.columns[44], df.columns[88], df.columns[86]],
                    "coef1": 15,
                    "coef2": 0.0000082
                },
                {
                    "position": "Global",
                    "sumElements": [df.columns[90], df.columns[84], df.columns[83], df.columns[75], df.columns[70],
                                    df.columns[67], df.columns[60], df.columns[54], df.columns[53], df.columns[55],
                                    df.columns[47], df.columns[89], df.columns[87], df.columns[85]],
                    "gralSum": [df.columns[82], df.columns[81], df.columns[78], df.columns[77], df.columns[72],
                                df.columns[66], df.columns[61], df.columns[56], df.columns[49], df.columns[46],
                                df.columns[45], df.columns[44], df.columns[88], df.columns[86],
                                df.columns[68], df.columns[62], df.columns[59], df.columns[52], df.columns[51]],
                    "elementsProm": [df.columns[80], df.columns[79], df.columns[76], df.columns[74], df.columns[73],
                                     df.columns[71], df.columns[69], df.columns[65], df.columns[64], df.columns[63],
                                     df.columns[58], df.columns[57], df.columns[50],
                                     df.columns[48], df.columns[89], df.columns[87], df.columns[85], df.columns[82],
                                     df.columns[81], df.columns[78], df.columns[77], df.columns[72], df.columns[66],
                                     df.columns[61], df.columns[56], df.columns[49], df.columns[46], df.columns[45],
                                     df.columns[44],
                                     df.columns[88], df.columns[86], df.columns[68], df.columns[62], df.columns[59],
                                     df.columns[52], df.columns[51]]
                }
            ],
            "development": [
                {
                    "training": "Free kicks",
                    "e_trained": [df.columns[71], df.columns[48]]
                },
                {
                    "training": "Corners",
                    "e_trained": [df.columns[80], df.columns[48]]
                },
                {
                    "training": "Penalty kicks",
                    "e_trained": [df.columns[57], df.columns[48]]
                },
                {
                    "training": "Long throws",
                    "e_trained": [df.columns[64]]
                },
                {
                    "training": "Speed",
                    "e_trained": [df.columns[44], df.columns[59]]
                },
                {
                    "training": "Agility and balance",
                    "e_trained": [df.columns[86], df.columns[88]]
                },
                {
                    "training": "Strength",
                    "e_trained": [df.columns[51], df.columns[68]]
                },
                {
                    "training": "Support",
                    "e_trained": [df.columns[52], df.columns[45]]
                },
                {
                    "training": "Defensive positioning",
                    "e_trained": [df.columns[56], df.columns[78], df.columns[63]]
                },
                {
                    "training": "Attacking moves",
                    "e_trained": ["Dec, OtB", df.columns[87]]
                },
                {
                    "training": "Last third",
                    "e_trained": [df.columns[78], df.columns[82]]
                },
                {
                    "training": "Shoots",
                    "e_trained": [df.columns[48], df.columns[65], df.columns[74]]
                },
                {
                    "training": "Passes",
                    "e_trained": [df.columns[48], df.columns[58], df.columns[46]]
                },
                {
                    "training": "Crossings",
                    "e_trained": [df.columns[79], df.columns[48]]
                },
                {
                    "training": "Ball control",
                    "e_trained": [df.columns[76], df.columns[73], df.columns[48]]
                },
                {
                    "training": "Aerial game",
                    "e_trained": [df.columns[69], df.columns[85]]
                }
            ]
        }
    elif language == "es":
        js_positions = {
            "positionEvaluation": [
                {
                    "position": "POR-De",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[54],
                                    df.columns[47], df.columns[67], df.columns[60], df.columns[87], df.columns[81],
                                    df.columns[56], df.columns[78], df.columns[88]],
                    "coef1": 13,
                    "coef2": 0.000001
                },
                {
                    "position": "PCI-De",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[73],
                                    df.columns[58], df.columns[54], df.columns[53], df.columns[67], df.columns[60],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[46], df.columns[82], df.columns[44], df.columns[88], df.columns[47]],
                    "coef1": 19,
                    "coef2": 0.00000002
                },
                {
                    "position": "PCI-Ap",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[73],
                                    df.columns[58], df.columns[54], df.columns[53], df.columns[67], df.columns[60],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[46], df.columns[82], df.columns[44], df.columns[88], df.columns[47]],
                    "coef1": 19,
                    "coef2": 0.000003
                },
                {
                    "position": "PCI-At",
                    "sumElements": [df.columns[90], df.columns[70], df.columns[83], df.columns[84], df.columns[73],
                                    df.columns[58], df.columns[54], df.columns[53], df.columns[67], df.columns[60],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[46], df.columns[82], df.columns[44], df.columns[88], df.columns[47],
                                    df.columns[75]],
                    "coef1": 20,
                    "coef2": 0.00004
                },
                {
                    "position": "DCT-De",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[50], df.columns[63], df.columns[58],
                                    df.columns[48], df.columns[89], df.columns[87], df.columns[56], df.columns[81],
                                    df.columns[78], df.columns[82], df.columns[85], df.columns[46],
                                    df.columns[68], df.columns[59], df.columns[51]],
                    "coef1": 17,
                    "coef2": 0.00005
                },
                {
                    "position": "DCT-Cu",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[50], df.columns[63], df.columns[58],
                                    df.columns[48], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[46],
                                    df.columns[68], df.columns[59], df.columns[51]],
                    "coef1": 16,
                    "coef2": 0.000006
                },
                {
                    "position": "DCT-Ta",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[50], df.columns[63], df.columns[58],
                                    df.columns[48], df.columns[89], df.columns[87], df.columns[56], df.columns[81],
                                    df.columns[78], df.columns[82], df.columns[85], df.columns[46],
                                    df.columns[68], df.columns[51]],
                    "coef1": 16,
                    "coef2": 0.000007
                },
                {
                    "position": "DFC-De",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68], df.columns[59]],
                    "coef1": 13,
                    "coef2": 0.000008
                },
                {
                    "position": "DFC-Cu",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[87], df.columns[56],
                                    df.columns[81], df.columns[78], df.columns[82], df.columns[85], df.columns[51],
                                    df.columns[68], df.columns[59]],
                    "coef1": 12,
                    "coef2": 0.0000008
                },
                {
                    "position": "DFC-Ta",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68]],
                    "coef1": 12,
                    "coef2": 0.000009
                },
                {
                    "position": "LIB-Ap",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[63], df.columns[50], df.columns[58],
                                    df.columns[76], df.columns[48], df.columns[87], df.columns[56], df.columns[81],
                                    df.columns[78], df.columns[49], df.columns[82], df.columns[46],
                                    df.columns[72], df.columns[85], df.columns[88], df.columns[68], df.columns[51],
                                    df.columns[86]],
                    "coef1": 20,
                    "coef2": 0.000000101
                },
                {
                    "position": "CLT-De",
                    "sumElements": [df.columns[69], df.columns[79], df.columns[63], df.columns[50], df.columns[89],
                                    df.columns[76], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[45], df.columns[68],
                                    df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 17,
                    "coef2": 0.0000011
                },
                {
                    "position": "CLT-Ap",
                    "sumElements": [df.columns[69], df.columns[79], df.columns[63], df.columns[50], df.columns[89],
                                    df.columns[76], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[45], df.columns[68],
                                    df.columns[51], df.columns[52], df.columns[59], df.columns[61]],
                    "coef1": 17,
                    "coef2": 0.0000012
                },
                {
                    "position": "CLT-At",
                    "sumElements": [df.columns[69], df.columns[79], df.columns[63], df.columns[50], df.columns[89],
                                    df.columns[76], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[82], df.columns[85], df.columns[45], df.columns[68],
                                    df.columns[51], df.columns[52], df.columns[59], df.columns[61]],
                    "coef1": 17,
                    "coef2": 0.00000013
                },
                {
                    "position": "DPr-De",
                    "sumElements": [df.columns[69], df.columns[50], df.columns[63], df.columns[89], df.columns[81],
                                    df.columns[56], df.columns[87], df.columns[85], df.columns[68], df.columns[51],
                                    df.columns[59]],
                    "coef1": 11,
                    "coef2": 0.00000014
                },
                {
                    "position": "DPr-Cu",
                    "sumElements": [df.columns[69], df.columns[50], df.columns[63], df.columns[87], df.columns[81],
                                    df.columns[56], df.columns[85], df.columns[68], df.columns[59], df.columns[51]],
                    "coef1": 10,
                    "coef2": 0.000015
                },
                {
                    "position": "DPr-Ta",
                    "sumElements": [df.columns[69], df.columns[50], df.columns[63], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[68], df.columns[51]],
                    "coef1": 9,
                    "coef2": 0.000000016
                },
                {
                    "position": "CRC-Ap",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[58], df.columns[48],
                                    df.columns[76], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[82], df.columns[45], df.columns[72], df.columns[44],
                                    df.columns[88], df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.00000017
                },
                {
                    "position": "CRC-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[58], df.columns[48],
                                    df.columns[76], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[82], df.columns[45], df.columns[72], df.columns[44],
                                    df.columns[88], df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.0000018
                },
                {
                    "position": "CAR-De",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[63], df.columns[50],
                                    df.columns[76], df.columns[48], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[88],
                                    df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.000019
                },
                {
                    "position": "CAR-Ap",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[63], df.columns[76],
                                    df.columns[48], df.columns[58], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[56], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[88],
                                    df.columns[52], df.columns[59]],
                    "coef1": 18,
                    "coef2": 0.00000201
                },
                {
                    "position": "CAR-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[50], df.columns[58], df.columns[63],
                                    df.columns[76], df.columns[48], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[61], df.columns[78], df.columns[49], df.columns[45], df.columns[72],
                                    df.columns[44],
                                    df.columns[88], df.columns[52], df.columns[59]],
                    "coef1": 19,
                    "coef2": 0.00000021
                },
                {
                    "position": "CIN-De",
                    "sumElements": [df.columns[73], df.columns[63], df.columns[58], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[45], df.columns[44], df.columns[88],
                                    df.columns[52]],
                    "coef1": 16,
                    "coef2": 0.000000022
                },
                {
                    "position": "CIN-Ap",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[63], df.columns[58], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[78], df.columns[56],
                                    df.columns[61], df.columns[49], df.columns[45], df.columns[82], df.columns[44],
                                    df.columns[88],
                                    df.columns[52]],
                    "coef1": 17,
                    "coef2": 0.00000023
                },
                {
                    "position": "CIN-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[63], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[65], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[82],
                                    df.columns[72],
                                    df.columns[44], df.columns[88], df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.0000024
                },
                {
                    "position": "LP-De",
                    "sumElements": [df.columns[69], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[49], df.columns[85], df.columns[51]],
                    "coef1": 10,
                    "coef2": 0.00000025
                },
                {
                    "position": "LAT-De",
                    "sumElements": [df.columns[79], df.columns[50], df.columns[58], df.columns[63], df.columns[87],
                                    df.columns[81], df.columns[78], df.columns[56], df.columns[49], df.columns[82],
                                    df.columns[52], df.columns[59]],
                    "coef1": 12,
                    "coef2": 0.0000026
                },
                {
                    "position": "LAT-Ap",
                    "sumElements": [df.columns[79], df.columns[50], df.columns[58], df.columns[63], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[49], df.columns[82], df.columns[45], df.columns[52], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000027
                },
                {
                    "position": "LAT-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[52], df.columns[59], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[45], df.columns[82], df.columns[79], df.columns[73], df.columns[50],
                                    df.columns[63],
                                    df.columns[76], df.columns[58], df.columns[48]],
                    "coef1": 19,
                    "coef2": 0.0000028
                },
                {
                    "position": "PVD-De",
                    "sumElements": [df.columns[50], df.columns[63], df.columns[87], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[49], df.columns[82], df.columns[51]],
                    "coef1": 9,
                    "coef2": 0.000029
                },
                {
                    "position": "MCI-De",
                    "sumElements": [df.columns[68], df.columns[51], df.columns[52], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[85], df.columns[69], df.columns[63], df.columns[58],
                                    df.columns[50]],
                    "coef1": 16,
                    "coef2": 0.0000301
                },
                {
                    "position": "MC-De",
                    "sumElements": [df.columns[63], df.columns[58], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[51], df.columns[52]],
                    "coef1": 13,
                    "coef2": 0.000031
                },
                {
                    "position": "MC-Ap",
                    "sumElements": [df.columns[63], df.columns[58], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[56], df.columns[81], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[51], df.columns[52], df.columns[73]],
                    "coef1": 14,
                    "coef2": 0.000032
                },
                {
                    "position": "REG-Ap",
                    "sumElements": [df.columns[58], df.columns[73], df.columns[76], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[49], df.columns[82],
                                    df.columns[72], df.columns[46], df.columns[86]],
                    "coef1": 13,
                    "coef2": 0.000033
                },
                {
                    "position": "VOL-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[50], df.columns[63], df.columns[74],
                                    df.columns[65], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[61], df.columns[45], df.columns[82], df.columns[44], df.columns[86],
                                    df.columns[51],
                                    df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.000034
                },
                {
                    "position": "VOL-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[50], df.columns[63], df.columns[74],
                                    df.columns[65], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[61], df.columns[45], df.columns[82], df.columns[44], df.columns[86],
                                    df.columns[51],
                                    df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.000035
                },
                {
                    "position": "PVO-De",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[48], df.columns[87],
                                    df.columns[56], df.columns[78], df.columns[49], df.columns[45], df.columns[46],
                                    df.columns[82], df.columns[86]],
                    "coef1": 12,
                    "coef2": 0.000036
                },
                {
                    "position": "PVO-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[48], df.columns[87], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[45], df.columns[46], df.columns[82],
                                    df.columns[86]],
                    "coef1": 11,
                    "coef2": 0.000037
                },
                {
                    "position": "CRP-De",
                    "sumElements": [df.columns[56], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[49], df.columns[45], df.columns[85], df.columns[88],
                                    df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 13,
                    "coef2": 0.000038
                },
                {
                    "position": "CRP-Ap",
                    "sumElements": [df.columns[58], df.columns[63], df.columns[50], df.columns[89], df.columns[87],
                                    df.columns[81], df.columns[49], df.columns[45], df.columns[85], df.columns[88],
                                    df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 13,
                    "coef2": 0.000039
                },
                {
                    "position": "CM-De",
                    "sumElements": [df.columns[73], df.columns[63], df.columns[58], df.columns[50], df.columns[48],
                                    df.columns[89], df.columns[87], df.columns[56], df.columns[81], df.columns[78],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.0000401
                },
                {
                    "position": "CM-Ap",
                    "sumElements": [df.columns[52], df.columns[87], df.columns[81], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[46], df.columns[45], df.columns[82], df.columns[48],
                                    df.columns[58], df.columns[73], df.columns[50]],
                    "coef1": 13,
                    "coef2": 0.000041
                },
                {
                    "position": "CM-At",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[46], df.columns[44], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.000042
                },
                {
                    "position": "IM-Ap",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[48], df.columns[87],
                                    df.columns[81], df.columns[56], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[45], df.columns[82], df.columns[46], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.000043
                },
                {
                    "position": "CTT-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[50], df.columns[76], df.columns[74],
                                    df.columns[48], df.columns[65], df.columns[89], df.columns[87], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[82],
                                    df.columns[44],
                                    df.columns[86], df.columns[51], df.columns[52], df.columns[59]],
                    "coef1": 20,
                    "coef2": 0.000044
                },
                {
                    "position": "OIT-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[65], df.columns[48],
                                    df.columns[87], df.columns[81], df.columns[56], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[46], df.columns[82], df.columns[44],
                                    df.columns[88],
                                    df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 19,
                    "coef2": 0.000045
                },
                {
                    "position": "MEZ-Ap",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[87], df.columns[78], df.columns[61], df.columns[45],
                                    df.columns[82], df.columns[46], df.columns[44], df.columns[86], df.columns[52]],
                    "coef1": 15,
                    "coef2": 0.000046
                },
                {
                    "position": "MEZ-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[87], df.columns[78], df.columns[61], df.columns[45],
                                    df.columns[46], df.columns[72], df.columns[82], df.columns[44], df.columns[86],
                                    df.columns[52]],
                    "coef1": 16,
                    "coef2": 0.000047
                },
                {
                    "position": "OAD-Ap",
                    "sumElements": [df.columns[88], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[46], df.columns[72], df.columns[82], df.columns[73], df.columns[58],
                                    df.columns[48], df.columns[76]],
                    "coef1": 12,
                    "coef2": 0.000048
                },
                {
                    "position": "OAD-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[87], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[46], df.columns[72], df.columns[82], df.columns[73],
                                    df.columns[58], df.columns[48], df.columns[76]],
                    "coef1": 13,
                    "coef2": 0.000049
                },
                {
                    "position": "INT-De",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[63], df.columns[79],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[52]],
                    "coef1": 14,
                    "coef2": 0.00000501
                },
                {
                    "position": "INT-Ap",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[61], df.columns[79],
                                    df.columns[48], df.columns[87], df.columns[81], df.columns[56], df.columns[78],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[52], df.columns[46]],
                    "coef1": 15,
                    "coef2": 0.0000051
                },
                {
                    "position": "INT-At",
                    "sumElements": [df.columns[73], df.columns[50], df.columns[58], df.columns[61], df.columns[79],
                                    df.columns[48], df.columns[87], df.columns[78], df.columns[49], df.columns[45],
                                    df.columns[82], df.columns[52], df.columns[46]],
                    "coef1": 13,
                    "coef2": 0.0000052
                },
                {
                    "position": "IDF-De",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[63], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[89], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[52]],
                    "coef1": 16,
                    "coef2": 0.0000053
                },
                {
                    "position": "IDF-Ap",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[63], df.columns[50], df.columns[76],
                                    df.columns[48], df.columns[87], df.columns[89], df.columns[81], df.columns[56],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[45], df.columns[44],
                                    df.columns[52],
                                    df.columns[58], df.columns[82]],
                    "coef1": 18,
                    "coef2": 0.0000054
                },
                {
                    "position": "OES-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[48], df.columns[76], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[82], df.columns[46], df.columns[88]],
                    "coef1": 10,
                    "coef2": 0.0000055
                },
                {
                    "position": "OES-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[48], df.columns[76], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[44], df.columns[88]],
                    "coef1": 13,
                    "coef2": 0.00056
                },
                {
                    "position": "ENG-Ap",
                    "sumElements": [df.columns[88], df.columns[87], df.columns[78], df.columns[61], df.columns[49],
                                    df.columns[46], df.columns[72], df.columns[82], df.columns[73], df.columns[58],
                                    df.columns[48], df.columns[76]],
                    "coef1": 12,
                    "coef2": 0.0000057
                },
                {
                    "position": "MP-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[82], df.columns[46],
                                    df.columns[72], df.columns[88]],
                    "coef1": 12,
                    "coef2": 0.0000058
                },
                {
                    "position": "MP-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[48], df.columns[65],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[82], df.columns[46],
                                    df.columns[72], df.columns[88], df.columns[74]],
                    "coef1": 13,
                    "coef2": 0.0000059
                },
                {
                    "position": "TRE-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[48],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[46], df.columns[82],
                                    df.columns[72], df.columns[44], df.columns[88], df.columns[86]],
                    "coef1": 14,
                    "coef2": 0.00000601
                },
                {
                    "position": "DLS-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[48],
                                    df.columns[87], df.columns[81], df.columns[78], df.columns[61], df.columns[45],
                                    df.columns[82], df.columns[44], df.columns[88], df.columns[86], df.columns[52],
                                    df.columns[59]],
                    "coef1": 16,
                    "coef2": 0.0000061
                },
                {
                    "position": "EXT-Ap",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[61], df.columns[45], df.columns[44], df.columns[88], df.columns[52],
                                    df.columns[59]],
                    "coef1": 11,
                    "coef2": 0.0000062
                },
                {
                    "position": "EXT-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[87], df.columns[61], df.columns[72], df.columns[44], df.columns[88],
                                    df.columns[59]],
                    "coef1": 11,
                    "coef2": 0.0000063
                },
                {
                    "position": "DLI-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[65],
                                    df.columns[48], df.columns[87], df.columns[61], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[44], df.columns[88], df.columns[86], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000064
                },
                {
                    "position": "DLI-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[59], df.columns[87],
                                    df.columns[61], df.columns[82], df.columns[72], df.columns[58], df.columns[73],
                                    df.columns[74], df.columns[76], df.columns[48], df.columns[65]],
                    "coef1": 14,
                    "coef2": 0.0000065
                },
                {
                    "position": "II-Ap",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[78], df.columns[61], df.columns[45], df.columns[82],
                                    df.columns[46], df.columns[44], df.columns[88], df.columns[52], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000066
                },
                {
                    "position": "II-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[58], df.columns[76], df.columns[48],
                                    df.columns[65], df.columns[87], df.columns[78], df.columns[61], df.columns[82],
                                    df.columns[72], df.columns[46], df.columns[44], df.columns[88], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000067
                },
                {
                    "position": "BDE-At",
                    "sumElements": [df.columns[73], df.columns[48], df.columns[74], df.columns[87], df.columns[81],
                                    df.columns[78], df.columns[61], df.columns[45], df.columns[82], df.columns[44],
                                    df.columns[86], df.columns[52]],
                    "coef1": 12,
                    "coef2": 0.0000068
                },
                {
                    "position": "HOE-Ap",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[69], df.columns[87], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[85], df.columns[68], df.columns[51],
                                    df.columns[86], df.columns[52]],
                    "coef1": 12,
                    "coef2": 0.0000069
                },
                {
                    "position": "HOE-At",
                    "sumElements": [df.columns[79], df.columns[73], df.columns[69], df.columns[87], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[85], df.columns[68], df.columns[51],
                                    df.columns[86], df.columns[52], df.columns[74]],
                    "coef1": 13,
                    "coef2": 0.00000701
                },
                {
                    "position": "OBJ-Ap",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[74], df.columns[89], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68], df.columns[86]],
                    "coef1": 13,
                    "coef2": 0.0000071
                },
                {
                    "position": "OBJ-At",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[74], df.columns[89], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[85],
                                    df.columns[51], df.columns[68], df.columns[86]],
                    "coef1": 13,
                    "coef2": 0.0000072
                },
                {
                    "position": "2°D-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[48], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[86], df.columns[51]],
                    "coef1": 13,
                    "coef2": 0.0000073
                },
                {
                    "position": "2°D-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[48], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[49], df.columns[82], df.columns[72],
                                    df.columns[46], df.columns[86], df.columns[51], df.columns[76]],
                    "coef1": 14,
                    "coef2": 0.0000074
                },
                {
                    "position": "DP-De",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[51], df.columns[52],
                                    df.columns[59], df.columns[89], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[49], df.columns[82], df.columns[45], df.columns[85], df.columns[73]],
                    "coef1": 15,
                    "coef2": 0.0000075
                },
                {
                    "position": "DP-Ap",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[51], df.columns[52],
                                    df.columns[59], df.columns[89], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[82], df.columns[45], df.columns[85],
                                    df.columns[73],
                                    df.columns[58]],
                    "coef1": 17,
                    "coef2": 0.0000076
                },
                {
                    "position": "DP-At",
                    "sumElements": [df.columns[44], df.columns[88], df.columns[86], df.columns[51], df.columns[52],
                                    df.columns[59], df.columns[89], df.columns[87], df.columns[81], df.columns[78],
                                    df.columns[61], df.columns[49], df.columns[82], df.columns[45], df.columns[85],
                                    df.columns[73],
                                    df.columns[74]],
                    "coef1": 17,
                    "coef2": 0.0000077
                },
                {
                    "position": "DLC-Ap",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[58], df.columns[76], df.columns[74],
                                    df.columns[65], df.columns[48], df.columns[87], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[46], df.columns[44],
                                    df.columns[88],
                                    df.columns[68], df.columns[86], df.columns[51], df.columns[59], df.columns[52]],
                    "coef1": 21,
                    "coef2": 0.0000078
                },
                {
                    "position": "DLC-At",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[58], df.columns[76], df.columns[74],
                                    df.columns[65], df.columns[48], df.columns[87], df.columns[78], df.columns[61],
                                    df.columns[49], df.columns[45], df.columns[82], df.columns[46], df.columns[44],
                                    df.columns[88],
                                    df.columns[68], df.columns[86], df.columns[51], df.columns[59], df.columns[52]],
                    "coef1": 21,
                    "coef2": 0.0000079
                },
                {
                    "position": "ARI-At",
                    "sumElements": [df.columns[69], df.columns[73], df.columns[74], df.columns[48], df.columns[87],
                                    df.columns[78], df.columns[61], df.columns[82], df.columns[44]],
                    "coef1": 9,
                    "coef2": 0.00000801
                },
                {
                    "position": "DLA-At",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[74], df.columns[76], df.columns[48],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[45], df.columns[82],
                                    df.columns[44], df.columns[88], df.columns[86], df.columns[52], df.columns[59]],
                    "coef1": 15,
                    "coef2": 0.0000081
                },
                {
                    "position": "F9-Ap",
                    "sumElements": [df.columns[73], df.columns[58], df.columns[76], df.columns[74], df.columns[48],
                                    df.columns[87], df.columns[78], df.columns[61], df.columns[49], df.columns[72],
                                    df.columns[82], df.columns[46], df.columns[44], df.columns[88], df.columns[86]],
                    "coef1": 15,
                    "coef2": 0.0000082
                },
                {
                    "position": "Global",
                    "sumElements": [df.columns[90], df.columns[84], df.columns[83], df.columns[75], df.columns[70],
                                    df.columns[67], df.columns[60], df.columns[54], df.columns[53], df.columns[55],
                                    df.columns[47], df.columns[89], df.columns[87], df.columns[85]],
                    "gralSum": [df.columns[82], df.columns[81], df.columns[78], df.columns[77], df.columns[72],
                                df.columns[66], df.columns[61], df.columns[56], df.columns[49], df.columns[46],
                                df.columns[45], df.columns[44], df.columns[88], df.columns[86],
                                df.columns[68], df.columns[62], df.columns[59], df.columns[52], df.columns[51]],
                    "elementsProm": [df.columns[80], df.columns[79], df.columns[76], df.columns[74], df.columns[73],
                                     df.columns[71], df.columns[69], df.columns[65], df.columns[64], df.columns[63],
                                     df.columns[58], df.columns[57], df.columns[50],
                                     df.columns[48], df.columns[89], df.columns[87], df.columns[85], df.columns[82],
                                     df.columns[81], df.columns[78], df.columns[77], df.columns[72], df.columns[66],
                                     df.columns[61], df.columns[56], df.columns[49], df.columns[46], df.columns[45],
                                     df.columns[44],
                                     df.columns[88], df.columns[86], df.columns[68], df.columns[62], df.columns[59],
                                     df.columns[52], df.columns[51]]
                }
            ],
            "development": [
                {
                    "training": "Tiros libres",
                    "e_trained": [df.columns[71], df.columns[48]]
                },
                {
                    "training": "Corners",
                    "e_trained": [df.columns[80], df.columns[48]]
                },
                {
                    "training": "Lanzamiento penalty",
                    "e_trained": [df.columns[57], df.columns[48]]
                },
                {
                    "training": "Saques largos",
                    "e_trained": [df.columns[64]]
                },
                {
                    "training": "Rapidez",
                    "e_trained": [df.columns[44], df.columns[59]]
                },
                {
                    "training": "Equilibrio y agilidad",
                    "e_trained": [df.columns[86], df.columns[88]]
                },
                {
                    "training": "Fuerza",
                    "e_trained": [df.columns[51], df.columns[68]]
                },
                {
                    "training": "Aguante",
                    "e_trained": [df.columns[52], df.columns[45]]
                },
                {
                    "training": "Colocación defensiva",
                    "e_trained": [df.columns[56], df.columns[78], df.columns[63]]
                },
                {
                    "training": "Movimientos en ataque",
                    "e_trained": [df.columns[78], df.columns[61], df.columns[87]]
                },
                {
                    "training": "Ultimo tercio",
                    "e_trained": [df.columns[78], df.columns[82]]
                },
                {
                    "training": "Disparos",
                    "e_trained": [df.columns[48], df.columns[65], df.columns[74]]
                },
                {
                    "training": "Pases",
                    "e_trained": [df.columns[48], df.columns[58], df.columns[46]]
                },
                {
                    "training": "Centros",
                    "e_trained": [df.columns[79], df.columns[48]]
                },
                {
                    "training": "Control de balón",
                    "e_trained": [df.columns[76], df.columns[73], df.columns[48]]
                },
                {
                    "training": "Juego aéreo",
                    "e_trained": [df.columns[69], df.columns[85]]
                }
            ]
        }

    for p in range(len(js_positions["positionEvaluation"]) - 1):
        aux_string = js_positions["positionEvaluation"][p]["position"]
        aux_coef1 = js_positions["positionEvaluation"][p]["coef1"]
        aux_coef2 = js_positions["positionEvaluation"][p]["coef2"]
        df[aux_string] = 0
        for index, element in enumerate(  # skipcq: PYL-W0612
                js_positions["positionEvaluation"][p]["sumElements"]):
            tmp_value = js_positions["positionEvaluation"][p]["sumElements"][
                index]
            df[aux_string] = df[aux_string] + df[tmp_value]
        df[aux_string] = (df[aux_string] / aux_coef1) + aux_coef2

    cols1 = js_positions["positionEvaluation"][83]["sumElements"]
    cols2 = js_positions["positionEvaluation"][83]["gralSum"]
    cols_d = cols1 + cols2
    cols3 = js_positions["positionEvaluation"][83]["elementsProm"]
    df["Global"] = np.where(
        df[df.columns[3]].str.contains("POR|GK"),
        df[cols_d].sum(1).div(33),
        df[cols3].mean(1),
    )

    return df


# RANK POSITION VALUES
# Make a rank with values previously setted
# ///////////////////////////////////////////////////////////////
def ranking_values(df):
    """
    It takes a dataframe, and for each row, it ranks the values in the columns 96 to 179, and then adds the rank to the
    column name

    :param df: the dataframe
    :return: A dataframe with the same columns as the original dataframe, but with the addition of the ranking columns.
    """

    def add_rank(x):
        """
        It takes a string and returns a string with the last character of the string replaced with the last character
        of the string followed by the string "_rank"

        :param x: the string to be modified
        :return: the last character of the string, plus "_rank"
        """
        return x.replace(x[-1], x[-1] + "_rank")

    df = df.join(df.iloc[:, 96:179].rank(
        axis=1, method="first", ascending=False).astype(int).rename(columns=add_rank))
    return df


# DATAFRAME FOR SQUAD VIEW
# Cut original dataframe to make readable for squad view
# ///////////////////////////////////////////////////////////////
def create_df_for_squad(df, language):
    """
    It takes a dataframe and a language, and returns a dataframe that is ready to be exported for use in
     the Squad table

    :param df: the dataframe you want to convert
    :param language: the language of the text
    :return: A dataframe with the columns:
        - h1
        - h2
        - h4
        - h7
        - h5
        - Global
        - au1
        - au2
        - au3
        - au4
        - au5
        - au6
        - au7
        - au8
        - 96
        in dict
    """
    role_id = text[language].a.au0
    df_for_squad = df.loc[:, [
                                 df.columns[0],
                                 df.columns[1],
                                 df.columns[3],
                                 df.columns[6],
                                 df.columns[4],
                                 "Global",
                             ], ]
    df_for_squad[text[language].a.au1] = "-"
    df_for_squad[text[language].a.au2] = 1
    df_for_squad[text[language].a.au3] = 1
    df_for_squad[text[language].a.au4] = role_id
    df_for_squad[text[language].a.au5] = 2
    df_for_squad[text[language].a.au6] = role_id
    df_for_squad[text[language].a.au7] = 3
    df_for_squad[text[language].a.au8] = role_id
    df_for_squad = df_for_squad.join(df.iloc[:, 96:179])
    df_for_squad = df_for_squad.join(df.iloc[:, 180:263])
    return df_for_squad


# DATAFRAME FOR TACTIC VIEW
# Cut original dataframe to make readable for tactic view
# ///////////////////////////////////////////////////////////////
def create_df_for_tactic(df):
    """
    This function takes in a dataframe and a list of integers and returns a dataframe with only
    the columns that correspond to the integers in the list.

    :param df: the dataframe you want to create a new dataframe from
    :return: A dataframe with only the column of the tactic being used.
    """
    df_for_tactic = df.loc[:, [df.columns[0]]]
    return df_for_tactic


# DATAFRAME FOR SCOUTING TEAM
# Cut original dataframe to make readable for sc
# ///////////////////////////////////////////////////////////////
def create_df_for_scouting_team(df, language):
    """
    It takes a dataframe and a language, and returns a dataframe with the columns that are needed for scouting

    :param df: the dataframe you want to create a scouting team from
    :param language: the language you want to use
    :return: A dataframe with the columns:
        - Name
        - Age
        - Nationality
        - Club
        - Overall
        - Potential
        - Preferred Foot
        - International Reputation
        - Weak Foot
        - Skill Moves
        - Work Rate
        - Body Type
        - Position
    """
    role_id = text[language].a.au0
    df_for_scouting = df.loc[:, [
                                    df.columns[0],
                                    df.columns[1],
                                    df.columns[3],
                                    df.columns[6],
                                    df.columns[4],
                                    "Global",
                                ], ]
    df_for_scouting[text[language].a.au1] = "-"
    df_for_scouting[text[language].a.au2] = 1
    df_for_scouting[text[language].a.au3] = 1
    df_for_scouting[text[language].a.au4] = role_id
    df_for_scouting[text[language].a.au5] = 2
    df_for_scouting[text[language].a.au6] = role_id
    df_for_scouting[text[language].a.au7] = 3
    df_for_scouting[text[language].a.au8] = role_id
    df_for_scouting = df_for_scouting.join(df.iloc[:, 10:179])
    df_for_scouting = df_for_scouting.join(df.iloc[:, 180:263])
    return df_for_scouting
