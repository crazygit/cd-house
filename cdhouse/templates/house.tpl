{%- if new_items | length != 0 %}
    :tada::tada::tada:新开楼盘
    {% for item in new_items -%}
        {{ item.region }}  {{ item.community_name }}  {{ item.sell_range}}  {{ item.houses }}  {{ item.start_time }}  {{ item.end_time }}  {{ item.status }}
    {% endfor %}
{% endif %}

{%- if update_items | length != 0 %}
    信息更新的楼盘:
    {% for item in update_items -%}
        {{ item.region }}  {{ item.community_name }}  {{ item.sell_range}}  {{ item.houses }}  {{ item.start_time }}  {{ item.end_time }}  {{ item.status }}
    {% endfor %}
{% endif %}



