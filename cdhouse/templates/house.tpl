{%- if new_items | length != 0 -%}
🎉【新开楼盘】🎉
{% for item in new_items %}
区域: {{ item.region }}
项目名称: {{ item.community_name }}
预售范围: {{ item.sell_range}}
住房套数: {{ item.houses }}
开发商咨询电话: {{ item.tel }}
登记开始时间: {{ item.start_time }}
登记结束时间: {{ item.end_time }}
项目报名状态: {{ item.status }}
{% endfor %}
{% endif %}

{%- if update_items | length != 0 -%}
❗️【信息更新的楼盘】❗️
{% for item in update_items %}
区域: {{ item.region }}
项目名称: {{ item.community_name }}
预售范围: {{ item.sell_range}}
住房套数: {{ item.houses }}
开发商咨询电话: {{ item.tel }}
登记开始时间: {{ item.start_time }}
登记结束时间: {{ item.end_time }}
项目报名状态: {{ item.status }}
{% endfor %}
{% endif %}
【数据更新于: {{ update_time }}】