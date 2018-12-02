***
FAQ
***

Questions we have been asked by users, plus potential pitfalls we hope to help users avoid:


What is EarthML, really?
========================

EarthML is a tutorial-based website that shows how to use open-source tools from the Python ecosystem to solve problems in earth science and climate science, focusing on machine learning and other automated analysis techniques.  To make it easy for you to run these tutorials and get started on your own projects, we also provide an environment specification for installing matching versions of these tools suitable for all the tasks covered in the tutorial.

Along the way, the EarthML project has contributed a wide range of improvements to the available open-source packages, including Dask, Dask-ML, HoloViews, GeoViews, Intake, Panel, and Datashader.  You don't have to do anything special to get these improvements; they are just part of the projects now. But you'll benefit from them when you run any of the tutorials or you use these tools in your own work.


Who runs the EarthML project?
=============================

EarthML is supported by `NASA Goddard Space Flight Center <https://www.nasa.gov/goddard>`_ through a partnership with `Anaconda, Inc. <http://anaconda.com>`_.


What packages are included?
===========================

The `environment.yml <https://github.com/pyviz-topics/EarthML/environment.yml>`_ included with EarthML lists all the packages needed to run the tutorials and examples. These specific packages were included as the currently best available options satisfying the following criteria:
- Fully open source
- Fully scriptable for batch runs and remote HPC jobs
- Fully scalable to large datasets and distributed or HPC systems, both for computation and for visualization
- Fully Pythonic, without having to switch to other tools or languages (C/Fortran/JS/Scala/Java/Matlab/QGIS) to get things done
- Fully interactive visualizations and custom applications
- Simple entry points, with deep support for later customization and elaboration
- Support for keeping the details of data sources and of visualization toolkits distinct from core domain-specific code


Can I use my own favorite packages with EarthML tools and examples?
===================================================================

Of course! You may have different goals, be working on different tasks, or simply have a different preference, and you are welcome to subsitute any library you prefer for any stage in the workflow. You just need to make sure that that library is compatible with the others in the EarthML environment and that you translate data to and from appropriate formats for each tool.


How can I adapt an EarthML example to my own purposes?
======================================================

Once you have the example running in the ``earthml`` environment, you can look through the notebook to see which libraries it's actually using out of that environment, and make your own `environment.yml` containing just those packages.  Once that reduced environment works for the example, you can then add any other packages you like to solve whatever problem you are working on.


What is *not* covered well by EarthML?
======================================

- EarthML has no opinion about which tools or algorithms you use with your data -- we show you how to get your data ready for ML and how to visualize and analyze the results, but what you do in the middle is entirely up to you!
- EarthML does not currently include any 3D plotting support, though we have `prototyped <https://anaconda.org/philippjfr/cesiumjs_backend>`_ some 3D support using `CesiumJS. <https://cesiumjs.org>`_
- It would be great to have more examples, both for using other ML libraries and for domain-specific tasks; contributions welcome!


How do I report a problem?
==========================

For the quickest response from those who can fix things, try to identify which package is most directly involved, and then file a GitHub issue on the site for that project (see `PyViz.org <http://pyviz.org>`_ for links to many of them).  If you can't figure out which project is involved, or if your issue is with this website or the notebooks you downloaded from it, then please open an issue on `github.com/pyviz-topics/EarthML <https://github.com/pyviz-topics/EarthML/issues>`_ or chat with us on the `PyViz Gitter channel. <http://gitter.im/pyviz/pyviz>`_
