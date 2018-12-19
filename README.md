A simple Django application I built to power the website for my wedding.

We used the website to ...

Collect RSVPs via a form on the website.
Integrated with Plivo to send text messages to confirm RSVP.
Displayed a Mapbox widget to show the venue location, local hotels, and public transit.
Integrated with Stripe to accept monetary gifts via credit card form on the site.


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
