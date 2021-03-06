from frontend.webapp import app, celery
import config

celery = celery  # Give `celery` variable to pass to celery

if __name__ == '__main__':
    app.debug = config.WEBAPP_DEBUG
    app.run()
