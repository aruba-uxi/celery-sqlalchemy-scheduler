from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from uxi_celery_scheduler.data_models import ScheduledTask
from uxi_celery_scheduler.db.models import CrontabSchedule, PeriodicTask
from uxi_celery_scheduler.exceptions import PeriodicTaskNotFound


def schedule_task(
    session: Session,
    scheduled_task: ScheduledTask,
) -> PeriodicTask:
    """
    Schedule a task by adding a periodic task entry.
    """
    schedule = CrontabSchedule(**scheduled_task.schedule.dict())
    task = PeriodicTask(
        crontab=schedule,
        name=scheduled_task.name,
        task=scheduled_task.task,
    )
    session.add(task)

    return task


def update_task_enable_status(
    session: Session,
    enable_status: bool,
    periodic_task_id: int,
) -> PeriodicTask:
    """
    Update task enable status (if task is enabled or disabled).
    """
    try:
        task = session.query(PeriodicTask).get(periodic_task_id)
        task.enabled = enable_status
        session.add(task)

    except NoResultFound as e:
        raise PeriodicTaskNotFound from e

    return task


def update_period_task(
    session: Session,
    scheduled_task: ScheduledTask,
    periodic_task_id: int,
) -> PeriodicTask:
    """
    Update the details of a task including the crontab schedule
    """
    try:
        task = session.query(PeriodicTask).get(periodic_task_id)

        schedule = CrontabSchedule(**scheduled_task.schedule.dict())
        task.crontab = schedule
        task.name = scheduled_task.name
        task.task = scheduled_task.task
        session.add(task)

    except NoResultFound as e:
        raise PeriodicTaskNotFound from e

    return task


def delete_task(session: Session, periodic_task_id: int) -> PeriodicTask:
    try:
        task = session.query(PeriodicTask).get(periodic_task_id)
        session.delete(task)
        return task
    except NoResultFound:
        raise NoResultFound()
