*******
EarthML
*******

.. raw:: html

   <div style="width: 65%; float:left">


**Machine learning and visualization in Python for Earth science**

EarthML is an `open-source
<https://github.com/ioam/holoviews/blob/master/LICENSE.txt>`_ Python
library for exploratory machine learning research in Earth
science. EarthML is designed to be a lightweight project with the aim of
illustrating how other, freely available, general-purpose open source
and `PyViz <http://pyviz.org>`_ projects may be used to solve problems
in this domain:

   -  `Bokeh <http://bokeh.pydata.org>`_: Interactive browser-based
      plotting.
   -  `HoloViews <http://holoviews.org>`_: Easy construction of Bokeh
      plots for datasets.
   -  `GeoViews <http://geoviews.org>`_: HoloViews with earth-specific
      projections.
   -  `Datashader <https://github.com/bokeh/datashader>`_: Rendering large
      datasets into images for display in browsers.
   -  `XArray <http://xarray.pydata.org>`_: Processing gridded data structures.
   -  `Dask <http://dask.pydata.org/en/latest/>`_: Parallelism and performance at scale.


.. raw:: html

   <div>
   <div >
     <a href="http://holoviews.org/gallery/demos/bokeh/iris_splom_example.html">
       <img src="http://earthml.pyviz.org/_static/collage/walker_lake.png" width='20%'>    </img> </a>
     <a href="http://holoviews.org/getting_started/Gridded_Datasets.html">
       <img src="https://assets.holoviews.org/collage/cells.png" width='22%'> </img>  </a>
     <a href="http://holoviews.org/gallery/demos/bokeh/scatter_economic.html">
       <img src="http://holoviews.org/_images/scatter_economic.png" width='43%'> </img>    </a>
   </div>
   </div>

   
We recommend the `Getting Started Guide <getting_started>`_ to learn
the basic concepts and start using Project as quickly as possible.

The `User Guide <user_guide>`_ goes into key concepts more deeply when
you are ready for further study.

The `API <Reference_Manual>`_ is the definitive guide to each EarthML
object.

Please feel free to report `issues
<https://github.com/pyviz-topics/EarthML/issues>`_ or `contribute code
<https://github.com/pyviz-topics/EarthML/>`_.


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

[OPTIONAL] If you want to keep things organized, you can then create a separate Conda environment to work in for this tutorial::

   > conda create -n pyviz-tutorial python=3.6
   > source activate pyviz-tutorial

(omitting "source" if you are on Windows).


Step 2: Install the ``pyviz`` environment
-----------------------------------------

::

   > conda install -c pyviz pyviz

Step 3: Install additional dependencies
---------------------------------------


::

   > pip install rio-toa
   > conda install -c intake intake-xarray


.. raw:: html

   </div>

.. toctree::
   :hidden:
   :maxdepth: 2

   Introduction <self>
   Getting Started <getting_started/index>
   User Guide <user_guide/index>
   Topics <topics/index>
   API <Reference_Manual/index>
   FAQ





..
   ********
   EarthSim
   ********

   **Lightweight Python tools for environmental simulation**

   EarthSim is a project for developing Python-based workflows for
   specifying, launching, visualizing, and analyzing environmental
   simulations, such as those for hydrology modeling. EarthSim is
   designed to be a lightweight project internally, relying on code and
   documentation primarily maintained in other, freely available,
   general-purpose SciPy and `PyViz <http://pyviz.org>`_ projects:

   -  `Bokeh <http://bokeh.pydata.org>`_: Interactive browser-based
      plotting.
   -  `HoloViews <http://holoviews.org>`_: Easy construction of Bokeh
      plots for datasets.
   -  `Datashader <https://github.com/bokeh/datashader>`_: Rendering large
      datasets into images for display in browsers.
   -  `Param <https://github.com/ioam/param>`_: Specifying parameters of
      interest, e.g. to make widgets.
   -  `XArray <http://xarray.pydata.org>`_: Processing gridded data structures.
   -  `GeoViews <http://geoviews.org>`_: HoloViews with earth-specific
      projections.

   This website has three main sections:

   - `Getting Started <getting_started>`_:
      How to install the code, notebooks, and data files needed for the examples.
   - `User Guide <user_guide>`_:
      Usage information for the ``earthsim`` Python package, which
      contains a small amount of code specific to environmental
      simulation such as helper functions for annotating plots and
      specifying irregular meshes.
   - `Topics <topics>`_:
      A set of Jupyter notebooks that show how to use the various PyViz
      tools together to solve earth-science problems, such as how to run
      various simulators.

   If you have any notebooks showing how to use these tools to do useful
   work in environmental simulation, we'd love to add them to the Topics!

   Please feel free to report `issues
   <https://github.com/pyviz/earthsim/issues>`_ or `contribute code.
   <https://help.github.com/articles/about-pull-requests>`_
