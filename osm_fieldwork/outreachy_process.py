import os
import subprocess
from io import BytesIO



with open("boundaries.geojson", "rb") as geojson_file:
    boundary = geojson_file.read()  
    boundary_bytesio = BytesIO(boundary)
    boundary_bytes_data = boundary_bytesio.getvalue()

command = ["pdm", "run", "python", "osm_fieldwork/basemapper.py", "-b", boundary_bytes_data, "-y", "-z", "12-15", "-s", "esri"]

subprocess.run(command)
