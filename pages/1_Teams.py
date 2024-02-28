import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Pleads",
    page_icon="⚽",
    layout="wide"
)


# ------------------------
# ---Open session--------------------
# ------------------------
df = st.session_state["df_data"]

# ------------------------
# ---Sidebar---------------------
# ------------------------
clubs = df['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubs)

df_club = df[df['Club'] == club]#.set_index("Name")

# ------------------------
# ---Page---------------------
# ------------------------

show_columns = ['Name', 'Age', 'Photo', 'Nationality', 'Overall',
       'Value(£)', 'Wage(£)', 'Position', 'Flag',
       # 'Joined', 'Contract Valid Until', 'Height(cm.)',
       'Weight(lbs.)', 'Release Clause(£)', 'Year_Joined']

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header(club)
    with col2:    
        st.image(df_club.iloc[0]['Club Logo'])
    st.markdown("""---""")

with st.container():
    st.subheader("Analyzing the team: 🎯")
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

st.markdown("""---""")

with st.container():
    st.subheader("Overall rating of the player's")
    df_aux = df_club.loc[:,['Name','Overall']].sort_values(['Overall','Name'])
    df_fig = px.bar(df_aux, x='Overall', y='Name')
    st.plotly_chart(df_fig, user_container_with=True)                 

with st.container():
    st.subheader("Player's weekly wage in pounds (£)")
    df_aux = df_club.loc[:,['Name','Value(£)']].sort_values(['Value(£)','Name'])
    df_fig = px.bar(df_aux, x='Value(£)', y='Name')
    st.plotly_chart(df_fig, user_container_with=True)
