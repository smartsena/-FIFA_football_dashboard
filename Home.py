import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime


st.set_page_config(
    page_title="Pleads",
    page_icon="⚽",
    layout="wide"
)
##-------------------------##
##-------------------------##
##-------------------------##

year_dataset = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
# year = st.sidebar.selectbox("Ano", year_dataset)

fifa_years = st.sidebar.radio(
    "Fifa_years fifa_years",
    year_dataset,
    # [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."]
)
if fifa_years:
    st.header('FIFA OFFICIAL DATASET' ⚽ :rainbow[YEAR {}]'.format(fifa_years)) 
    # st.header(type("xpto "+str(fifa_years)))
    # st.header("xpto "+str(fifa_years))
st.sidebar.markdown("Projeto Lucas Sena Alves(https://smartsena.github.io/portifolio_projetos")


##-------------------------##
##-------------------------##
##-------------------------##

# if fifa_years
if "df_data" not in st.session_state:
    fifa2023 = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", encoding="utf8", index_col=0)
    fifa2022 = pd.read_csv("datasets/CLEAN_FIFA22_official_data.csv", encoding="utf8", index_col=0)
    fifa2021 = pd.read_csv("datasets/CLEAN_FIFA21_official_data.csv", encoding="utf8", index_col=0)
    fifa2020 = pd.read_csv("datasets/CLEAN_FIFA20_official_data.csv", encoding="utf8", index_col=0)
    fifa2019 = pd.read_csv("datasets/CLEAN_FIFA19_official_data.csv", encoding="utf8", index_col=0)
    fifa2018 = pd.read_csv("datasets/CLEAN_FIFA18_official_data.csv", encoding="utf8", index_col=0)
    fifa2017 = pd.read_csv("datasets/CLEAN_FIFA17_official_data.csv", encoding="utf8", index_col=0)
    # df = "fifa"+str(fifa_years).copy()
    # print(df)
    # print(type(df))
    # https://docs.streamlit.io/library/api-reference/session-state
    
    df = fifa2023
    # print(df)
    
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by="Overall", ascending=False)
    df = df.reset_index(drop=True)
    st.session_state["df_data"] = df
    
if "data_old" not in st.session_state:
    df_old = pd.read_csv("datasets/consolidado_BI_TI_amostra_short.csv", encoding="utf8", index_col=0)
    st.session_state["data_old"] = df_old

##-------------------------##
##-------------------------##
##-------------------------##


st.header("FIFA23 OFFICIAL DATASET")    
btn_kaggle_fifa23 = st.button("KAGGLE FIFA23")
btn_portifoil = st.button("Portifólio de Projetos")

if btn_kaggle_fifa23:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
if btn_portifoil:
    webbrowser.open_new_tab("https://smartsena.github.io/portifolio_projetos")

st.markdown("""
About Dataset
CONTEXT

The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.

COLUMNS

ID: A unique identifier for each player.
Name: The name of the player.
Age: The age of the player at the time of data collection.
Photo: A link or reference to the player's photograph.
Nationality: The nationality of the player.
Flag: The national flag associated with the player's nationality.
Overall: The overall rating of the player's skills and abilities.
Potential: The potential rating representing the player's future development.
Club: The current club affiliation of the player.
Club Logo: A link or reference to the logo of the player's club.
Value (£): .
Wage (£): The player's weekly wage in pounds (£).
Special: A numerical value representing the player's special abilities.
Preferred Foot: The player's preferred foot for playing.
International Reputation: A rating indicating the player's international reputation.
Weak Foot: A rating representing the player's weaker foot abilities.
Skill Moves: The number of skill moves the player possesses.
Work Rate: The work rate of the player.
Body Type: The physical build or body type of the player.
Real Face: Indicates whether the player has a real face representation.
Position: The player's preferred playing position.
Joined: The date when the player joined the current club.
Loaned From: The club from which the player is currently on loan.
Contract Valid Until: The date until which the player's contract is valid.
Height (cm.): The height of the player in centimeters.
Weight (lbs.): The weight of the player in pounds.
Release Clause (£): The release clause value of the player in pounds (£).
Kit Number: The player's kit number.
Best Overall Rating: The player's highest overall rating.
Year Joined: The year when the player joined the current club.
ACKNOWLEDGEMENT
We would like to acknowledge the original contributor https://www.kaggle.com/bryanb of this football dataset for providing the foundation upon which our cleaned and uploaded dataset is built.

Check out the link below for original dataset!
https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1
"""
)

