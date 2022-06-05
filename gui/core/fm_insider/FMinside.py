# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import pandas as pd
import plotly.express as px
import numpy as np
import json
import warnings
from gui.core.translations import en, es
from gui.core.models.CustomNestedNamespace.py_CustomNestedNamespace import NestedNamespace

# INITIAL CONFIGURATION TO PROCESS
# ///////////////////////////////////////////////////////////////
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
text = {}
text.update({'en': NestedNamespace(en.column_headers)})
text.update({'es': NestedNamespace(es.column_headers)})
poss = {}
poss.update({'en': NestedNamespace(en.positions)})
poss.update({'es': NestedNamespace(es.positions)})

# SETTING PANDAS
# Load file to create the dataframe
# ///////////////////////////////////////////////////////////////
def setting_up_pandas(path_file, btn_press):
    pd.set_option('styler.render.max_columns', 100)
    pd.set_option('styler.render.max_rows', 100)
    pd.set_option('styler.format.precision', 0)
    # pd.options.display.float_format = '{:20,.2f}'.format
    # LOADING SQUAD FILE
    if btn_press == 'squad_btn':
        try:
            html_filename = r"{}".format(path_file)
            df_p = pd.read_html(html_filename, encoding='utf-8')[0]
        except ValueError:
            return None
        except FileNotFoundError:
            return None
        return df_p
    # LOADING SCOUTING FILE
    elif btn_press == 'scout_btn':
        try:
            html_filename = r"{}".format(path_file)
            df_s = pd.read_html(html_filename, encoding='utf-8')[0]
        except ValueError:
            return None
        except FileNotFoundError:
            return None
        return df_s

# CONVERT VALUES TO ITS RESPECTIVE TYPE
# Convert value to str, float, int / replace text in number cells
# ///////////////////////////////////////////////////////////////
def convert_values(df, l):
    for column in [text[l].h.h10, text[l].h.h11, text[l].h.s23
                   ]:
        if column in [text[l].h.s23]:
            df[column] = df[column].astype(str).str.replace('km', '')
            df[column] = df[column].str.replace('-', '0')
            df[column] = df[column].str.replace(',', '.')
        else:
            df[column] = df[column].str.replace('N/A', '0')
            df[column] = df[column].str.replace('$', '')
            df[column] = df[column].str.replace('Â', '')
            df[column] = df[column].str.replace('p/a', '')
            df[column] = df[column].str.replace('p/m', '')
            df[column] = df[column].str.replace(',', '')
            df[column] = df[column].str.replace('K', '000')
            df[column] = df[column].str.replace('.', '')
            df[column] = df[column].str.replace('M', '00000')

    for column in [text[l].h.s6, text[l].h.s3, text[l].h.s2, text[l].h.s14, text[l].h.s18, text[l].h.s21, text[l].h.s9,
                   text[l].h.s13, text[l].h.s11, text[l].h.s1, text[l].h.s15, text[l].h.s16, text[l].h.s22,
                   text[l].h.s4, text[l].h.s27, text[l].h.s28, text[l].h.s26, text[l].h.s5, text[l].h.s8,
                   text[l].h.s10, text[l].h.s17, text[l].h.s19, text[l].h.s20,
                   ]:
        df[column] = df[column].str.replace('-', '0')
        if column in [text[l].h.s5, text[l].h.s8, text[l].h.s10, text[l].h.s17, text[l].h.s20, ]:
            df[column] = (df[column].astype(str).str.rstrip('%').astype(float)) / 100

    for column in [text[l].h.s6, text[l].h.s20, text[l].h.s10, text[l].h.s8, text[l].h.s5, text[l].h.s19,
                   text[l].h.s28, text[l].h.s18, text[l].h.s27, text[l].h.s23, text[l].h.s16, text[l].h.s22,
                   text[l].h.s15, text[l].h.s14, text[l].h.s13, text[l].h.s11, text[l].h.s9, text[l].h.s17,
                   text[l].h.s30]:
        df[column] = pd.to_numeric(df[column], downcast="float")

    for column in [text[l].h.s1, text[l].h.s2, text[l].h.s3, text[l].h.s4, text[l].h.s21, text[l].h.s26, text[l].h.h11]:
        df[column] = pd.to_numeric(df[column], downcast="integer")

    for column in [text[l].h.s6, text[l].h.s9, text[l].h.s11, text[l].h.s13, text[l].h.s14, text[l].h.s15, text[l].h.s16,
                   text[l].h.s18, text[l].h.s19, text[l].h.s22, text[l].h.s27, text[l].h.s28]:
        df[column] = df[column].div(100).round(2)
    return df

