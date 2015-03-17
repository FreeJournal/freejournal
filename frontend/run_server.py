from webapp import app, celery
import config

celery = celery  # Give `celery` variable to pass to celery

if __name__ == '__main__':
    app.debug = config.WEB_DEBUG
    app.run()
