{% macro sentence_case(text) %}{{ text[0]|upper}}{{text[1:]}}{% endmacro %}

{% macro random_variables(obj_list) %}  
{% for rvar in obj_list -%}
#. {{ sentence_case(rvar.title) }}, ``{{ rvar.name }}``: **{{ rvar.distribution }}** distribution with a {% for param in rvar.params %} {{ param.title }} :math:`({{ param.tex }})` of {{ param.value }}, {% endfor %}

{% endfor %}
{% endmacro %}

{{ page.title }}
============================================================

{{page.docs.synopsis}}
{{page.docs.statement}}


{{ random_variables(page.rvars) }}

.. 
   .. figure:: {{ page.docs.model_fig }}
      :align: center
      :width: 600
      :figclass: align-center


{% if page.docs.workflow %}
Problem Workflow
^^^^^^^^^^^^^^^^

The workflow is defined in the **UQ** tab using the {{ page.input.UQ_Method.uqEngine }} UQ engine as follows:

{{ page.docs.workflow }}


{% endif %}


Model Definition
^^^^^^^^^^^^^^^^

{% if page.files %}
The following input files define the FE model and are supplied at the **FEM** tab using the **{{ page.input.fem.program }}** workflow option. They must be placed in an *empty* folder:

{% for file in page.files -%}

#. ``{{ file.loc }}``: {{ file.description }}

{% endfor %}
{% endif %}


.. warning::

   Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!


Results
^^^^^^^^^^^^^^^

{{ page.docs.results }}

