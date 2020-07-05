{% for Prop in schema.UQ_Method.additionalProperties %}
   {% if Prop in page.input.UQ_Method %}
      {% for prop in schema.UQ_Method.additionalProperties %}
* **{{ Prop.title }}**: {{ prop.value }}


      {% endfor %}
   {% endif %}
{% endfor %}