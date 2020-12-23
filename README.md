A simple Django application I built as the website for my wedding.


We used the website to ...


Collect RSVPs via a form, send confirmation text messages via Plivo.

![rsvp screenshot](https://github.com/vicgarcia/getmarried/raw/master/screenshots/top-screenshot.png)


Displayed a Mapbox widget to show the venue location, local hotels, and public transit.

![mapbox widget](https://github.com/vicgarcia/getmarried/raw/master/screenshots/middle-screenshot.png)


Integrated with Stripe to accept cash gifts via credit card.

![stripe form](https://github.com/vicgarcia/getmarried/raw/master/screenshots/bottom-screenshot.png)


The site is no longer live, but the application can be run locally using Docker.

```bash
# clone the repository
git clone git@github.com:vicgarcia/getmarried.git

# start docker
docker-composer up --build

# visit the dev site
# http://127.0.0.1:8000

# create a superuser account
./docker/django/manage.sh createsuperuser

# visit the admin and log in
# http://127.0.0.1:8000/admin/
```
