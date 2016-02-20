# POST /meetups

> Submit a new meetup
 
## Request
```
{
    "name": "The Great Meetup",
    "organizer": "Kyle",
    "timeslots": [
        {
            "start_time": "2016-02-10 07:00:00",
            "end_time": "2016-02-10 09:00:00"
        }, 
        ...
    ],
    "activities": [
        {
            "tripadvisor_id": "123123",
            "name": "Amy's Cafe"
        },
        ...
    ]
}
```

## Response 
```
{
    "id": "9XDCS01K3",
    "password": "C018VN83N"
}
```

# GET /meetups/<string:meetup_id>

> Return the information of the specific meetup
 
## Response
```
{
    "id": "9XDCS01K3"
    "name": "The Great Meetup",
    "organizer": "Kyle",
    "timeslots": [
        {
            "start_time": "2016-02-10 07:00:00",
            "end_time": "2016-02-10 09:00:00",
            "votes": "2"
        }, 
        ...
    ],
    "activities": [
        {
            "tripadvisor_id": "123123",
            "name": "Amy's Cafe",
            "votes": "0"
        },
        ...
    ]
}
```