# CREATE METRICS FOR GOALKEEPERS
# Create columns and process values to create KPI for goalkeepers
# ///////////////////////////////////////////////////////////////
def create_metrics_for_gk(df, l):
    # Create Saves_90 metric (saves made per 90)

    df['Tot_Sav'] = df[text[l].h.s1] + df[text[l].h.s2] + df[text[l].h.s3]
    df['Per_90'] = df[text[l].h.h12] / 90
    df['Saves_90'] = df['Tot_Sav'] / df['Per_90']
    # Create Faced_90 metric (shots faced per 90)
    df['Shots_Faced'] = df[text[l].h.s4] + df['Tot_Sav']
    df['Faced_90'] = df['Shots_Faced'] / df['Per_90']
    return df

# ROUND DATA
# Round all float values to 2 decimals
# ///////////////////////////////////////////////////////////////
def round_data(df):
    tmp = df.select_dtypes(include=[np.number, np.float])
    df.loc[:, tmp.columns] = np.round(tmp, decimals=2)
    return df

# DATA FOR RANKINGS
# Load data to make metrics for rankings
# ///////////////////////////////////////////////////////////////
def data_for_rankings(df, lang):
    file = None
    if lang == 'en':
        file = open("gui/core/fm_insider/data_ranking_values_en.json", mode="r", encoding="utf-8")
    elif lang == 'es':
        file = open("gui/core/fm_insider/data_ranking_values_es.json", mode="r", encoding="utf-8")
    c = file.read()
    file.close()
    js_positions = json.loads(c)
    for p in range(len(js_positions["positionEvaluation"]) - 1):
        aux_string = js_positions["positionEvaluation"][p]["position"]
        aux_coef1 = js_positions["positionEvaluation"][p]["coef1"]
        aux_coef2 = js_positions["positionEvaluation"][p]["coef2"]
        df[aux_string] = 0
        for e in range(len(js_positions["positionEvaluation"][p]["sumElements"])):
            tmp_value = js_positions["positionEvaluation"][p]["sumElements"][e]
            df[aux_string] = df[aux_string] + df[tmp_value]
        df[aux_string] = (df[aux_string] / aux_coef1) + aux_coef2

    cols1 = js_positions["positionEvaluation"][83]["sumElements"]
    cols2 = js_positions["positionEvaluation"][83]["gralSum"]
    cols_d = cols1 + cols2
    cols3 = js_positions["positionEvaluation"][83]["elementsProm"]
    df['Global'] = np.where(df[text[lang].h.h4].str.contains('POR'), df[cols_d].sum(1).div(33), df[cols3].mean(1))

    return df

# RANK VALUES
# Make a rank with values previously setted
# ///////////////////////////////////////////////////////////////
def ranking_values(df):
    f = lambda x: x.replace(x[-1], x[-1] + '_rank')
    df = df.join(df.iloc[:, 94:177].rank(axis=1, method='first', ascending=False).astype(int).rename(columns=f))
    return df

