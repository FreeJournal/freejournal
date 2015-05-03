from async import repeat_periodic, wait_for_interrupt


@repeat_periodic(1)
def job_thread():
    print "hello repeatable world"


def exit_func():
    print ""
    print "you ctrl+c'd, now exiting"

wait_for_interrupt(exit_func, job_thread())
