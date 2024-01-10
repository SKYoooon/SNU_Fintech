import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image
from matplotlib import rc

rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False


## 파일 로드

df = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/hdata/scatter_total_preprocessed_data.csv', encoding='UTF-8')
df_array = np.array(df)
#print(df.columns)

## 데이터 array 화
price_list = np.array(df['price'])
totalnum_list = np.array(df['totalnum'])
highincomeratio_list = np.array(df['highincomeratio'])
population_list = np.array(df['population'])
wagemoney_list = np.array(df['wagemoney'])
wageaverage_list = np.array(df['wageaverage'])

##
df2 = pd.DataFrame()
df2['price'] = price_list                        # 단위 : 10000 원 / 제곱 미터
df2['totalnum'] = totalnum_list                  # 단위 : 1000명
df2['highincomeratio'] = highincomeratio_list    # 단위 : % (고소득자 비율 : 고소득 직종 종사자 수 / 총 종사자 수)
df2['population'] = population_list              # 단위 : 명
df2['wagemoney'] = wagemoney_list                # 단위 : 100만원
df2['wageaverage'] = wageaverage_list            # 단위 : 100만원

df2_array = np.array(df2)
heatmap_df2 = df2.corr()

def main():
    st.title("House prices and various variables")
    st.subheader("Heatmap:")
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_df2, annot=True, cmap = "YlGnBu", linewidths=0.5)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.markdown("히트맵을 통하여 인구와 집값과의 상관관계가 낮음을 알 수 있고, 고소득 일자리 비율과 집값과의 상관관계가 높음을 알 수 있다.")
    st.markdown("---")

    st.title('Analysis')
    st.subheader("고소득 비율과 집값의 상관관계")
    img = Image.open('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/hdata/conclusion_scatter.png')
    st.image(img)

    st.markdown("---")

    st.title('Conclusion')
    st.subheader("고소득 비율과 집값의 상관관계에 대한 지도")
    img = Image.open('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/hdata/conclusion_1.png')
    st.image(img)

    st.markdown("---")
    
    img = Image.open('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/hdata/conclusion10.png')
    st.image(img)

    st.markdown("---")


if __name__ == "__main__":
    main()
