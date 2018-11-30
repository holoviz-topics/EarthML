*******
EarthML
*******

.. raw:: html

   <div style="width: 65%; float:left">


**Machine learning and visualization in Python for Earth science**

EarthML is a "meta-project" with the aim of illustrating how other,
freely available, general-purpose open source projects may be used to
solve problems in this domain:

   - Data libraries:
      -  `Intake <https://intake.readthedocs.io>`_: Cleanly loading data from various sources.
      -  `XArray <http://xarray.pydata.org>`_: Processing gridded data structures.
      -  `Pandas <http://pandas.pydata.org>`_: Processing gridded data structures.
      -  `Dask <http://dask.pydata.org>`_: Parallelism and performance at scale.
   - Visualization libraries:
      -  `hvPlot <http://hvplot.pyviz.org>`_: Simple data-centric API for plotting, building on:
        -  `Bokeh <http://bokeh.pydata.org>`_: Interactive browser-based
           plotting.
        -  `HoloViews <http://holoviews.org>`_: Easy construction of Bokeh
           plots for datasets.
        -  `GeoViews <http://geoviews.org>`_: HoloViews with earth-specific
           projections.
        -  `Datashader <https://github.com/bokeh/datashader>`_: Rendering large
           datasets into images for display in browsers.
      -  `Panel <https://panel.pyviz.org>`_: Dashboards, apps, and widgets for any library's plots.
   - Other tools:
      - `Jupyter <http://jupyter.org/>`_
      - `Cartopy <https://scitools.org.uk/cartopy>`_
   - ML tools: (representative only -- use any you like!)
      - `Scikit-learn <https://scikit-learn.org>`_: General ML for numeric data
      - `Keras <https://keras.io>`_/`TensorFlow <https://www.tensorflow.org>`_/- `PyTorch <https://pytorch.org>`_: Deep learning, images
         

The EarthML `Tutorial <tutorial>`_ offers a general-purpose overview
of the concepts and tools involved, and the `Topics <topics>`_ section
shows examples of how these tools may be used to perform machine
learning and related tasks in the Earth sciences, such as:

.. raw:: html

   <div style="display: flex; flex-flow: column">
      <div style="display: flex; flex-flow: row">
         <a href="topics/Carbon_Flux.html">
            <img src="_static/collage/carbon.png" width=95%/>
         </a>
         <a href="topics/Heat_and_Trees.html">
            <img src="_static/collage/trees.png" width=95%/>
         </a>
      </div>
      <br></br>
      <div style="display: flex; flex-flow: row">
         <a href="topics/Walker_Lake.html">
            <img src="_static/collage/walker.png" width=95%/>
         </a>
         <a href="topics/Landsat_Spectral_Clustering.html">
            <img src="_static/collage/cluster.png" width=95%/>
         </a>
      </div>
      <br></br>
      <div style="display: flex; flex-flow: row">
         <a href="topics/Landsat_Classifier_Ensemble.html">
            <img src="_static/collage/ensemble.png" width=47%/>
         </a>
      </div>
   </div>


Please feel free to report `issues
<https://github.com/pyviz-topics/EarthML/issues>`_ or `contribute code
<https://github.com/pyviz-topics/EarthML/>`_.


------------
Installation
------------

Step 1: Install a `Miniconda <http://conda.pydata.org/miniconda.html>`_  (or `Anaconda <https://www.continuum.io/downloads>`_) environment
------------------------------------------------------------------------------------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably
Google Chrome) should be suitable. 16GB of RAM is required for some of
the examples, but most will run fine in 4GB.

If you don't already have conda on your machine, you can get it from
`Anaconda.com <http://conda.pydata.org/miniconda.html>`_, and then open
a terminal window.

If you do have conda already, it's a good idea to update it (running it
twice to get the very latest) to ensure you have the latest version::

   > conda update conda
   > conda update conda


Step 2: Clone the EarthML git repository
----------------------------------------

::

   > git clone https://github.com/pyviz-topics/EarthML.git
   > cd EarthML


Step 3: Install and activate the ``earthml`` environment
--------------------------------------------------------

::

   > conda env create -f environment.yml
   > conda activate earthml

Step 4: Run the notebook server
-------------------------------


::

   > cd examples
   > jupyter notebook


.. raw:: html

   </div>

.. toctree::
   :hidden:
   :maxdepth: 2

   Introduction <self>
   Tutorial <tutorial/index>
   Topics <topics/index>
   FAQ <FAQ>
   About <about>
