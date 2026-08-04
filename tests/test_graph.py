from pprint import pprint

from app.profiling.profiler import DataProfiler
from app.analytics.sales_analytics import SalesAnalytics
from app.graph.graph import graph


profiler = DataProfiler()
profile = profiler.profile("staging_transactions")

analytics = SalesAnalytics()
sales_analytics = analytics.analyze()

state = {
    "profile": profile,
    "analytics": sales_analytics
}

result = graph.invoke(state)

pprint(result)