import os

from django.conf import settings

from winchester.settings.base import USE_TZ, TIME_ZONE

# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-routes
task_routes = None

# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-settings-celery-beat
beat_schedule = {}

if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
broker_url = os.getenv("CELERY_BROKER_URL", default="redis://localhost:6379/0")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
result_backend = broker_url
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
accept_content = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
task_serializer = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
result_serializer = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
task_time_limit = 5 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
task_soft_time_limit = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-track-started
task_track_started = True
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#worker-max-tasks-per-child
worker_max_tasks_per_child = 100  # 100 jobs before worker is replaced
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#worker-max-memory-per-child
worker_max_memory_per_child = 12000  # 12MB

if settings.debug:
    # http: // docs.celeryproject.org / en / latest / userguide / configuration.html  # worker-send-task-events
    worker_send_task_events = True

