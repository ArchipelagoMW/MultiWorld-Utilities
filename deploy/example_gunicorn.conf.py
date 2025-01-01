import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = "WebHost:get_app()"
accesslog = "-"
access_log_format = (
    '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
)
worker_class = "sync"  # "sync" | eventlet" | "gevent" | "tornado"
forwarded_allow_ips = "*"
loglevel = "debug"
