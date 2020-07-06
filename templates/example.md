{% from "base.jinja" import schema_table, random_variables, list_files %}

# {{ page.title }}

{{page.docs.synopsis}}

{{page.docs.statement}}

{% if not page.docs.rv %}
The following parameters are defined in the **RV** tab of quoFEM:
{% else %}
{{ page.docs.rv }}
{% endif %}
{{ random_variables(page.rvars) }}

## UQ Workflow

{% if not page.docs.uq %}
To define the uncertainty workflow in quoFEM, select **{{ page.input.UQ_Method.uqType }}** for the **Dakota Method Category**, and enter the following inputs:
{% else %}
{{ page.docs.uq }}
{% endif %}
{{ schema_table(page,"UQ_Method") }}

## Model Files

{% if not page.docs.fem %}
The following files make up the **FEM** model definition.
{% else %}
{{ page.docs.fem }}
{% endif %}
{{ list_files(page) }}

## Results

{{ page.docs.results }}
