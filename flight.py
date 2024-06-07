class Flight:
    def __init__(self, flight_info):
        self.info = {
            "org_airport": flight_info["flyFrom"],
            "dst_airport": flight_info["flyTo"],
            "ret_airport_from": flight_info["route"][1]["flyFrom"],
            "ret_airport_to": flight_info["route"][1]["flyTo"],

            "org_city": flight_info["cityFrom"],
            "dst_city": flight_info["cityTo"],
            "ret_city_from": flight_info["route"][1]["cityFrom"],
            "ret_city_to": flight_info["route"][1]["cityTo"],

            "org_country": flight_info["countryFrom"]["name"],
            "dst_country": flight_info["countryTo"]["name"],

            "price(EUR)": flight_info["price"],

            "dep_date": flight_info["route"][0]["utc_departure"],
            "ret_date": flight_info["route"][1]["utc_departure"],

            "dep_airline": flight_info["route"][0]["airline"],
            "ret_airline": flight_info["route"][1]["airline"],

            "dep_flight_no": flight_info["route"][0]["flight_no"],
            "ret_flight_no": flight_info["route"][1]["flight_no"],

            "link": flight_info["deep_link"],
        }