# SCORES FOR POSITION
# Create scores for every position in game for every player in dataframe
# ///////////////////////////////////////////////////////////////
def create_scores_for_position(df, l):
    # Create score for each position and club DNA.\n",
    df['dna_score'] = df[text[l].h.a46] + df[text[l].h.a44] + df[text[l].h.a34] + df[text[l].h.a6] + df[text[l].h.a2] \
                      + df[text[l].h.a1] + df[text[l].h.a9]

    df[poss[l].p3 + "_score"] = df[text[l].h.a47] + df[text[l].h.a41] + df[text[l].h.a40] + df[text[l].h.a27] + \
                                df[text[l].h.a24] + df[text[l].h.a11] + df[text[l].h.a10] + df[text[l].h.a4] + \
                                df[text[l].h.a17] + df[text[l].h.a15] + df[text[l].h.a30] + df[text[l].h.a44] + \
                                df[text[l].h.a3] + df[text[l].h.a35] + df[text[l].h.a13] + df[text[l].h.a39] + \
                                df[text[l].h.a38] + df[text[l].h.a1] + df[text[l].h.a45]

    df[poss[l].p8 + "_score"] = df[text[l].h.a26] + df[text[l].h.a20] + df[text[l].h.a7] + df[text[l].h.a46] + df[
        text[l].h.a44] \
                                + df[text[l].h.a42] + df[text[l].h.a35] + df[text[l].h.a13] + df[text[l].h.a39] + df[
                                    text[l].h.a38] \
                                + df[text[l].h.a16] + df[text[l].h.a8] + df[text[l].h.a25]

    df[poss[l].p21 + "_score"] = df[text[l].h.a36] + df[text[l].h.a33] + df[text[l].h.a20] + df[text[l].h.a15] + df[
        text[l].h.a7] \
                                 + df[text[l].h.a5] + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a35] + df[
                                     text[l].h.a18] \
                                 + df[text[l].h.a13] + df[text[l].h.a6] + df[text[l].h.a2] + df[text[l].h.a38] + df[
                                     text[l].h.a1] \
                                 + df[text[l].h.a45] + df[text[l].h.a16] + df[text[l].h.a9]

    df[poss[l].p22 + "_score"] = df[text[l].h.a36] + df[text[l].h.a33] + df[text[l].h.a20] + df[text[l].h.a15] + df[
        text[l].h.a7] \
                                 + df[text[l].h.a5] + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a35] + df[
                                     text[l].h.a29] \
                                 + df[text[l].h.a18] + df[text[l].h.a13] + df[text[l].h.a6] + df[text[l].h.a2] + df[
                                     text[l].h.a38] \
                                 + df[text[l].h.a1] + df[text[l].h.a45] + df[text[l].h.a16] + df[text[l].h.a9]

    df[poss[l].p18 + "_score"] = df[text[l].h.a36] + df[text[l].h.a33] + df[text[l].h.a15] + df[text[l].h.a7] + df[
        text[l].h.a5] \
                                 + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a35] + df[text[l].h.a29] + df[
                                     text[l].h.a18] \
                                 + df[text[l].h.a6] + df[text[l].h.a2] + df[text[l].h.a39] + df[text[l].h.a1] + df[
                                     text[l].h.a45] \
                                 + df[text[l].h.a43] + df[text[l].h.a16] + df[text[l].h.a9]

    df[poss[l].p32 + "_score"] = df[text[l].h.a20] + df[text[l].h.a15] + df[text[l].h.a7] + df[text[l].h.a46] + df[
        text[l].h.a44] \
                                 + df[text[l].h.a35] + df[text[l].h.a13] + df[text[l].h.a6] + df[text[l].h.a2] + df[
                                     text[l].h.a39] \
                                 + df[text[l].h.a38] + df[text[l].h.a9] + df[text[l].h.a8]

    df[poss[l].p40 + "_score"] = df[text[l].h.a20] + df[text[l].h.a15] + df[text[l].h.a7] + df[text[l].h.a46] + df[
        text[l].h.a44] \
                                 + df[text[l].h.a42] + df[text[l].h.a6] + df[text[l].h.a2] + df[text[l].h.a38] + df[
                                     text[l].h.a45] \
                                 + df[text[l].h.a16] + df[text[l].h.a9] + df[text[l].h.a8]

    df[poss[l].p38 + "_score"] = df[text[l].h.a15] + df[text[l].h.a5] + df[text[l].h.a30] + df[text[l].h.a44] + df[
        text[l].h.a3] \
                                 + df[text[l].h.a35] + df[text[l].h.a18] + df[text[l].h.a6] + df[text[l].h.a2] + df[
                                     text[l].h.a39] \
                                 + df[text[l].h.a43]

    df[poss[l].p35 + "_score"] = df[text[l].h.a31] + df[text[l].h.a22] + df[text[l].h.a20] + df[text[l].h.a15] + df[
        text[l].h.a7] \
                                 + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a35] + df[text[l].h.a18] + df[
                                     text[l].h.a13] \
                                 + df[text[l].h.a2] + df[text[l].h.a39] + df[text[l].h.a38] + df[text[l].h.a1] + df[
                                     text[l].h.a43] \
                                 + df[text[l].h.a16] + df[text[l].h.a9] + df[text[l].h.a8]

    df[poss[l].p44 + "_score"] = df[text[l].h.a15] + df[text[l].h.a7] + df[text[l].h.a5] + df[text[l].h.a30] + df[
        text[l].h.a44] \
                                 + df[text[l].h.a3] + df[text[l].h.a35] + df[text[l].h.a18] + df[text[l].h.a13] + df[
                                     text[l].h.a6] \
                                 + df[text[l].h.a2] + df[text[l].h.a39] + df[text[l].h.a38] + df[text[l].h.a9]

    df[poss[l].p68 + "_score"] = df[text[l].h.a36] + df[text[l].h.a33] + df[text[l].h.a22] + df[text[l].h.a15] + df[
        text[l].h.a5] \
                                 + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a3] + df[text[l].h.a35] + df[
                                     text[l].h.a29] \
                                 + df[text[l].h.a18] + df[text[l].h.a39] + df[text[l].h.a1] + df[text[l].h.a45] + df[
                                     text[l].h.a16]

    df[poss[l].p65 + "_score"] = df[text[l].h.a33] + df[text[l].h.a31] + df[text[l].h.a22] + df[text[l].h.a15] + df[
        text[l].h.a5] \
                                 + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a3] + df[text[l].h.a29] + df[
                                     text[l].h.a18] \
                                 + df[text[l].h.a39] + df[text[l].h.a1] + df[text[l].h.a45] + df[text[l].h.a43] + df[
                                     text[l].h.a16]

    df[poss[l].p66 + "_score"] = df[text[l].h.a33] + df[text[l].h.a31] + df[text[l].h.a22] + df[text[l].h.a15] + df[
        text[l].h.a5] \
                                 + df[text[l].h.a30] + df[text[l].h.a44] + df[text[l].h.a29] + df[text[l].h.a18] + df[
                                     text[l].h.a39] \
                                 + df[text[l].h.a1] + df[text[l].h.a45] + df[text[l].h.a43] + df[text[l].h.a16]

    df[poss[l].p59 + "_score"] = df[text[l].h.a33] + df[text[l].h.a22] + df[text[l].h.a15] + df[text[l].h.a5] + df[
        text[l].h.a30] \
                                 + df[text[l].h.a44] + df[text[l].h.a3] + df[text[l].h.a35] + df[text[l].h.a29] + df[
                                     text[l].h.a18] \
                                 + df[text[l].h.a39] + df[text[l].h.a45]

    df[poss[l].p49 + "_score"] = df[text[l].h.a33] + df[text[l].h.a15] + df[text[l].h.a5] + df[text[l].h.a30] + df[
        text[l].h.a44] \
                                 + df[text[l].h.a3] + df[text[l].h.a35] + df[text[l].h.a29] + df[text[l].h.a18] + df[
                                     text[l].h.a6] \
                                 + df[text[l].h.a39] + df[text[l].h.a45]

    df[poss[l].p83 + "_score"] = df[text[l].h.a33] + df[text[l].h.a31] + df[text[l].h.a15] + df[text[l].h.a5] + df[
        text[l].h.a30] \
                                 + df[text[l].h.a44] + df[text[l].h.a3] + df[text[l].h.a35] + df[text[l].h.a29] + df[
                                     text[l].h.a18] \
                                 + df[text[l].h.a6] + df[text[l].h.a39] + df[text[l].h.a1] + df[text[l].h.a45] + df[
                                     text[l].h.a43]

    df[poss[l].p78 + "_score"] = df[text[l].h.a31] + df[text[l].h.a30] + df[text[l].h.a46] + df[text[l].h.a44] + df[
        text[l].h.a42] \
                                 + df[text[l].h.a35] + df[text[l].h.a18] + df[text[l].h.a6] + df[text[l].h.a2] + df[
                                     text[l].h.a39] \
                                 + df[text[l].h.a38] + df[text[l].h.a1] + df[text[l].h.a45] + df[text[l].h.a43] + df[
                                     text[l].h.a16] \
                                 + df[text[l].h.a9] + df[text[l].h.a8]
    return df

