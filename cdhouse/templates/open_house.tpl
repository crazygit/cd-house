{# 按区域查询楼盘信息的模板 #}
【{{ region }}】
{% import 'macros.tpl' as macros %}
{% for project in projects %}
{{ macros.render_project(project, ) }}
{% else %}
暂无预售楼盘信息
{% endfor %}