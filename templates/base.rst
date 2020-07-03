{{ page.title }}
============================================================

{{page.docs.synopsis}}
{{page.docs.statement}}

.. figure:: {{ page.docs.model_fig }}
   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:

{% for rvar in page.input.randomVariables -%}
#. ``{{ rvar.name }}``

{% endfor %}

Problem Workflow
^^^^^^^^^^^^^^^^

Workflow

Model Definition
^^^^^^^^^^^^^^^^

The following input files must be placed in an *empty* folder:

{% if page.files %}
{% for file in page.files -%}

#. ``{{ file.loc }}``: {{ file.description }}

{% endfor %}
{% endif %}


.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

If the user selects **Data** in the **RES** tab, they will be presented with both a graphical plot and a tabular listing of the data.

.. figure:: figures/trussRES2.png
   :align: center
   :figclass: align-center

{{ page.docs.results }}

.. figure:: {{ page.docs.res_fig }}
   :align: center
   :figclass: align-center