# DATAFRAME FOR SQUAD VIEW
# Cut original dataframe to make readable for squad view
# ///////////////////////////////////////////////////////////////
def create_df_for_squad(df, l):
    role_es = '<- EDITA'
    role_en = '<- EDIT'
    df_for_squad = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.h4, text[l].h.h7, text[l].h.h5, 'Global']]
    if l == 'en':
        df_for_squad["Role Ideal"] = '-'
        df_for_squad["Role Score"] = 1
        df_for_squad['Frol'] = 1
        df_for_squad['Role 1S'] = role_en
        df_for_squad['Srol'] = 2
        df_for_squad['Role 2S'] = role_en
        df_for_squad['Trol'] = 3
        df_for_squad['Role 3S'] = role_en
    elif l == 'es':
        df_for_squad["Rol Ideal"] = '-'
        df_for_squad["Ptj Rol"] = 1
        df_for_squad['Frol'] = 1
        df_for_squad['Rol 1S'] = role_es
        df_for_squad['Srol'] = 2
        df_for_squad['Rol 2S'] = role_es
        df_for_squad['Trol'] = 3
        df_for_squad['Rol 3S'] = role_es
    df_for_squad = df_for_squad.join(df.iloc[:, 94:177])
    df_for_squad = df_for_squad.join(df.iloc[:, 196:279])
    return df_for_squad

