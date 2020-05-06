*******
EarthML
*******

.. raw:: html

   <div style="max-width: 1200; float:left">


**Machine learning and visualization in Python for Earth science**

Python offers a wide variety of open-source libraries covering a huge
range of functionality, but it can be difficult to work out which
libraries are suitable for which tasks. The EarthML project helps to:

   - Demonstrate how to use Python tools for machine learning and analysis in the earth sciences
   - Identify libraries suitable for working with earth-science data
   - Make improvements to these libraries as needed to help improve earth-science workflows

EarthML contains no code of its own, only tutorials and examples
showing how to use packages like:

- **Data libraries:**

  - `Intake <https://intake.readthedocs.io>`_: Cleanly loading data from various sources.
  - `XArray <http://xarray.pydata.org>`_: Processing gridded (n-dimensional) data structures.
  - `Pandas <http://pandas.pydata.org>`_: Processing columnar (tabular) data structures.
  - `Dask <http://dask.pydata.org>`_: Parallelism and performance at scale.

- **Visualization libraries:**

  - `hvPlot <http://hvplot.pyviz.org>`_: Simple data-centric API for plotting, building on:

    - `Bokeh <http://bokeh.pydata.org>`_: Interactive browser-based plotting.
    - `HoloViews <http://holoviews.org>`_: Easy construction of Bokeh plots for datasets.
    - `GeoViews <http://geoviews.org>`_: HoloViews with earth-specific projections.
    - `Datashader <https://github.com/bokeh/datashader>`_: Rendering large datasets into images for display in browsers.
  - `Panel <https://panel.pyviz.org>`_: Dashboards, apps, and widgets for any library's plots.

- **Other tools:**

  - `Jupyter <http://jupyter.org/>`_: Reproducible notebooks (source code for all examples on this site).
  - `Cartopy <https://scitools.org.uk/cartopy>`_: Geographic coordinate reference systems.
  - `Dask <http://dask.pydata.org>`_: Parallelism and performance at scale.

- **ML tools: (representative only -- use any you like!)**

  - `Scikit-learn <https://scikit-learn.org>`_: General ML for numeric data.
  - `Keras <https://keras.io>`_/ `TensorFlow <https://www.tensorflow.org>`_/ `PyTorch <https://pytorch.org>`_: Deep learning, images.


The EarthML `Tutorial <tutorial>`_ offers a general-purpose overview
of the concepts and tools involved, and the `Topics <topics>`_ section
shows examples of how these tools may be used to perform machine
learning and related tasks in the Earth sciences, such as:

.. raw:: html

  <style>table {border-spacing: 15px} td { border: 1px solid black; vertical-align: top} </style>
    <table>
      <tr>
        <td border=1>
          <a href="https://examples.pyviz.org/carbon_flux/"><b>Carbon Flux</b></a><br>
          <a href="https://examples.pyviz.org/carbon_flux/"><img src="_static/collage/carbon.png" /></a>
        </td>
        <td border=1>
          <a href="https://examples.pyviz.org/heat_and_trees/Heat_and_Trees.html"><b>Heat and Trees</b></a><br>
          <a href="https://examples.pyviz.org/heat_and_trees/Heat_and_Trees.html"><img src="_static/collage/trees.png" /></a>
        </td>
        <td border=1>
          <a href="https://examples.pyviz.org/walker_lake/Walker_Lake.html"><b>Walker Lake</b></a><br>
          <a href=""https://examples.pyviz.org/walker_lake/Walker_Lake.html"><img src="_static/collage/walker.png" /></a>
        </td>
      </tr>
      <tr>
        <td border=1>
          <a href="https://examples.pyviz.org/landuse_classification/Image_Classification.html"><b>Classification</b></a><br>
          <a href="https://examples.pyviz.org/landuse_classification/Image_Classification.html"><img src="_static/collage/classifier.png" /></a>
        </td>
        <td border=1>
          <a href="https://examples.pyviz.org/landsat_clustering/landuse_clustering.html"><b>Clustering</b></a><br>
          <a href="https://examples.pyviz.org/landsat_clustering/landuse_clustering.html"><img src="_static/collage/cluster.png" /></a>
        </td>
        <td border=1>
          <a href="https://examples.pyviz.org/seattle_lidar/Seattle_Lidar.html"><b>Lidar</b></a><br>
          <a href="https://examples.pyviz.org/seattle_lidar/Seattle_Lidar.html"><img src="_static/collage/lidar.png" /></a>
        </td>
      <tr>
    </table>

Please feel free to report `issues
<https://github.com/pyviz-topics/EarthML/issues>`_ or `contribute code
<https://github.com/pyviz-topics/EarthML/>`_.


----------------------------
Running the EarthML projects
----------------------------

The EarthML topic examples are included among the many examples
available on `examples.pyviz.org <https://examples.pyviz.org/>`_. Each
project is encapsulated in a reproducible project that includes an
environment specification, an optional `intake
<https://intake.readthedocs.io/en/latest/>`_ data catalog as well as
notebooks and any other necessary assets.

Instructions for running these projects with `anaconda-project
<https://github.com/Anaconda-Platform/anaconda-project>`_ in the
`examples.pyviz User Guide
<https://examples.pyviz.org/user_guide.html>`_

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
