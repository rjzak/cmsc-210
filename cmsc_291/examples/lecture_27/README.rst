Baltimore City 311 Request Data Exploration
===========================================

To get started, make sure you install these libraries::

    $> conda install numpy scikit-learn pandas jupyterlab ipywidgets matplotlib plotly Nodejs


Next, you'll need to install some Jupyterlab extensions::

    $> jupyter labextension install jupyterlab-plotly
    $> jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget

Finally, you'll want to start up the `Jupyter Lab <https://jupyterlab.readthedocs.io/en/latest/>`_ webserver::

    $> jupyter lab --config="jupyter_notebook_config.py"

When you do this, JupyterLab will open automatically in your browser.
