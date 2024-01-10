import streamlit as st
import plotly.express as px
import os
import pandas as pd

df = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/hdata/scatter_region_preprocessed_data.csv', encoding='UTF-8')

def main(df):
    st.title("Animation")
    st.write("수도권 시군구별 고소득 종사자 비율과 다양한 변수간의 관계")
    years = ['2016', '2017', '2018', '2019', '2020', '2021']
    year_start = 2016
    year_end = 2021
    year_step = 1

    st.sidebar.markdown("## Housing Price Data")
    year_range = st.sidebar.slider("Select Year Range", 2016, 2021, (year_start, year_end), year_step)
    region = st.sidebar.multiselect("Select Area", df['area'].unique())

    df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    if region:
        df_filtered = df[df['area'].isin(region)]

    st.write("Showing data from", year_range[0], "to", year_range[1])

    fig = px.scatter(df_filtered, x='highincomeratio', y='totalnum', color='area', size='price', hover_name='region',animation_frame='year', range_x=[0, max(df['highincomeratio'])+5], range_y=[0, max(df['totalnum'])+100])
    fig.update_layout(title='마커의 크기 : 제곱 미터당 집값 (10000원)', xaxis_title='고소득 종사자 비율 (%)', yaxis_title='총 종사자 수 (1000 명)')
    st.plotly_chart(fig)

    fig2 = px.scatter(df_filtered, x='highincomeratio', y='population', color='area', size='price', hover_name='region', animation_frame='year', range_x=[0, max(df['highincomeratio']) + 5], range_y=[0, max(df['population']) + 300000])
    fig2.update_layout(title='마커의 크기 : 제곱 미터당 집값 (10000원)', xaxis_title='고소득 종사자 비율 (%)', yaxis_title='총 인구 수 (1000 명)')
    st.plotly_chart(fig2)

    fig3 = px.scatter(df_filtered, x='highincomeratio', y='wageaverage', color='area', size='price', hover_name='region', animation_frame='year', range_x=[0, max(df['highincomeratio']) + 5], range_y=[min(df['wageaverage']) - 10, max(df['wageaverage']) + 10])
    fig3.update_layout(title='마커의 크기 : 제곱 미터당 집값 (10000원)', xaxis_title='고소득 종사자 비율 (%)', yaxis_title='원천징수지 기준 1인당 평균 연봉 (100만원)')
    st.plotly_chart(fig3)

if __name__ == '__main__':
    main(df)
