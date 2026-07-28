from pprint import pprint

from app.profiling.profiler import DataProfiler

profiler = DataProfiler()

report = profiler.profile()

pprint(report)