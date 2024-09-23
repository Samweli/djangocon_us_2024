# Open-source Python tools to visualize and analyse geospatial data.

This repository contains materials used and showcased in the DjangoCon US 2024 talk about
the open-source python tools used in the analysis and visualization of geospatial data.

The repository includes scripts to animate world temperature data, analyze bus routes, and perform other geospatial analyses using Jupyter notebooks and Python scripts integrated with QGIS.


## Running talks examples

The examples provided in this repository can be run either through jupterbook or on a linux terminal 
after installing the needed requirements.


## Getting Started

### Prerequisites

To run the project, ensure you have the following installed:

1. **Python 3.x**: Python is required to run the scripts.
3. **Docker**: If you wish to run the application in a containerized environment.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samweli/djangocon_us_2024.git
   cd djangocon_us_2024
2. **Start juypter notebook**
   ```bash
   docker-compose up --build
3. Once the container is running, you'll see a URL in the console output. It will look something like:
    ```bash 
      http://127.0.0.1:8888/?token=your_secret_token 
    ```
4. Open this URL in your web browser. You'll be taken to the Jupyter Notebook interface.


## Resources 
- Geopandas - https://geopandas.org
- Rasterio - https://rasterio.readthedocs.io
- QGIS Python API - https://qgis.org/pyqgis <br>
  Documentation site for the QGIS Python API
- QGIS Python plugins repository -  https://plugins.qgis.org/plugins
- QGIS website - https://qgis.org

### Contributing
Feel free to contribute to the project by submitting pull requests or issues on GitHub.