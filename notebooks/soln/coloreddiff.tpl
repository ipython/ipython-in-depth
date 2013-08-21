{% extends 'html_full.tpl'%}

{% block any_cell %}
    {% if cell['metadata'].get('example',{}).get('difficulty','') == 'Hard' -%}
        <div style="background-color:red">
        {{ super() }}
        </div>
    {% elif  cell['metadata'].get('example',{}).get('difficulty','') == 'Medium'  %}
        <div style='background-color:orange'>
        {{ super() }}
        </div>
    {% else  %}
        {{ super() }}
    {% endif %}
{%- endblock any_cell %}