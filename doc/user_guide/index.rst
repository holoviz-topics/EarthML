**********
User Guide
**********

Most of the functionality developed in the EarthML project is in the
various general-purpose open-source Python packages like `Bokeh
<http://bokeh.pydata.org>`_, `HoloViews <http://holoviews.org>`_, and
`Datashader <http://datashader.org>`_:


* `Introduction and Workflow <01_Introduction_and_Workflow.html>`_: Overview of the recommended workflow.

* `Data Ingestion with Intake] <02_Data_Ingestion_with_Intake.html>`_: Loading large data sets efficiently with `intake <https://github.com/ContinuumIO/intake>`_.

* `Alignment and Preprocessing <03_Alignment_and_Preprocessing.html>`_: How to prepare your data for the machine learning pipeline.

* `Machine Learning <04_Machine_Learning.html>`_: Specifying a `scikit-learn <http://scikit-learn.org/stable/index.html>`_ pipeline to ingest the prepared training data.

* `Data Visualization <05_Data_Visualization.html>`_: How to visualize your data throughout the workflow, starting from data ingestion to the final machine learning product.


.. toctree::
    :titlesonly:
    :hidden:
    :maxdepth: 2
               
    Introduction and Workflow <01_Introduction_and_Workflow>
    Data Ingestion with Intake <02_Data_Ingestion_with_Intake>
    Alignment and Preprocessing <03_Alignment_and_Preprocessing>
    Machine Learning <04_Machine_Learning>
    Data Visualization <05_Data_Visualization>
