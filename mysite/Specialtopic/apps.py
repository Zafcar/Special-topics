from django.apps import AppConfig


class SpecialtopicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Specialtopic'

    def ready(self):
        from Scheduler import job_scheduler
        job_scheduler.excel_service()
        job_scheduler.email_service()