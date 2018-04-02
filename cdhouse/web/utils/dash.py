# -*- coding: utf-8 -*-
from dash import Dash


class CustomDash(Dash):

    def index(self, *args, **kwargs):  # pylint: disable=unused-argument
        scripts = self._generate_scripts_html()
        css = self._generate_css_dist_html()
        config = self._generate_config_html()
        title = getattr(self, 'title', 'Dash')
        return '''
          <!DOCTYPE html>
          <html>
              <head>
                  <meta charset="UTF-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <link rel="apple-touch-icon" sizes="180x180" href="//crazygit.wiseturtles.com/images/favicon-32x32-next.png?v=5.1.4">
                  <link rel="icon" type="image/png" sizes="32x32" href="//crazygit.wiseturtles.com/images/favicon-32x32-next.png?v=5.1.4">
                  <link rel="icon" type="image/png" sizes="16x16" href="//crazygit.wiseturtles.com/images/favicon-16x16-next.png?v=5.1.4">
                  <meta name="keywords" content="crazygit,成都房协,房源,摇号,统计" />
                  <title>{}</title>
                  {}
              </head>
              <body>
                  <div id="react-entry-point">
                      <div class="_dash-loading">
                          Loading...
                      </div>
                  </div>
                  <footer>
                      {}
                      {}
                      <script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>

<!--PC和WAP自适应版-->
<div id="SOHUCS" sid="cd-house" ></div>
<script type="text/javascript">
(function(){{
var appid = 'cytxOsaQx';
var conf = 'prod_533636c75500e09df7b5d8181bf4e901';
var width = window.innerWidth || document.documentElement.clientWidth;
if (width < 960) {{
window.document.write('<script id="changyan_mobile_js" charset="utf-8" type="text/javascript" src="https://changyan.sohu.com/upload/mobile/wap-js/changyan_mobile.js?client_id=' + appid + '&conf=' + conf + '"><\/script>'); }} else {{ var loadJs=function(d,a){{var c=document.getElementsByTagName("head")[0]||document.head||document.documentElement;var b=document.createElement("script");b.setAttribute("type","text/javascript");b.setAttribute("charset","UTF-8");b.setAttribute("src",d);if(typeof a==="function"){{if(window.attachEvent){{b.onreadystatechange=function(){{var e=b.readyState;if(e==="loaded"||e==="complete"){{b.onreadystatechange=null;a()}}}}}}else{{b.onload=a}}}}c.appendChild(b)}};loadJs("https://changyan.sohu.com/upload/changyan.js",function(){{window.changyan.api.config({{appid:appid,conf:conf}})}}); }} }})(); </script>

                  </footer>
              </body>
          </html>
          '''.format(title, css, config, scripts)