# DATAFRAME FOR TACTIC VIEW
# Cut original dataframe to make readable for tactic view
# ///////////////////////////////////////////////////////////////
def create_df_for_tactic(df, l):
    df_for_tactic = df.loc[:, [text[l].h.h1]]
    return df_for_tactic

# DATAFRAME FOR EVERY POSITION
# Cut original dataframe to make readable for positions
# ///////////////////////////////////////////////////////////////
def create_df_for_position(df, l):
    # Create custom DataFrame for each position and club DNA
    dna = df.loc[:, [text[l].h.h1, text[l].h.h3, text[l].h.h2, text[l].h.a46, text[l].h.a44, text[l].h.a34,
                     text[l].h.a6, text[l].h.a2, text[l].h.a1, text[l].h.a9, 'dna']]

    sk_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a47, text[l].h.a41, text[l].h.a40, text[l].h.a27,
                       text[l].h.a24, text[l].h.a11, text[l].h.a10, text[l].h.a4, text[l].h.a17, text[l].h.a15,
                       text[l].h.a30, text[l].h.a44, text[l].h.a3, text[l].h.a35, text[l].h.a13, text[l].h.a39,
                       text[l].h.a38, text[l].h.a1, text[l].h.a45, poss[l].p3]]

    cd_de = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a26, text[l].h.a20, text[l].h.a7, text[l].h.a46,
                       text[l].h.a44, text[l].h.a42, text[l].h.a35, text[l].h.a13, text[l].h.a39, text[l].h.a38,
                       text[l].h.a16, text[l].h.a8, text[l].h.a25, poss[l].p8]]

    wb_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a36, text[l].h.a33, text[l].h.a20, text[l].h.a15,
                       text[l].h.a7, text[l].h.a5, text[l].h.a30, text[l].h.a44, text[l].h.a35, text[l].h.a18,
                       text[l].h.a13, text[l].h.a6, text[l].h.a2, text[l].h.a38, text[l].h.a1, text[l].h.a45,
                       text[l].h.a16, text[l].h.a9, poss[l].p21]]

    wb_at = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a36, text[l].h.a33, text[l].h.a20, text[l].h.a15,
                       text[l].h.a7, text[l].h.a5, text[l].h.a30, text[l].h.a44, text[l].h.a35, text[l].h.a29,
                       text[l].h.a18, text[l].h.a13, text[l].h.a6, text[l].h.a2, text[l].h.a38, text[l].h.a1,
                       text[l].h.a45, text[l].h.a16, text[l].h.a9, poss[l].p22]]

    cwb_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a36, text[l].h.a33, text[l].h.a15, text[l].h.a7,
                        text[l].h.a5, text[l].h.a30, text[l].h.a44, text[l].h.a35, text[l].h.a29, text[l].h.a18,
                        text[l].h.a6, text[l].h.a2, text[l].h.a39, text[l].h.a1, text[l].h.a45, text[l].h.a43,
                        text[l].h.a16, text[l].h.a9, poss[l].p18]]

    dm_de = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a20, text[l].h.a15, text[l].h.a7, text[l].h.a46,
                       text[l].h.a44, text[l].h.a35, text[l].h.a13, text[l].h.a6, text[l].h.a2, text[l].h.a39,
                       text[l].h.a38, text[l].h.a9, text[l].h.a8, poss[l].p32]]

    bwm_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a20, text[l].h.a15, text[l].h.a7, text[l].h.a46,
                        text[l].h.a44, text[l].h.a42, text[l].h.a6, text[l].h.a2, text[l].h.a38, text[l].h.a45,
                        text[l].h.a16, text[l].h.a9, text[l].h.a8, poss[l].p40]]

    dlp_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a15, text[l].h.a5, text[l].h.a30, text[l].h.a44,
                        text[l].h.a3, text[l].h.a35, text[l].h.a18, text[l].h.a6, text[l].h.a2, text[l].h.a39,
                        text[l].h.a43, poss[l].p38]]

    vol_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a31, text[l].h.a22, text[l].h.a20, text[l].h.a15,
                        text[l].h.a7, text[l].h.a30, text[l].h.a44, text[l].h.a35, text[l].h.a18, text[l].h.a13,
                        text[l].h.a2, text[l].h.a39, text[l].h.a38, text[l].h.a1, text[l].h.a43, text[l].h.a16,
                        text[l].h.a9, text[l].h.a8, poss[l].p35]]

    car_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a15, text[l].h.a7, text[l].h.a5, text[l].h.a30,
                        text[l].h.a44, text[l].h.a3, text[l].h.a35, text[l].h.a18, text[l].h.a13, text[l].h.a6,
                        text[l].h.a2, text[l].h.a39, text[l].h.a38, text[l].h.a9, poss[l].p44]]

    iw_at = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a36, text[l].h.a33, text[l].h.a22, text[l].h.a15,
                       text[l].h.a5, text[l].h.a30, text[l].h.a44, text[l].h.a3, text[l].h.a35, text[l].h.a29,
                       text[l].h.a18, text[l].h.a39, text[l].h.a1, text[l].h.a45, text[l].h.a16, poss[l].p68]]

    if_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a33, text[l].h.a31, text[l].h.a22, text[l].h.a15,
                       text[l].h.a5, text[l].h.a30, text[l].h.a44, text[l].h.a3, text[l].h.a29, text[l].h.a18,
                       text[l].h.a39, text[l].h.a1, text[l].h.a45, text[l].h.a43, text[l].h.a16, poss[l].p65]]

    if_at = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a33, text[l].h.a31, text[l].h.a22, text[l].h.a15,
                       text[l].h.a5, text[l].h.a30, text[l].h.a44, text[l].h.a29, text[l].h.a18, text[l].h.a39,
                       text[l].h.a1, text[l].h.a45, text[l].h.a43, text[l].h.a16, poss[l].p66]]

    am_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a33, text[l].h.a22, text[l].h.a15, text[l].h.a5,
                       text[l].h.a30, text[l].h.a44, text[l].h.a3, text[l].h.a35, text[l].h.a29, text[l].h.a18,
                       text[l].h.a39, text[l].h.a45, poss[l].p59]]

    ap_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a33, text[l].h.a15, text[l].h.a5, text[l].h.a30,
                       text[l].h.a44, text[l].h.a3, text[l].h.a35, text[l].h.a29, text[l].h.a18, text[l].h.a6,
                       text[l].h.a39, text[l].h.a45, poss[l].p49]]

    f9_su = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a33, text[l].h.a31, text[l].h.a15, text[l].h.a5,
                       text[l].h.a30, text[l].h.a44, text[l].h.a3, text[l].h.a35, text[l].h.a29, text[l].h.a18,
                       text[l].h.a6, text[l].h.a39, text[l].h.a1, text[l].h.a45, text[l].h.a43, poss[l].p83]]

    pf_at = df.loc[:, [text[l].h.h1, text[l].h.h2, text[l].h.a31, text[l].h.a30, text[l].h.a46, text[l].h.a44,
                       text[l].h.a42, text[l].h.a35, text[l].h.a18, text[l].h.a6, text[l].h.a2, text[l].h.a39,
                       text[l].h.a38, text[l].h.a1, text[l].h.a45, text[l].h.a43, text[l].h.a16, text[l].h.a9,
                       text[l].h.a8, poss[l].p78]]


