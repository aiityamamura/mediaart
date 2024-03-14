import streamlit as st
import pandas as pd
import plotly.express as px

# 広めのレイアウト
st.set_page_config(layout="wide")
# タイトルの設定
st.title('はじめてのStreamlit')
# 3分割
col1, col2, col3 = st.columns((1, 2, 3))

df = pd.DataFrame(
    [[10, 20, 30], [20, 30, 5], [30, 36, 43]],
    index=['A', 'B', 'C'], columns=['AA', 'BB', 'CC']
)
# 左
with col1:
    st.radio('Streamlitが好きですか？', ['好き', '嫌い', 'どちらとも言えない'])
# 真ん中
with col2:
    st.table(df)
# 右
with col3:
    st.line_chart(df)
