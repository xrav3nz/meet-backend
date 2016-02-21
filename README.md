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
            "web_url": "https://www.tripadvisor.ca/Restaurant_Review-g154945-d6280714-Reviews-Boardgame_Cafe-Victoria_Victoria_Capital_Regional_District_Vancouver_Island_Briti.html",
            "name": "Board Game Cafe"
        },
        ...
    ],
    "restaurants": [
        {
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d3398229-Reviews-m11068-Wan_Convenience_Store-Boston_Massachusetts.html",
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
            "web_url": "https://www.tripadvisor.ca/Restaurant_Review-g154945-d6280714-Reviews-Boardgame_Cafe-Victoria_Victoria_Capital_Regional_District_Vancouver_Island_Briti.html",
            "name": "Board Game Cafe",
            "votes": "0"
        },
        ...
    ],
    "restaurants": [
        {
            "id", "1",
            "web_url": "http://www.tripadvisor.com/Restaurant_Review-g60745-d3398229-Reviews-m11068-Wan_Convenience_Store-Boston_Massachusetts.html",
            "name": "Amy's Cafe",
            "votes": "3"
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
    "activity_ids": [
        1,
        ...
    ]
}
```

## Response 
```
{
    "timeslots": [
        {
            "id": "1",
            "votes": "2"
        }, 
        ...
    ],
    "activities": [
        {
            "id", "1",
            "votes": "0"
        },
        ...
    ]
}
```



# GET /restaurants/\<string:latitude\>,\<string:longtitude\>

> Search for restaurants at the given coordinate
 
## Parameters
**`count`** *optional*  
> Default: 5, number of results to return  

## Request
```
/restaurants/42.33141,-71.099396?count=5
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


# GET /attractions/\<string:latitude\>,\<string:longtitude\>

> Search for restaurants at the given coordinate
 
## Parameters
**`count`** *optional*  
> Default: 5, number of results to return  

## Request
```
/attractions/42.33141,-71.099396?count=5
```

## Response 
```
{
    "results": [
        {
            "name": "Diablo Glass School",
            "web_url": "http://www.tripadvisor.com/Attraction_Review-g60745-d3546275-Reviews-m11068-Diablo_Glass_School-Boston_Massachusetts.html"
        },
        {
            "name": "The Squealing Pig Boston",
            "web_url": "http://www.tripadvisor.com/Attraction_Review-g60745-d5831233-Reviews-m11068-The_Squealing_Pig_Boston-Boston_Massachusetts.html"
        },
        {
            "name": "Warren Anatomical Museum",
            "web_url": "http://www.tripadvisor.com/Attraction_Review-g60745-d7224158-Reviews-m11068-Warren_Anatomical_Museum-Boston_Massachusetts.html"
        },
        {
            "name": "Penguin Pizza",
            "web_url": "http://www.tripadvisor.com/Attraction_Review-g60745-d5845923-Reviews-m11068-Penguin_Pizza-Boston_Massachusetts.html"
        },
        {
            "name": "Mission Bar & Grill",
            "web_url": "http://www.tripadvisor.com/Attraction_Review-g60745-d5842367-Reviews-m11068-Mission_Bar_Grill-Boston_Massachusetts.html"
        }
    ]
}
```