# METRICS
# Model metrics to make it visible
# ///////////////////////////////////////////////////////////////
def metric_choice(df, choice):
    if choice == "Paradas":
        fig = px.scatter(df,
                         x="Saves_90",
                         y="Faced_90",
                         text="Name",
                         log_x=False,
                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800, title_text='Goalkeepers')
        fig.show()
        return fig
    elif choice == "Duelos Terrestres":
        fig = px.scatter(
            df,
            x="Tck",
            y="Int/90",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Tackles Won/90')
        fig.update_yaxes(title_text='Interceptions/90')
        fig.update_layout(template="plotly_dark", title="Ground Duels")
        fig.show()
        return fig
    elif choice == "Duelos aereos":
        fig = px.scatter(
            df,
            x="Hdrs W/90",
            y="Hdr %",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Headers Won/90')
        fig.update_yaxes(title_text='Headers Won %')
        fig.update_layout(template="plotly_dark", title="Aerial Duels")
        fig.show()
        return fig
    elif choice == "Habilidad para transportar":
        fig = px.scatter(
            df,
            x="Ch C/90",
            y="DrbPG",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Progressive Passes/90')
        fig.update_yaxes(title_text='Progressive Runs/90')
        fig.update_layout(template="plotly_dark", title="Ball carrying skills")
        fig.show()
        return fig
    elif choice == "Habilidad de centros":
        fig = px.scatter(
            df,
            x="Cr C",
            y="Cr C/A",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Crossed Completed/90')
        fig.update_yaxes(title_text='Crossing Accuracy')
        fig.update_layout(title="Crossing ability")
        fig.show()
        return fig
    elif choice == "Habilidad de pase":
        fig = px.scatter(
            df,
            x="Ps C/90",
            y="Pas %",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Passes Completed/90')
        fig.update_yaxes(title_text='Pass Completion %')
        fig.update_layout(template="plotly_dark", title="Passing Ability")
        fig.show()
        return fig
    elif choice == "Creacion con amplitud":
        fig = px.scatter(
            df,
            x="Cr C",
            y="K Ps/90",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Crossed Completed/90')
        fig.update_yaxes(title_text='Key Passes/90')
        fig.update_layout(template="plotly_dark", title="Wide Creation")
        fig.show()
        return fig
    elif choice == "Impacto en ataque":
        fig = px.scatter(
            df,
            x="Gls/90",
            y="Asts/90",
            text="Name",
            log_x=False,
            size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=500)
        fig.update_xaxes(title_text='Goals/90')
        fig.update_yaxes(title_text='Assists/90')
        fig.update_layout(template="plotly_dark", title="Attacking Impact")
        fig.show()
        return fig
    elif choice == "Eficiencia de gol":
        fig = px.scatter(df,
                         x="Gls/90",
                         y="ShT/90",
                         text="Name",
                         log_x=False,
                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800, title_text='Goalscoring Efficiency')
        fig.show()
        return fig
    elif choice == "Creacion de juego":
        fig = px.scatter(df,
                         x="K Ps/90",
                         y="Ch C/90",
                         text="Name",
                         log_x=False,
                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800, title_text='Playmakers')
        fig.show()
        return fig
    elif choice == "Creacion de gol":
        fig = px.scatter(df, x="Ch C/90", y="Asts/90", text="Name",
                         title="Goal Creation (Chances Created/90 vs Assists/90)", log_x=False, size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.show()
        return fig
    elif choice == "Juego por banda":
        fig = px.scatter(df,
                         x="Drb/90",
                         y="Asts/90",
                         text="Name",
                         log_x=False,
                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800, title_text='Wing Play')
        fig.show()
        return fig
    elif choice == "Mejores entradores":
        fig = px.scatter(df,
                         x="Tck_90",
                         y="Tck R",
                         text="Name",
                         log_x=False,
                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800, title_text='Best Tacklers')
        fig.show()
        return fig
    elif choice == "Perfil de edad":
        fig = px.scatter(df,
                         x="Age",
                         y="Mins",
                         text="Name",
                         title="Current Squad - Squad Age Profile",
                         log_x=False,
                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white")
        # legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_layout(shapes=[
            dict(type='line',
                 line_color="white",
                 line_width=550,
                 opacity=0.1,
                 yref='paper',
                 y0=0,
                 y1=1,
                 xref='x',
                 x0=26.5,
                 x1=26.5)
        ])
        fig.show()
        return fig
    elif choice == "Perfil salarial":
        # Tratar de separar financial
        fig = px.scatter(df,
                         x="Mins",
                         y="Salary",
                         text="Name",
                         log_x=False,

                         size_max=60)
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800,
                          font_family="Century Gothic",
                          font_color="white",
                          title_font_family="Century Gothic",
                          title_font_color="white",
                          legend_title_font_color="white")
        fig.update_xaxes(title_font_family="Century Gothic")
        fig.update_traces(textposition='top center')
        fig.update_layout(height=800, title_text='Current Squad - Value for Money')
        fig.show()
        return fig