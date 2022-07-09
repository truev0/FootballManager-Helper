# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import warnings
import os

import numpy as np
import pandas as pd

from gui import BASE_DIR
from gui.core.dicts import en, es
from gui.core.models.CustomNestedNamespace.py_CustomNestedNamespace import (
    NestedNamespace,
)

# INITIAL CONFIGURATION TO PROCESS
# ///////////////////////////////////////////////////////////////
warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
text = {}
text.update({"en": NestedNamespace(en.column_headers)})
text.update({"es": NestedNamespace(es.column_headers)})
poss = {}
poss.update({"en": NestedNamespace(en.positions)})
poss.update({"es": NestedNamespace(es.positions)})


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
        html_filename = f"{path_file}"
        df_fmi = pd.read_html(html_filename, encoding="utf-8")[0]
    except ValueError:
        return None
    except FileNotFoundError:
        return None
    return df_fmi


# CONVERT VALUES TO ITS RESPECTIVE TYPE
# Convert value to str, float, int / replace text in number cells
# ///////////////////////////////////////////////////////////////
def convert_values(df, language):
    """
    It converts the values in the dataframe to the correct data type

    :param df: the dataframe you want to convert
    :param language: The language of the data you're using
    :return: A dataframe with the columns converted to the correct data type.
    """
    for column in [text[language].h.h10, text[language].h.h11, text[language].h.s23]:
        if column in [text[language].h.s23]:
            df[column] = df[column].astype(str).str.replace("km", "")
            df[column] = df[column].str.replace("-", "0")
            df[column] = df[column].str.replace(",", ".")
        else:
            df[column] = df[column].str.replace("N/A", "0")
            df[column] = df[column].str.replace("N/D", "0")
            df[column] = df[column].str.replace("$", "")
            df[column] = df[column].str.replace("Â", "")
            df[column] = df[column].str.replace("p/a", "")
            df[column] = df[column].str.replace("p/m", "")
            df[column] = df[column].str.replace(",", "")
            df[column] = df[column].str.replace("K", "000")
            df[column] = df[column].str.replace(".", "")
            df[column] = df[column].str.replace("M", "00000")

    for column in [
            text[language].h.s6,
            text[language].h.s3,
            text[language].h.s2,
            text[language].h.s14,
            text[language].h.s18,
            text[language].h.s21,
            text[language].h.s9,
            text[language].h.s13,
            text[language].h.s11,
            text[language].h.s1,
            text[language].h.s15,
            text[language].h.s16,
            text[language].h.s22,
            text[language].h.s4,
            text[language].h.s27,
            text[language].h.s28,
            text[language].h.s26,
            text[language].h.s5,
            text[language].h.s8,
            text[language].h.s10,
            text[language].h.s17,
            text[language].h.s19,
            text[language].h.s20,
            text[language].h.s31,
    ]:
        df[column] = df[column].str.replace("-", "0")
        if column in [
                text[language].h.s5,
                text[language].h.s8,
                text[language].h.s10,
                text[language].h.s17,
                text[language].h.s20,
        ]:
            df[column] = (
                df[column].astype(str).str.rstrip("%").astype(float)) / 100

    for column in [
            text[language].h.s6,
            text[language].h.s20,
            text[language].h.s10,
            text[language].h.s8,
            text[language].h.s5,
            text[language].h.s19,
            text[language].h.s28,
            text[language].h.s18,
            text[language].h.s27,
            text[language].h.s23,
            text[language].h.s16,
            text[language].h.s22,
            text[language].h.s15,
            text[language].h.s14,
            text[language].h.s13,
            text[language].h.s11,
            text[language].h.s9,
            text[language].h.s17,
            text[language].h.s30,
            text[language].h.s31,
    ]:
        df[column] = pd.to_numeric(df[column], downcast="float")

    for column in [
            text[language].h.s1,
            text[language].h.s2,
            text[language].h.s3,
            text[language].h.s4,
            text[language].h.s21,
            text[language].h.s26,
            text[language].h.h11,
            text[language].h.s32,
    ]:
        df[column] = pd.to_numeric(df[column], downcast="integer")

    return df


# CONVERT VALUES IN SCOUTING DATAFRAME
# Convert value to str, float, int / replace text in number cells
# ///////////////////////////////////////////////////////////////
def convert_values_scout(df):
    """
    It takes a dataframe as an input, and for each column in the dataframe, if the column is of type "object",
     it replaces all instances of "-" with "0"

    :param df: the dataframe you want to convert
    :return: A dataframe with the values converted to numeric.
    """
    for i, item in enumerate(df.columns):
        if df.dtypes[i] == "object":
            df[item] = df[item].str.replace("-", "0")
    return df


# CREATE METRICS FOR GOALKEEPERS
# Create columns and process values to create KPI for goalkeepers
# ///////////////////////////////////////////////////////////////
def create_metrics_for_gk(df, language):
    """
    It takes a dataframe and a language as input, and returns the dataframe with the following metrics added:

    - Tot_Sav: total saves made
    - Per_90: minutes played per 90 minutes
    - Saves_90: saves made per 90 minutes
    - Shots_Faced: shots faced
    - Faced_90: shots faced per 90 minutes

    The function is used in the following way:

    :param df: the dataframe you want to create the metrics for
    :param language: the language of the text in the dataframe
    :return: A dataframe with the new metrics added.
    """
    # Create Saves_90 metric (saves made per 90)
    df["Tot_Sav"] = df[text[language].h.s1] + df[text[language].h.s2] + df[text[language].h.s3]
    df["Per_90"] = df[text[language].h.h12] / 90
    df["Saves_90"] = df["Tot_Sav"] / df["Per_90"]
    # Create Faced_90 metric (shots faced per 90)
    df["Shots_Faced"] = df[text[language].h.s4] + df["Tot_Sav"]
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
    c = None
    if language == "en":
        path_file = os.path.normpath(os.path.join(BASE_DIR, "core\\fm_insider\\data_ranking_values_en.json"))
        with open(
                path_file,
                mode="r",
                encoding="utf-8",
        ) as f:
            c = f.read()
    elif language == "es":
        path_file = os.path.normpath(os.path.join(BASE_DIR, "core\\fm_insider\\data_ranking_values_es.json"))
        with open(
                path_file,
                mode="r",
                encoding="utf-8",
        ) as f:
            c = f.read()

    js_positions = json.loads(c)
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
        df[text[language].h.h4].str.contains("POR"),
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
        text[language].h.h1,
        text[language].h.h2,
        text[language].h.h4,
        text[language].h.h7,
        text[language].h.h5,
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
def create_df_for_tactic(df, language):
    """
    This function takes in a dataframe and a list of integers and returns a dataframe with only
    the columns that correspond to the integers in the list.

    :param df: the dataframe you want to create a new dataframe from
    :param language: the index of the tactic you want to create a dataframe for
    :return: A dataframe with only the column of the tactic being used.
    """
    df_for_tactic = df.loc[:, [text[language].h.h1]]
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
        text[language].h.h1,
        text[language].h.h2,
        text[language].h.h4,
        text[language].h.h7,
        text[language].h.h5,
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
