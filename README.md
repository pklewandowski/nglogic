# NGLOGIC API RECRUITMENT TASK

## Overview

This application allow users to query API endpoint to get index of specified value.
the endpoint structure is like

`/nlogic/r'-?\d+'/`

So we can, for example, get the result by entering url:
`localhost:8000/nlogic/200/` or `localhost:8000/nlogic/-15/`
assuming the application is running on localhost and 8000 port (common for Django apps dev server)
We can enter values netween `datasource.MIN_VALUE - MIN_MAX_TREHSHOLD` and  
`datasource.MAX_VALUE + MIN_MAX_TREHSHOLD`
The example app data is loaded from input.txt  (for tests the file is test_input.txt and contains only 10,000 records), conaining 100,000 records from 0 to 1,000,000,
so the minimum acceptable value is <-25,1000025> as the `MIN_MAX_TREHSHOLD` is set to 25.
When value is outside the allowed range, the HTTP 422 Unprocessable Entity will be returned as following:

```shell
HTTP 422 Unprocessable Entity
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "idx": null,
    "value": 99999999,
    "message": "Value 99999999 is too hi. Maximum value is 1000025"
}
```

If entered value does not exist in the dataset, the nearest value index is returned with appropriate comment:

```shell
http://localhost:8000/nglogic/1234/

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "idx": 12,
    "value": 1234,
    "message": "Value was not found in datasource. Nearest index returned"
}
```

This is not quite as it was described in the task requirements, but I'm affraid I could misunderstand the "10% level"
criteria,
so did it the above way.
Application uses Django Rest Framework with it's basic benefits (like ie. serializers), even if it might seem to not
exactly needed for this particular example purposes. It's for highlight the skills etc.

Makefile is created in the root of the app. 
It has few entries like pytest, format or clean. With `make clean` you can remove any compield files (`.pyc`)
etc.

In `utils` dir there are defined url converter and decorator for API views
In `settings` there is also logging config defined (LOGGING).

As a data structure I've choosen instead of `list` (as suggested in project recruitment_task.md file), the `dict`
as it's a hashmap, ideally fitting to this functionality.
Additionally (for optimization), I've added to the data model object `NglogicApiDataModel` 
a list of keys and MIN_VALUE and MAX_VALUE.
It's initialized in `apps.NglogicApiConfig:ready()` method so it's ran on startup

## Build

App can be dockerized. Build script `build_app.sh` as well as Dockerfile and docker-compose.yml
are located under the root dir