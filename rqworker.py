import rollbar
from rq import Connection, Queue, Worker

from ghinbox import app


def exception_handler(job, *exc_info):
    """
    Called by RQ when there is a failure in a worker.
    NOTE: Make sure that in your RQ worker process, rollbar.init() has been called with
    handler='blocking'. The default handler, 'thread', does not work from inside an RQ worker.
    """
    # Report data about the job with the exception.
    job_info = job.to_dict()
    # job_info['data'] is the pickled representation of the job, and doesn't json-serialize well.
    # repr() works nicely.
    job_info['data'] = repr(job_info['data'])

    extra_data = {'job': job_info}
    payload_data = {'framework': 'rq'}

    rollbar.report_exc_info(exc_info, extra_data=extra_data, payload_data=payload_data)

    # continue to the next handler
    return True


if __name__ == '__main__':
    rollbar.init(app.config['ROLLBAR_ACCESS_TOKEN'], 'production', handler='blocking')
    with Connection():
        q = Queue()
        worker = Worker(q)
        worker.push_exc_handler(exception_handler)
        worker.work()
