# -*- coding: utf-8 -*-
from scrapy.commands.crawl import Command as ExistingCrawlCommand
from scrapy.exceptions import UsageError


class Command(ExistingCrawlCommand):
    """custom crawl command with exit code"""

    def run(self, args, opts):
        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError(
                "running 'scrapy crawl' with more than one spider is no longer supported"
            )
        spname = args[0]

        crawler = self.crawler_process.create_crawler(spname)
        self.crawler_process.crawl(crawler, **opts.spargs)
        self.crawler_process.start()
        exception_count = crawler.stats.get_value('log_count/ERROR')
        if exception_count:
            self.exitcode = 1
