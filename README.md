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

# GET /meetups/\<string:meetup_id\>

> Return the information of the specific meetup
 
## Response
```
{
    "id": "9XDCS01K3"
    "name": "The Great Meetup",
    "organizer": "Kyle",
    "timeslots": [
        {
            "id": "1",
            "start_time": "2016-02-10 07:00:00",
            "end_time": "2016-02-10 09:00:00",
            "votes": "2"
        }, 
        ...
    ],
    "activities": [
        {
            "id", "1",
            "tripadvisor_id": "123123",
            "name": "Amy's Cafe",
            "votes": "0"
        },
        ...
    ]
}
```

# PUT /meetups/\<string:meetup_id\>

> Vote for the activities and timeslots
 
## Request
```
{
    "timeslot_ids": [
        1,
        ...
    ],
    "activitiy_ids": [
        1,
        ...
    ]
}
```

## Response 
```
{
    "timeslot_ids": [
        {
            "id": "1",
            "votes": "2"
        }, 
        ...
    ],
    "activitiy_ids": [
        {
            "id", "1",
            "votes": "0"
        },
        ...
    ]
}
```



# GET /resturants/\<string:latitude\>,\<string:longtitude\>

> Search for resturants at the given coordinate
 
## Parameters
**`count`** *optional*  
> Default: 5, number of results to return  

## Request
```
/resturants/42.33141,-71.099396?count=5
```

## Response 
```
{
    "results": [
        {
            "name": "Chacho's Pizza & Subs",
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d4225110-Reviews-m11068-Chacho_s_Pizza_Subs-Boston_Massachusetts.html"
        },
        {
            "name": "Wan Convenience Store",
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d3398229-Reviews-m11068-Wan_Convenience_Store-Boston_Massachusetts.html"
        },
        {
            "name": "Crispy Dough Pizzeria",
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d4198412-Reviews-m11068-Crispy_Dough_Pizzeria-Boston_Massachusetts.html"
        },
        {
            "name": "Lilly's Gourmet Pasta Express",
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d2080094-Reviews-m11068-Lilly_s_Gourmet_Pasta_Express-Boston_Massachusetts.html"
        },
        {
            "name": "Diploma Mill",
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d5223032-Reviews-m11068-Diploma_Mill-Boston_Massachusetts.html"
        }
    ]
}
```

