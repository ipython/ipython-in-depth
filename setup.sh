conda env create -f environment.yml

source activate scipy18jlab

NODE_OPTIONS=--max_old_space_size=4096 jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-threejs ipyvolume bqplot @jupyterlab/geojson-extension @jupyterlab/fasta-extension

NODE_OPTIONS=--max_old_space_size=4096 jupyter labextension install jupyterlab-toc jupyter-leaflet @jupyter-widgets/jupyterlab-sidecar
