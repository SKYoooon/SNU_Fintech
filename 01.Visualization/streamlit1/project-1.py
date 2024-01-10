import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc
rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False


def main():

    st.title('Population and House prices')
    st.markdown("---")
    st.subheader("Population growth rate and apartment price growth rate")
    img = Image.open('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/data/img1.png')
    st.image(img)

    st.markdown("---")

    st.subheader("Population and house price trend in Seoul")
    price_df = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/data/korea_price.csv', encoding='UTF-8')
    population_df = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/data/korea_population.csv', encoding='UTF-8')

    seoul_price_array = np.array(price_df.iloc[0])[1:]
    seoul_population_array = (np.array(population_df.iloc[0])[1:]) / 10000



    st.write("연도별 서울시 제곱 미터당 집 값 (10000원) 및 인구수(10000명) 비교\n")
    years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111)
    ax.plot(years, seoul_population_array, color='dodgerblue', linewidth=3)
    ax.plot(years, seoul_population_array, "bo", markersize=10)

    ax2 = plt.twinx()
    ax2.plot(years, seoul_price_array, color='violet', linewidth=3)
    ax2.plot(years, seoul_price_array, "ro", markersize=10)
    plt.rcParams['font.family'] = 'AppleGothic'  # 나눔바른고딕 적용하기
    ax.set_xlabel('연도', fontsize=12)
    ax.set_ylabel('인구수(10000명)', fontsize=12)
    ax2.set_ylabel('제곱 미터당 집 값(10000원)', fontsize=12)
    st.pyplot(fig)
    st.markdown("---")

if __name__ == "__main__":
    main()