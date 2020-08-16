import plotly.express as px

import pandas as pd
import json


class Utils:
    def load_csv(self, path):
        df = pd.read_csv(path)
        df.drop(columns='Siglas', inplace=True)

        df['Numero de visitas'] = df['Numero de visitas'].str.replace(
            ',', '').astype(int)

        columns = ['Clave SIINAH', 'Ano', 'Mes']
        df[columns] = df[columns].astype('Int64').astype('object')

        df['Clave SIINAH'].fillna('0000000', inplace=True)

        return df

    def _load_geojson(self, path):
        with open(path, encoding='utf-8') as json_data:
            geojson = json.load(json_data, strict=False)

        return geojson

    def plot_map(self, data, title, color='Numero de visitas'):
        path = 'mexicogeo.json'
        geojson_mx = self._load_geojson(path)
        fig = px.choropleth(data.reset_index(),
                            geojson=geojson_mx,
                            featureidkey='properties.name',
                            locations='Estado',
                            hover_name='Estado',
                            color=color,
                            animation_frame='Mes',
                            color_continuous_scale='Electric',
                            scope='north america'
                            )

        fig.update_geos(showcountries=True, showcoastlines=True,
                        showland=True, fitbounds='locations')
        fig.update_layout(title_text=title)

        fig.show()

    def plot_bar(self, data, x, y, title, **kwargs):
        fig = px.bar(data.reset_index(),
                    x=x,
                    y=y,
                    title=title,
                    barmode='group',
                    **kwargs
                    )
        fig.show()


class Query:
    def __init__(self, df):
        self.df = df

    def get_total(self, group_columns):
        return self.df.groupby(group_columns).sum()

    def get_average(self, group_columns):
        return self.df.groupby(group_columns).mean().round().astype(int)

    def get_percentage(self, total_group, aditional_group):
        group = self.df.groupby(total_group + aditional_group).sum()
        total = self.df.groupby(total_group).sum()

        group_total = group.join(total, on=total_group, rsuffix='_total')
        group_total['percentage'] = group_total['Numero de visitas'] * \
            100 / group_total['Numero de visitas_total']

        return group_total
