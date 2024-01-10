import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc
import plotly.express as px
import plotly.graph_objects as go
rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

def main():

    import streamlit as st
    import pandas as pd
    import altair as alt

    df = pd.read_csv('/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/3data/wage_price.csv', encoding='utf-8')

    st.title('Wages and House Prices by Region')
    st.write('Data from 2016 to 2021')

    selected_year = st.slider('Select Year', min_value=2016, max_value=2021, step=1)

    filtered_df = df[df['year'] == selected_year]

    melted_df = filtered_df.melt(id_vars=['Region'], value_vars=['wage', 'house_price'], var_name='metric')

    chart = alt.Chart(melted_df).mark_bar().encode(
        x=alt.X('Region', axis=alt.Axis(title='Region'), sort=['Region A', 'Region B', 'Region C']),
        y=alt.Y('value', title='Value'),
        color='metric',
        column='metric',
        tooltip=['Region', 'metric', 'value']
    ).properties(
        width=200,
        height=400,
        title=f'Wage and House Price for {selected_year}'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=12
    )

    st.altair_chart(chart)
    st.markdown("---")
    st.title("Mapping Wages and House Prices")

    image_dict = {
        "서울":"/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/3data/s_img.png",
        "경기":"/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/3data/gg_img.png",
        "인천":"/Users/ysk/Documents/7th_Fintech/04.Visual/PROJECT/streamlit1/pages/3data/ic_img.png"
    }

    selected_image_name = st.selectbox("Choose an region:", list(image_dict.keys()))

    image_path = image_dict[selected_image_name]
    image = Image.open(image_path)

    st.image(image, caption=selected_image_name, use_column_width=True)

    st.markdown("---")

if __name__ == "__main__":
    main()
