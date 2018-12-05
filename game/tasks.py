import logging

from django.utils import timezone
from celery.schedules import crontab
from django.db.models import F

from taveuni.celery import app
from game.models import Crop

logger = logging.getLogger(__name__)


@app.task(name='check_crop_age')
def check_crops_age():
    logger.info(f'Check crops age...')

    Crop.objects.filter(
        status__in=[Crop.GROWING, Crop.RIPENING]
    ).update(
        age=F('age')+F('growing_speed')*5
    )

    Crop.objects.filter(
        status=Crop.GROWING,
        age__gt=F('ripening_age')
    ).update(
        status=Crop.RIPENING
    )



@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # # every 120 sec
    # sender.add_periodic_task(120.0,
    #                          load_schedule.s(),
    #                          queue='periodic_queue',
    #                          name='load schedule in cache every 15sec')
    #
    # # every 5 sec
    # sender.add_periodic_task(close_schedule_crontab,
    #                          close_schedule.s(),
    #                          queue='periodic_queue',
    #                          name='check close schedule every 5sec')
    #
    # # every 30 sec
    # sender.add_periodic_task(load_abnormal_schedules_crontab,
    #                          load_abnormal_schedules.s(),
    #                          queue='periodic_queue',
    #                          name='load abnormal schedules')
    #
    # # every 60 sec
    # sender.add_periodic_task(60.0,
    #                          check_holiday.s(),
    #                          queue='periodic_queue',
    #                          name='check holiday schedule every 60sec')
    #
    # # every 12am.
    # sender.add_periodic_task(crontab(hour=0, minute=0),
    #                          load_daily_schedules_count.s(),
    #                          queue='schedules',
    #                          name='calculate daily schedules count for games')
    #
    # # every 5am.
    # sender.add_periodic_task(crontab(hour=5, minute=0),
    #                          create_game_schedule.s(),
    #                          queue='schedules',
    #                          name='creates game schedules for today')

    # every 5 sec.
    sender.add_periodic_task(5.0,
                             check_crops_age.s(),
                             queue='schedules',
                             name='check all crops age every 5 seconds')

