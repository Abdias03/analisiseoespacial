import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

APP_TITLE = 'Faud and Identity Theft Report'
APP_SUB_TITLE = 'Source: Federal Trade Commission'


def display_fraud_facts(df, year, quarter, state_name, report_type, field_name, metric_title,
                        number_format='${:,}', is_median=False):
    df = df[(df['Year'] == year) & (df['Quarter'] == quarter)
            & (df['Report Type'] == report_type)]
    if state_name:
        df = df[df['State Name'] == state_name]
    df.drop_duplicates(inplace=True)
    if is_median:
        total = df[field_name].sum() / len(df) if len(df) else 0
    else:
        total = df[field_name].sum()
    st.metric(metric_title, number_format.format(round(total)))


def display_map(df, year, quarter):
    df = df[(df['Year'] == year) & (df['Quarter'] == quarter)]

    map = folium.Map(location=[38, -96.5], zoom_start=4,
                     scrollWheelZoom=False, tiles='CartoDB positron')

    choropleth = folium.Choropleth(
        geo_data='data/us-state-boundaries.geojson',
        data=df,
        columns=('State Name', 'State Total Reports Quarter'),
        key_on='feature.properties.name',
        line_opacity=0.8,
        highlight=True)

    choropleth.geojson.add_to(map)

    df = df.set_index('State Name')
    state_name = 'North Carolina'

    for feature in choropleth.geojson.data['features']:
        state_name = feature['properties']['name']
        feature['properties']['population'] = 'Population: ' + str('{:,}'.format(
            df.loc[state_name, 'State Pop'][0]) if state_name in list(df.index) else 'N/A')
        feature['properties']['per_100k'] = 'Reports/100k Population: ' + str('{:,}'.format(
            df.loc[state_name, 'Reports per 100K-F&O together'][0])if state_name in list(df.index) else 'N/A')

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(
            ['name', 'population', 'per_100k'], labels=False)
    )

    st_map = st_folium(map, width=700, height=450)

    state_name = ''
    if st_map['last_active_drawing']:
        state_name = st_map['last_active_drawing']['properties']['name']
    return state_name

    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)


def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # LOAD DATA
    df_continental = pd.read_csv('data/AxS-Continental_Full Data_data.csv')
    df_fraud = pd.read_csv('data/AxS-Fraud Box_Full Data_data.csv')
    df_median = pd.read_csv('data/AxS-Median Box_Full Data_data.csv')
    df_loss = pd.read_csv('data/AxS-Losses Box_Full Data_data.csv')

    year = 2022
    quarter = 1
    state_name = 'Texas'
    report_type = 'Fraud'
    field_name = 'State Fraud/Other Count'
    field_name_loss = 'Total Losses'
    field_Name_Media = 'Overall Median Losses Qtr'

    # st.write(df.shape)
    # st.write(df.head())
    # st.write(df.columns)

    # DISPLAY FILTERS AND MAP
    state_name = display_map(df_continental, year, quarter)

    # DISPLAY METRICS
    st.subheader(f'{state_name} {report_type} Facts')
    col1, col2, col3 = st.columns(3)
    with col1:
        display_fraud_facts(df_fraud, year, quarter, state_name,
                            report_type, field_name, f'# of {report_type} Reports', number_format='{:,}')
    with col2:
        display_fraud_facts(df_median, year, quarter, state_name,
                            report_type, field_Name_Media, 'Median $ Loss', '${:,}', is_median=True)
    with col3:
        display_fraud_facts(df_loss, year, quarter, state_name,
                            report_type, field_name_loss, 'Total $ Loss', '${:,}')


if __name__ == "__main__":
    main()
