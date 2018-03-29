{# 新开楼盘和信息更新的楼盘使用的模板 #}
{% import 'macros.tpl' as macros %}
{% if new_items | length != 0 %}
🎉【新开楼盘】🎉
{% for item in new_items %}
{{ macros.render_project(item) }}
{% endfor %}
{% endif %}
{% if update_items | length != 0 %}
❗️【信息更新的楼盘】❗️
{% for item in update_items %}
{{ macros.render_project(item) }}
{% endfor %}
{% endif %}

【数据更新于: {{ update_time }}】