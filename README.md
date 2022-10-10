# Hotel-Booking-Demand

## Deploy

1. Build docker image from Dockerfile

    ```docker build -t "<app name>" -f Dockerfile .```

2. Run the docker container after build
    ```docker run -p 9999:9999 <app name>```

3. Show all running containers
    
    ```docker ps```

4. Kill and remove running container
    
     ```docker rm <containerid> -f ```


## Endpoints

### /predict (POST)

Returns an output of prediction given a JSON object representing variables. Here's a sample input:

    ```
    [
        {"hotel": 0, "lead_time": 131, "arrival_date_year": 2017, "arrival_date_month": 7, "arrival_date_week_number": 27, "arrival_date_day_of_month": 6, "stays_in_weekend_nights": 1, "stays_in_week_nights": 3, "adults": 2, "country": 135, "market_segment": 6, "distribution_channel": 3, "is_repeated_guest": 0, "previous_cancellations": 0, "previous_bookings_not_canceled": 0, "booking_changes": 0, "deposit_type": 0, "agent": 9.0, "company": 40.0, "days_in_waiting_list": 0,"customer_type": 2, "adr": 89.1,"required_car_parking_spaces": 0,"total_of_special_requests": 0, "has_children": "0", "total_bookings": 0, "same_room": 1}
    ]
    ```
