import requests
from flight import Flight


class FlightSearch:

    @staticmethod
    def get_flight_data(query_url, query_params, query_header, country_codes):
        all_flights = []

        for country_code in country_codes:
            query_params["fly_to"] = country_code
            response = requests.get(url=query_url, params=query_params, headers=query_header)
            response.raise_for_status()
            for flight_data in response.json()["data"]:
                all_flights.append(Flight(flight_data))

        return all_flights

    @staticmethod
    def compare_or_add_flight_price_infos(new_flight, flight_data_df):
        is_cheaper_flight = False

        if (flight_data_df["dst_city"] == new_flight.info["dst_city"]).any():
            target_index = flight_data_df.loc[(flight_data_df["dst_city"] 
            == new_flight.info["dst_city"])].index[0]
            if flight_data_df.iloc[target_index]["price(EUR)"] > new_flight.info["price(EUR)"]:
                flight_data_df.at[target_index, 'price(EUR)'] = new_flight.info["price(EUR)"]
                is_cheaper_flight = True
        else:
            flight_data_df.loc[len(flight_data_df)] = new_flight.info
        return flight_data_df, is_cheaper_flight

    @staticmethod
    def update_and_find_cheap_flights(all_flights, flight_price_info_df):
        cheaper_flights = []

        for flight in all_flights:
            flight_price_info_df, is_cheaper_flight = FlightSearch.compare_or_add_flight_price_infos(flight, flight_price_info_df)
            if is_cheaper_flight:
                cheaper_flights.append(flight)

        return flight_price_info_df, cheaper_flights