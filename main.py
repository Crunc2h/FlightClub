import os
import pandas as pd
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_search_config import (TEQ_DIRECT_FLIGHT_QUERY_URL,
                                  TEQ_DF_PARAMS,
                                  TEQ_DF_HEADER,
                                  DST_COUNTRY_IATA)


FDATA_FILE_PATH = "~/FlightClub/flights_data.csv"
UDATA_FILE_PATH = "~/FlightClub/user_data.csv"

SMTP_ADDR = "smtp.gmail.com"
SMTP_ACCESS = os.environ.get("SMTP_ACCESS")
SMTP_SENDER = os.environ.get("SMTP_SENDER")

def main():
    all_flights = FlightSearch.get_flight_data(query_url=TEQ_DIRECT_FLIGHT_QUERY_URL,
                                               query_params=TEQ_DF_PARAMS,
                                               query_header=TEQ_DF_HEADER,
                                               country_codes=DST_COUNTRY_IATA)

    with open(FDATA_FILE_PATH) as flight_data_file:
        flight_data = pd.read_csv(flight_data_file)
        flight_data, cheaper_flights = FlightSearch.update_and_find_cheap_flights(all_flights, flight_data)
        flight_data.to_csv(FDATA_FILE_PATH, mode="w", index=False)
        print(len(all_flights))
        print(len(cheaper_flights))
        if len(cheaper_flights) > 0:
            with open(UDATA_FILE_PATH) as user_data_file:
                user_mails = pd.read_csv(user_data_file)["email"]
                NotificationManager.send_mails_to_users(smtp_addr=SMTP_ADDR,
                                                        smtp_access=SMTP_ACCESS,
                                                        smtp_sender=SMTP_SENDER,
                                                        user_mails=user_mails,
                                                        cheaper_flights=cheaper_flights)

main()










