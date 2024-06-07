import datetime as dt
import os

DST_COUNTRY_IATA = ["GB", "AT", "US", "US", "AL",
                    "BA", "BG", "HR", "CZ", "DK",
                    "EE", "FI", "FR", "DE", "GR",
                    "HU", "IE", "IT", "LU", "MT",
                    "NL", "NO", "PL", "PT", "RO",
                    "SK", "SI", "ES", "SE", "CH",
                    "JP", "CA", "BE"]

TEQ_DFSEARCH_API_KEY = os.environ.get("TEQ_API_KEY")

TEQ_DFSEARCH_QUERY_ENDPOINT = "v2/search"
TEQ_LOCATION_QUERY_ENDPOINT = "locations/query"
TEQ_BASE_URL = "https://api.tequila.kiwi.com/"

TEQ_LOCATION_QUERY_URL = TEQ_BASE_URL + TEQ_LOCATION_QUERY_ENDPOINT
TEQ_DIRECT_FLIGHT_QUERY_URL = TEQ_BASE_URL + TEQ_DFSEARCH_QUERY_ENDPOINT

TEQ_DF_HEADER = {
    "apikey": TEQ_DFSEARCH_API_KEY
}

MIN_NIGHTS_IN_DST = "3"
MAX_NIGHTS_IN_DST = "14"
RET_FROM_DIFF_CITY = "false"
RET_TO_DIFF_CITY = "false"
NUM_ADULTS = "1"
NUM_CHILDREN = "0"
NUM_INFANTS = "0"
MAX_STOPOVERS = "0"
CABIN_CLASS = "M"
RESULTS_LIMIT = "1000"
FIND_CHEAPEST_FLIGHT_PER_DST = "1"
DEPARTURE_CITY_IATA = "IST"
FLIGHT_SEARCH_TIME_RANGE = 180
DEPARTURE_START = (dt.date.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
DEPARTURE_END = (dt.date.today() + dt.timedelta(days=FLIGHT_SEARCH_TIME_RANGE)).strftime("%d/%m/%Y")

TEQ_DF_PARAMS = {
    "fly_from": DEPARTURE_CITY_IATA,
    "fly_to": None,
    "date_from": DEPARTURE_START,
    "date_to": DEPARTURE_END,
    "one_for_city": FIND_CHEAPEST_FLIGHT_PER_DST,
    "nights_in_dst_from": MIN_NIGHTS_IN_DST,
    "nights_in_dst_to": MAX_NIGHTS_IN_DST,
    "return_from_diff_city": RET_FROM_DIFF_CITY,
    "return_to_diff_city": RET_TO_DIFF_CITY,
    "adults": NUM_ADULTS,
    "children": NUM_CHILDREN,
    "infants": NUM_INFANTS,
    "selected_cabins": CABIN_CLASS,
    "max_stopovers": MAX_STOPOVERS,
    "limit": RESULTS_LIMIT
}

