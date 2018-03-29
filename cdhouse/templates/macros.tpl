{% macro render_project(project)%}
区域: {{ project.region }}
项目名称: {{ project.community_name }}
预售范围: {{ project.sell_range}}
住房套数: {{ project.houses }}
开发商咨询电话: {{ project.tel }}
登记开始时间: {{ project.start_time }}
登记结束时间: {{ project.end_time }}
项目报名状态: {{ project.status }}
{% endmacro %}