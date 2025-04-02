from celery import Celery
from src.config import create_app 

def make_celery():
    celery = Celery(
        "backend",
        broker="redis://localhost:6379/0",  # Ensure Redis is running
        backend="redis://localhost:6379/0",
        include=["src.baground_tasks"]
    )
    celery.conf.update(app.config)
    
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
app = create_app()

celery = make_celery()

if __name__ == "__main__":
    celery.worker_main()
