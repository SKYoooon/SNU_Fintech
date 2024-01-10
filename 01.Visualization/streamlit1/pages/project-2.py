import matplotlib
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import bar_chart_race as bcr
from matplotlib import rc
import ffmpeg
import matplotlib.animation as animation
import streamlit.components.v1 as components
import base64
import plotly.express as px
import plotly.graph_objects as go
rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

def main():
    # Load data
    st.title("Total number of employees")
    df1 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/total_worker.csv', encoding='utf-8')
    df1 = df1.transpose()
    df1.columns= ['서울 남부', '서울 북부', '경기 북부','경기 남부','인천']
    df1.drop('Unnamed: 0', axis=0, inplace=True)
    y_var = st.multiselect('지역을 선택하세요', df1.columns)

    fig = plt.figure(figsize=(15, 10))
    fig, ax = plt.subplots()

    st.line_chart(df1, y=y_var)
    # year = [2016, 2017, 2018, 2019, 2020, 2021]

    st.markdown("---")

    st.title("Monthly Earnings By Industry")

    # load data
    df10 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/wt5.csv', encoding='utf-8')
    df10.index = df10['Unnamed: 0']
    df10.drop(['Unnamed: 0'], axis=1, inplace=True)
    
    html_str= bcr.bar_chart_race(
        df = df10,
        n_bars=10,
        figsize=(8, 5),
        sort='desc',
        period_length =700,
        period_label={'x': .98, 'y': .2, 'ha': 'right','size': 31},
        perpendicular_bar_func='mean',
        title='Monthly Earnings By Industry',

        ).data


    start = html_str.find('base64,') + len('base64,')
    end = html_str.find('">')

    video = base64.b64decode(html_str[start:end])
    st.video(video)
    df10

    st.markdown("---")
    st.title("Relative ratio of the Top 4 industries with high income")
    data1 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/Gangnam.csv', encoding='utf-8')
    data2 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/Gangbuk.csv', encoding='utf-8')
    data3 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/ggnam.csv', encoding='utf-8')
    data4 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/ggbuk.csv', encoding='utf-8')
    data5 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/incheon.csv', encoding='utf-8')

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    df4 = pd.DataFrame(data4)
    df5 = pd.DataFrame(data5)

    years = st.selectbox('Year', ['2016', '2017', '2018', '2019', '2020', '2021'])

    cols = st.columns([0.5, 1, 1, 0.5])
    cols2 = st.columns([1, 1, 1])

    with cols[1]:
        fig = px.pie(df1, values=years, names='Job',
                     title='강남',
                     height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        st.plotly_chart(fig, use_container_width=True)

    with cols[2]:
        fig = px.pie(df2, values=years, names='Job',
                     title='강북',
                     height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        st.plotly_chart(fig, use_container_width=True)

    with cols2[0]:
        fig = px.pie(df3, values=years, names='Job',
                     title='경기 북부',
                     height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        st.plotly_chart(fig, use_container_width=True)

    with cols2[1]:
        fig = px.pie(df4, values=years, names='Job',
                     title='경기 남부',
                     height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        st.plotly_chart(fig, use_container_width=True)

    with cols2[2]:
        fig = px.pie(df5, values=years, names='Job',
                     title='인천',
                     height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0), )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # 보여주기!
    
    st.title("High-income Earners(2021)")

    tree1 = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/page2data/treemap.csv', encoding='utf-8' )

    fig = px.treemap(tree1, path=['total', '수도권', '시군구별'], values='highincome_num',
                     color='house_price', hover_data=['ratio'],
                     color_continuous_scale='reds')
    # Show plot
    st.plotly_chart(fig)

    st.markdown("---")

if __name__ == '__main__':
    main()