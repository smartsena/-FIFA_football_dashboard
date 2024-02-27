import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Pleads",
    page_icon="⚽",
    layout="wide"
)



st.write("# Analytic Tabular: 🎯")

df = st.session_state["df_data"]
print(df.columns)


clubs = df['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubs)

df_club = df[df['Club'] == club]#.set_index("Name")

st.image(df_club.iloc[0]['Club Logo'])
st.subheader(club)

# df_club.set_index["Name"]
# df_club

show_columns = ['Name', 'Age', 'Photo', 'Nationality', 'Overall',
       'Value(£)', 'Wage(£)', 'Position', 'Flag',
       # 'Joined', 'Contract Valid Until', 'Height(cm.)',
       'Weight(lbs.)', 'Release Clause(£)', 'Year_Joined']



st.dataframe(df_club[show_columns],
             column_config={
                 'Overall': st.column_config.ProgressColumn(
                     "Overall Plead",
                     help="The overall rating of the player's skills and abilities",
                     format="$%f",
                     min_value=0,
                     max_value=100,
                 ),
                 'Value(£)':st.column_config.NumberColumn(
                     "Value(£)",
                     help="The estimated market value of the player in pounds (£)",
                     # step=1,
                     format="£ %d",
                 ),
                 'Wage(£)':st.column_config.ProgressColumn(
                     "Weekly Wage",
                     help="The player's weekly wage in pounds (£)",
                     min_value=0,
                     max_value=df_club['Wage(£)'].max(),
                     format="£ %f",
                 ),
                     
                 'Photo':st.column_config.ImageColumn(
                     "Photo",
                     help="A link or reference to the player's photograph.",
                 ),
                 'Flag':st.column_config.ImageColumn(
                     "Flag",
                     help="The national flag associated with the player's nationality.",
                 ),
             },hide_index=True,height=1000,use_container_width=True,
            )
                 





# st.dataframe(df_club[show_columns], use_container_width=True, column_order=("Overall", "Value(£)"))


             
df_club2 = df[df['Club'] == club]


df_club2





