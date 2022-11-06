from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from Scheduler import excel_creator

def start():
    scheduler = BackgroundScheduler()
    trigger = CronTrigger(
        year="*", month="*", day="*", hour="20", minute="6", second="0"
    )
    scheduler.add_job(excel_creator.trial, trigger = trigger)
    scheduler.start()