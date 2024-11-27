from transit.models import StopTimes

def query_stop_times():
    results = StopTimes.objects.select_related('stop', 'trip__route').values(
        'stop__stop_name', 
        'arrival_time', 
        'departure_time', 
        'trip__route__route_long_name', 
        'trip__trip_id'
    )

    for result in results:
        print(
            f"Route: {result['trip__route__route_long_name']} | "
            f"Trip ID: {result['trip__trip_id']} | "
            f"Stop: {result['stop__stop_name']} | "
            f"Arrival: {result['arrival_time']} | "
            f"Departure: {result['departure_time']}"
        )
