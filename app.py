import streamlit as st
import pandas as pd
import time

st.header("Climate Database",divider='grey')
st.text_input("Input Station Code", key="name")
wmo_id_select = st.session_state.name

wmo_id = pd.read_csv(f'data/WMO_ID.csv')

#metric data
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Read Station Dataset
if wmo_id_select != 0 :
    df     = pd.read_csv(f'data/{wmo_id_select}.csv')
    df     = df.drop(['Unnamed: 0', 'TEMPERATURE_AVG_C'], axis=1)


    # Write to Website
    st.write(f"Dataset Paramater Iklim Stasin {((wmo_id[wmo_id['wmo_id'] == df['WMO_ID'][0]]).Stasiun).values[0]}")
    st.dataframe(df)


    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    st.button('reset', type='primary')

    if st.button("Show TN Temperature"):
        chart_data = pd.DataFrame(df, columns=["TEMP_24H_TN_C"])
        st.line_chart(chart_data)

    elif st.button("Show TX Temperature"):
        chart_data = pd.DataFrame(df, columns=["TEMP_24H_TX_C"])
        st.line_chart(chart_data)

    elif st.button("Show Rainfall"):
        chart_data = pd.DataFrame(df, columns=["RAINFALL_24H_MM"])
        st.line_chart(chart_data)
    else:
        st.write('Silahkah pilih data yang akan di plot')

    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

else :
    st.write('Silahkan masukan kode stasiun yang dimaksud')
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
