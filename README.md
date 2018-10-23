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
    <img src="_static/collage/trees.png" width='30%'>    </img> </a>
  <a href="http://earthml.pyviz.org/topics/Walker_Lake.html">
    <img src="_static/collage/walker.png" width='30%'> </img>  </a>
  <a href="http://earthml.pyviz.org/topics/landsat_spectral_clustering.html">
    <img src="_static/collage/cluster.png" width='30%'> </img>    </a>
</div>
</div>

In addition to these examples, the [Getting Started
Guide](getting_started) aims to quickly introduce the essential concepts
to help the reader understand how they can start using these tools to
solve their own problems. The [User Guide](user_guide) then offers a
more in depth overview of these concepts when you are ready for further
study. Lastly, the [API](Reference_Manual) is the definitive guide to
each EarthML object.

Please feel free to report
[issues](https://github.com/pyviz-topics/EarthML/issues) or [contribute
code](https://github.com/pyviz-topics/EarthML/).

Installation
============

Step 1: Install a [Miniconda](http://conda.pydata.org/miniconda.html) (or [Anaconda](https://docs.continuum.io/anaconda/install)) environment
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

\[OPTIONAL\] If you want to keep things organized, you can then create a
separate Conda environment to work in for this tutorial:

    > conda create -n pyviz-tutorial python=3.6
    > source activate pyviz-tutorial

(omitting "source" if you are on Windows).

Step 2: Install the `pyviz` environment
---------------------------------------

    > conda install -c pyviz pyviz

Step 3: Install additional dependencies
---------------------------------------

    > pip install rio-toa
    > conda install -c intake intake-xarray

</div>
