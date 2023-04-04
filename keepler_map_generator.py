import pandas as pd
from keplergl import KeplerGl

##############
# This is a sample project create to demonstrate usage of keepler in a python script
# the script read from a file of coordinate, and then creates an html map
############


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas dataframe.
    """
    with open(file_path, 'r') as file:
        df = pd.read_csv(file)
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%dT%H:%M:%S')
        df['lat_rounded'] = df['lat'].round(6)
        df['long_rounded'] = df['long'].round(6)
    return df


def create_map(data: pd.DataFrame, config: dict) -> KeplerGl:
    """
    Create a kepler.gl map instance with the given data and configuration.
    """
    kepler_map = KeplerGl(config=config)
    kepler_map.add_data(data=data, name="coords")
    return kepler_map


def save_map(kepler_map: KeplerGl, file_path: str, data: dict, config: dict):
    """
    Save the given kepler.gl map instance to an HTML file with the given data and configuration.
    """
    kepler_map.save_to_html(file_name=file_path, data=data, config=config)


if __name__ == "__main__":
    print("Starting map creation...")

    # Load data
    data_file_path = 'data_rt4.csv'
    data = load_data(data_file_path)

    # Create config
    first_lat = data['lat'].iloc[0]
    first_lon = data['long'].iloc[0]
    config = {
        "version": "v1",
        "config": {
            "visState": {
                "layers": [
                    {
                        "id": "anyid1234",
                        "type": "point",
                        "config": {
                            "dataId": "coords",
                            "label": "Point",
                            "color": [
                                255,
                                100,
                                0
                            ],
                            "columns": {
                                "lat": "lat_rounded",
                                "lng": "long_rounded",
                            },
                            "isVisible": True,
                            "visConfig": {
                                "radius": 0.4,
                                "fixedRadius": False,
                                "opacity": 0.2,
                                "outline": True,
                                "thickness": 2,
                                "strokeColor": None,
                                "colorRange": {
                                    "name": "UberPool 8",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#800000",
                                        "#9A6324",
                                        "#808000",
                                        "#469990",
                                        "#000075",
                                        "#e6194B",
                                        "#f58231",
                                        "#ffe119",
                                        "#bfef45",
                                        "#3cb44b",
                                        "#42d4f4",
                                        "#4363d8",
                                        "#911eb4",
                                        "#f032e6",
                                        "#a9a9a9",
                                        "#fabed4",
                                        "#ffd8b1",
                                        "#fffac8",
                                        "#aaffc3",
                                        "#dcbeff",
                                        "#ffffff"

                                    ],
                                    "reversed": True
                                },
                                "strokeColorRange": {
                                    "name": "Global Warming",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#FFFF66",
                                        "#FC6E22",
                                        "#FF1493",
                                        "#C24CF6",
                                        "#F1920E",
                                        "#00FECA",
                                        "#08F7F0"
                                    ]
                                },
                                "radiusRange": [
                                    2,
                                    12
                                ],
                                "filled": True
                            },
                            "hidden": False
                        },
                        "visualChannels": {
                            "colorField": {
                                "name": "time_bucket",
                                "type": "integer"
                            },
                            "colorScale": "ordinal",
                            "strokeColorField": {
                                "name": "session_color",
                                "type": "string"
                            },
                            "strokeColorScale": "ordinal",
                            "sizeScale": "sqrt"
                        }
                    }
                ],
            },
            "mapState": {
                "bearing": 0,
                "dragRotate": False,
                "latitude": first_lat,
                "longitude": first_lon,
                "pitch": 0,
                "zoom": 17,
                "isSplit": False
            },
        }
    }

    # Create map
    kepler_map = create_map(data=data, config=config)

    # Save map
    map_file_path = 'new_map.html'
    save_map(kepler_map=kepler_map, file_path=map_file_path, data={"coords": data}, config=config)

    print("Map creation complete.")
