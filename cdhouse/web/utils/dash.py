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
                  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                  <link rel="apple-touch-icon" sizes="180x180" href="http://crazygit.wiseturtles.com/images/favicon-32x32-next.png?v=5.1.4">
                  <link rel="icon" type="image/png" sizes="32x32" href="http://crazygit.wiseturtles.com/images/favicon-32x32-next.png?v=5.1.4">
                  <link rel="icon" type="image/png" sizes="16x16" href="http://crazygit.wiseturtles.com/images/favicon-16x16-next.png?v=5.1.4">
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
                  </footer>
              </body>
          </html>
          '''.format(title, css, config, scripts)
