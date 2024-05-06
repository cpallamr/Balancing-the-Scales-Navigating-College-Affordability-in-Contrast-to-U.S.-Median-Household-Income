
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Output, Input
import numpy as np

# Read the data
df = pd.read_excel("/Users/chaitu/Downloads/PROJECT/merged_data.xlsx")

# Access data for universities
df_universities = df[["State", "Latitude_location_2022", "Longitude_location_2022", "Institution_name",
                      "Control_of_Institution"]]

# Create mapbox access token (replace with your actual token)
mapbox_access_token = "pk.eyJ1Ijoic2Fpa3Jpc2huYW1hcmlrdWthbGEiLCJhIjoiY2x1ZW1kbnEwMXM3dDJtcDlnN3g3emYyYyJ9.BGvjA0jQoKK1KwHsg7WaNg"

# Define initial traces (universities and tuition costs)
university_trace = go.Scattermapbox(
    lat=df_universities["Latitude_location_2022"],
    lon=df_universities["Longitude_location_2022"],
    text=df_universities["Institution_name"],
    marker_color=["blue" if control == "Public" else "red" for control in df_universities["Control_of_Institution"]],
    marker_size=14,
    name="University Name"
)

# Create the figure with initial traces
fig4 = go.Figure([university_trace])
fig4.update_layout(mapbox_style="open-street-map", mapbox_zoom=3, mapbox_center={"lat": 37.0902, "lon": -95.7129}, showlegend=False)

# Create a Dash app
app6 = Dash(__name__)
# Define app layout
app6.layout = html.Div([
    html.H1("Universities and In State Tuition Cost"),
    html.Div([
        dcc.Graph(
            id="map",
            figure=fig4,
            style={'width': '1500px', 'height': '750px', 'margin': 'auto'}
        ),
        html.Div([
            dcc.Dropdown(
                id="state_dropdown",
                options=[{"label": "All States", "value": "All States"}] + [{"label": state, "value": state} for state in df_universities["State"].unique()],
                value="All States",
                clearable=False,
            ),
            dcc.Dropdown(
                id="control_dropdown",
                options=[{"label": "All", "value": "all"}] + [{"label": control, "value": control} for control in df_universities["Control_of_Institution"].unique()],
                value="all",
                clearable=False,
            ),
            dcc.Dropdown(
                id="university_dropdown",
                options=[],
                value="",
                placeholder="Select a University",
                clearable=False
            ),
        ], style={'position': 'absolute', 'top': '50px', 'right': '50px'}),
        dcc.Graph(id="tuition_trend_graph")
    ], style={'text-align': 'center'})
])

# Update university dropdown options based on state selection
@app6.callback(
    Output("university_dropdown", "options"),
    Input("state_dropdown", "value")
)
def update_university_options(state_value):
    if state_value == "All States":
        university_options = [{"label": university, "value": university} for university in df_universities["Institution_name"].unique()]
    else:
        university_options = [{"label": university, "value": university} for university in df_universities[df_universities["State"] == state_value]["Institution_name"].unique()]
    return university_options

# Update callback function based on dropdown selection
@app6.callback(
    Output("map", "figure"),
    [Input("state_dropdown", "value"),
     Input("control_dropdown", "value")]
)
def update_figure(state_value, control_value):
    filtered_df = df_universities.copy()
    if state_value != "All States":
        filtered_df = filtered_df[filtered_df["State"] == state_value]

    university_trace = go.Scattermapbox(
        lat=filtered_df["Latitude_location_2022"],
        lon=filtered_df["Longitude_location_2022"],
        text=filtered_df["Institution_name"],
        marker_color=["blue" if control == "Public" else "red" for control in filtered_df["Control_of_Institution"]],
        marker_size=14,
        name="University Name"
    )

    if control_value != "all":
        filtered_df = filtered_df[filtered_df["Control_of_Institution"] == control_value]

    fig4 = go.Figure([university_trace])
    fig4.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=3,
        mapbox_center={"lat": 37.0902, "lon": -95.7129},
        showlegend=False
    )

    return fig4

# Update trend graph based on university selection
@app6.callback(
    Output("tuition_trend_graph", "figure"),
    Input("university_dropdown", "value")
)
def update_tuition_trend(university_value):
    if university_value:
        # Fetch data for the selected university
        university_data = df[df["Institution_name"] == university_value]
        years = [f"In_state_tuition_{year}" for year in range(2002, 2023)]
        median_income_years = [f"Median_income_{year}" for year in range(2002, 2023)]
        
        # Calculate percentage change in median income from previous year
        median_income_changes = np.round(((university_data[median_income_years].values[0][1:] - university_data[median_income_years].values[0][:-1]) / university_data[median_income_years].values[0][:-1]) * 100, 2)
        
        # Plot trend graph
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years[::-1], y=university_data[years].values[0][::-1], mode='lines+markers', name='Tuition'))
        fig.add_trace(go.Scatter(x=median_income_years[::-1][1:], y=university_data[median_income_years].values[0][::-1][1:], mode='lines+markers', name='Median Income'))
        fig.add_trace(go.Bar(x=median_income_years[::-1][1:], y=median_income_changes[::-1], name='% Change in Median Income', yaxis="y2"))
        
        fig.update_layout(title=f'Tuition and Median Income Trend for {university_value}', xaxis_title='Year', yaxis_title='Amount')
        fig.update_yaxes(title_text='% Change', secondary_y=True)
        return fig
    else:
        return {}

# Run the Dash app
if __name__ == "__main__":
    app6.run_server(debug=True)
