import streamlit as st
import pandas as pd
# import webbrowser
from datetime import datetime


st.set_page_config(
    page_title="Pleads",
    page_icon="⚽",
    layout="wide"
)


##-------------------------##
##---Sidebar----------------------##
##-------------------------##
fifa_years = st.sidebar.radio(
    "FIFA YEAR",
    [2023], # [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    captions = ["Base FIFA 2023"]
)

st.sidebar.markdown("https://github.com/smartsena/FIFA_football_dashboard/")

##-------------------------##
##---Load DataSet----------------------##
##-------------------------##

def clean_code(df):
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by="Overall", ascending=False)
    df = df.reset_index(drop=True)
    
    return(df)

if "df_data" not in st.session_state:
    df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", encoding="utf8", index_col=0)
    df = clean_code(df)
    st.session_state["df_data"] = df
    
# if "data_old" not in st.session_state:
#     df_old = pd.read_csv("datasets/consolidado_BI_TI_amostra_short.csv", encoding="utf8", index_col=0)
#     st.session_state["data_old"] = df_old

##-------------------------##
##---Page----------------------##
##-------------------------##
if fifa_years:
    st.header('FIFA OFFICIAL DATASET ⚽ :rainbow[YEAR {}]'.format(fifa_years))

btn_kaggle_fifa23 = st.button("KAGGLE FIFA23")
btn_portifoil = st.button("Portifólio de Projetos")

if btn_kaggle_fifa23:
    # webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    st.sidebar.markdown("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
if btn_portifoil:
    # webbrowser.open_new_tab("https://smartsena.github.io/portifolio_projetos")
    st.sidebar.markdown("https://smartsena.github.io/portifolio_projetos")

st.markdown("""
#### About Dataset CONTEXT

The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.
""")
tab1, tab2 = st.tabs(["**About this Dashboard**", "**Dataset Columns**"])
with tab1:
    st.markdown("""
        Para todos os apaixonados por futebol entrego esse Dashboard.
        Com a riquissima base dispolibilizada no [FIFA23 OFFICIAL DATASET(CLEAN DATA)](https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/). 
        \n
        Surgiu a ideia de apresentar os dados de forma mais inteligevel. Foi criado esse projeto para melhor visualização dos Times e seus Jogadores.

        ---
        
        Esse projeto continua em aprimoramento. Para o estado atual, trazemos análises por **DUAS PERSPECTIVAS**:
        \n
        1. ##### Por TIME: 
            - Visualize os jogadores pertencentes ao time escolhido no ano selecionado. São exibidos gráficos para comparação dos jogoderes que compõe o time e é exibida uma planilha tratada com informações fornecidas pelos dados. 
        \n
        2. ##### Por JOGADOR: 
            - Escolha o time e o jogador a ser analisado no ano selecionado. Apontamos algumas métricas para facilitar na hora de descidir qual o jogador é o melhor. Assim fica fácil de montar seu time dos sonhos.
    """)

with tab2:
    st.markdown("""
    ACKNOWLEDGEMENT
    We would like to acknowledge the original contributor https://www.kaggle.com/bryanb of this football dataset for providing the foundation upon which our cleaned and uploaded dataset is built.

    Check out the link below for original dataset!
    https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?rvi=1
    
    ---
    
    - ORIGINAL DATASET FIELDS:
    """)
    
    # - ORIGINAL DATASET FIELDS:
    st.markdown("""
    COLUMNS         |   DESCRIPTION
    :---------:     |       :---------
    **ID**          |        *A unique identifier for each player.*
    **Name**        |        *The name of the player.*
    **Age**         |        *The age of the player at the time of data collection.*
    **Photo**       |        *A link or reference to the player's photograph.*
    **Nationality** |        *The nationality of the player.*
    **Flag**        |        *The national flag associated with the player's nationality.*
    **Overall**     |        *The overall rating of the player's skills and abilities.*
    **Potential**   |        *The potential rating representing the player's future development.*
    **Club**        |        *The current club affiliation of the player.*
    **Club Logo**   |        *A link or reference to the logo of the player's club.*
    **Value (£)**   |        *Player's weekly wage in pounds (£).*
    **Wage (£)**    |        *The player's weekly wage in pounds (£).*
    **Special**     |        *A numerical value representing the player's special abilities.*
    **Weak Foot**   |        *A rating representing the player's weaker foot abilities.*
    **Skill Moves** |        *The number of skill moves the player possesses.*
    **Work Rate**   |        *The work rate of the player.*
    **Body Type**   |        *The physical build or body type of the player.*
    **Real Face**   |        *Indicates whether the player has a real face representation.*
    **Position**    |        *The player's preferred playing position.*
    **Joined**      |        *The date when the player joined the current club.*
    **Loaned From** |        *The club from which the player is currently on loan.*
    **Kit Number**  |        *The player's kit number.*
    **International Reputation**    |        *A rating indicating the player's international - reputation.*
    **Preferred Foot**              |        *The player's preferred foot for playing.*
    **Contract Valid Until**        |        *The date until which the player's contract is valid.*
    **Height (cm.)**                |        *The height of the player in centimeters.*
    **Weight (lbs.)**               |        *The weight of the player in pounds.*
    **Release Clause (£)**          |        *The release clause value of the player in pounds (£).*
    **Best Overall Rating**         |        *The player's highest overall rating.*
    **Year Joined**                 |        *The year when the player joined the current club.*
    """)





