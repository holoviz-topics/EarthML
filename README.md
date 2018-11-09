# EarthML

**Machine learning and visualization in Python for Earth science**

EarthML is an
[open-source](https://github.com/ioam/holoviews/blob/master/LICENSE.txt)
Python library for exploratory machine learning research in Earth
science. EarthML is designed to be a lightweight project with the aim of
illustrating how other, freely available, general-purpose open source
and [PyViz](http://pyviz.org) projects may be used to solve problems in
this domain:

> -   [Bokeh](http://bokeh.pydata.org): Interactive
>     browser-based plotting.
> -   [HoloViews](http://holoviews.org): Easy construction of Bokeh
>     plots for datasets.
> -   [GeoViews](http://geoviews.org): HoloViews with
>     earth-specific projections.
> -   [Datashader](https://github.com/bokeh/datashader): Rendering large
>     datasets into images for display in browsers.
> -   [XArray](http://xarray.pydata.org): Processing gridded
>     data structures.
> -   [Dask](http://dask.pydata.org/en/latest/): Parallelism and
>     performance at scale.

A major goal of this website is to demonstrate examples of how Python
tools may be used to perform machine learning tasks in the earth
sciences. A number of such examples are available in the
[Topics](topics) section:

<div>
<div >
  <a href="http://earthml.pyviz.org/topics/trees.html">
    <img src="doc/_static/collage/trees.png" width='30%'>    </img> </a>
  <a href="http://earthml.pyviz.org/topics/Walker_Lake.html">
    <img src="doc/_static/collage/walker.png" width='30%'> </img>  </a>
  <a href="http://earthml.pyviz.org/topics/landsat_spectral_clustering.html">
    <img src="doc/_static/collage/cluster.png" width='30%'> </img>    </a>
</div>
</div>

In addition to these examples, the [Tutorial](tutorial) offers an
in depth overview of these concepts when you are ready for further
study.

Please feel free to report
[issues](https://github.com/pyviz-topics/EarthML/issues) or [contribute
code](https://github.com/pyviz-topics/EarthML/).

Installation
============

Step 1: Install a [Miniconda](http://conda.pydata.org/miniconda.html) (or [Anaconda](https://www.continuum.io/downloads)) environment
-------------------------------------------------------------------------------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably
Google Chrome) should be suitable. 16GB of RAM is required for some of
the examples, but most will run fine in 4GB.

If you don't already have conda on your machine, you can get it from
[Anaconda.com](http://conda.pydata.org/miniconda.html), and then open a
terminal window.

If you do have conda already, it's a good idea to update it (running it
twice to get the very latest) to ensure you have the latest version:

    > conda update conda
    > conda update conda

Step 2: Clone the EarthML git repository
----------------------------------------

    > git clone https://github.com/pyviz-topics/EarthML.git
    > cd EarthML

Step 3: Install and activate the ``earthml`` environment
--------------------------------------------------------
    > conda env create -f environment.yml
    > conda activate earthml

Step 4: Run the notebook server
-------------------------------
    > cd examples
    > jupyter notebook

</div>
