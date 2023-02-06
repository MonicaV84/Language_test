import streamlit as st
import pandas as pd
import plotly.express as px

import gettext



_ = gettext.gettext

st.set_page_config(
    page_title= 'Multilanguage',
    layout='wide'
)

url_titanic = 'https://drive.google.com/file/d/1w1C_69x60TX4ISktCLsBA5y2r-8BZfqo/view?usp=sharing'
path_titanic = 'https://drive.google.com/uc?export=download&id='+url_titanic.split('/')[-2]

@st.cache
def read_titanic():
    titanic = pd.read_csv(path_titanic)
    return titanic
read_titanic()
df_titanic = read_titanic()


language = st.checkbox('Marque esta casilla si quiere ver la página en inglés')
if language:
    gettext.gettext.translation('base', localedir='locales', languages=['en'])
    gettext.install('enGB')
    _ = gettext.gettext 
    

agree = st.checkbox(_('¿Quiere ver las primeras entradas del dataset?'))

if agree:
    
     st.dataframe(df_titanic.head())


groupby_column = st.sidebar.radio(
            _('Vea la cantidad de sobrevivientes según:'),
            options=('Pclass', 'Sex', 'Fare')
)

output_column = ['Survived']

df_grouped = df_titanic.groupby(by=[groupby_column], as_index=False)[output_column].sum()

fig = px.bar(
    df_grouped,
    x=groupby_column,
    y=output_column,
    template='ggplot2',
    height=550,
    title= (_('Número de sobrevivientes') + groupby_column),
    labels= 'survivers'
)
st.plotly_chart(fig)
