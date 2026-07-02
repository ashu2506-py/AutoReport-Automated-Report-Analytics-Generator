from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()


def start_scheduler(job, interval):

    scheduler.add_job(
        job,
        "interval",
        minutes=interval
    )

    print(f"Report scheduled every {interval} minute(s).")

    scheduler.start()