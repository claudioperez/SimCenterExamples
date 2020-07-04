{% macro sentence_case(text) %}{{ text[0]|upper}}{{text[1:]}}{% endmacro %}


{{ page.title }}
============================================================

{{page.docs.synopsis}}
{{page.docs.statement}}

.. figure:: {{ page.docs.model_fig }}
   :align: center
   :width: 600
   :figclass: align-center

The following problem variables are modeled as uncertain parameters:

{% for rvar in page.rvars -%}
#. {{ sentence_case(rvar.title) }}, ``{{ rvar.name }}``: {{ rvar.distribution }} distribution with a {% for param in rvar.params %} {{ param.title }} :math:`({{ param.tex }})` of {{ param.value }}, {% endfor %}.

{% endfor %}

{% if page.docs.workflow %}
Problem Workflow
^^^^^^^^^^^^^^^^

{% endif %}


Model Definition
^^^^^^^^^^^^^^^^

{% if page.files %}
The following input files must be placed in an *empty* folder:

{% for file in page.files -%}

#. ``{{ file.loc }}``: {{ file.description }}

{% endfor %}
{% endif %}


.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

{{ page.docs.results }}

