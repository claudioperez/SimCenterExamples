---
page_template: vega.html
...
:page_template: vega.html

{% from "base.jinja" import schema_table, random_variables, list_files, vega_plot %}

# {{ page.title }}

|  |  |
|----------|------|
| Problem files | [{{page.id}}](https://github.com/claudioperez/SimCenterDocumentation/tree/examples/docs/common/user_manual/examples/desktop/quoFEM/src/{{page.id}}) |

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
<!-- <div class="admonition warning">Do not place the files in your root, downloads, or desktop folder as when the application runs it will copy the contents on the directories and subdirectories containing these files multiple times. If you are like us, your root, Downloads or Documents folders contains and awful lot of files and when the backend workflow runs you will slowly find you will run out of disk space!</div> -->

## Results

{{ page.docs.results }}
{{ vega_plot(page) }}
