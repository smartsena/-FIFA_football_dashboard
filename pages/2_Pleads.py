import streamlit as st
import pandas as pd
#df_data = pd.read_csv("datasets/consolidado_BI_TI_amostra_short.csv", encoding="utf8", index_col=0)

#df_data = pd.read_csv("datasets/amostra_short.csv", encoding="utf8", index_col=0)
#df_data[1]
#df_data.head()
#df_data.tail()
#df_data.info()
#df_data.columns
#df_data.describe()
#￼st.write("Olá, mundo!")

st.set_page_config(
    page_title="Pleads",
    page_icon=":dart:",
    layout="wide"
)
st.write("# Analytic Tabular: 🚀")

df = st.session_state['df_data']


clubs = df['Club'].value_counts().index
club = st.sidebar.selectbox('Clube',clubs)

# df_players = df.loc[df['Club'] == club, 'Name']
df_players = df[df['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogador', players)

player_stats = df[df["Name"] == player]
player_stats = player_stats[player_stats["Club"] == club].iloc[0]
# player_stats["Photo"]
st.image(player_stats['Photo'])
st.title(f"{player_stats['Name']}")

st.divider()

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")


col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:**  {player_stats['Age']}")
col2.markdown(f"**Altura:**  {player_stats['Height(cm.)']/100}")
col3.markdown("**Peso:** {}" .format(player_stats['Weight(lbs.)'] * 0.453))#:.2f))
# col4.markdown(f"**:** {player_stats['']}")


st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col5, col6, col7, col8 = st.columns(4)
col5.metric(label="Valor de mercado", value=f"{player_stats['Value(£)']:,}")
col6.metric(label= "Remuneração Semanal", value=f"{player_stats['Wage(£)']:,}")
col7.metric(label="Valor de rescisão", value=f"{player_stats['Release Clause(£)']:,}")
# col.metric(f"**:** {player_stats['']}")

#---------------------------------------------#
# player_stats['Photo']
# st.write("# club Analytic Tabular:")
# club

# st.write("# player Analytic Tabular:")
# player

# st.write("# df_players Analytic Tabular:")
# df_players

# st.write("# players Analytic Tabular:")
st.dataframe(player_stats, width=400)