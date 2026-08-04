from pprint import pprint

from app.analytics.sales_analytics import SalesAnalytics

analytics = SalesAnalytics()

report = analytics.analyze()

pprint(report)