import smtplib
import string

class NotificationManager:

    @staticmethod
    def format_flight_string(flight_info):
        dep_date, dep_hour = flight_info["dep_date"].split('T')[0], flight_info["dep_date"].split('T')[1].split('.')[0]
        ret_date, ret_hour = flight_info["ret_date"].split('T')[0], flight_info["ret_date"].split('T')[1].split('.')[0]
        content = f"""Subject:Your chance to visit {flight_info['dst_city']}, {flight_info['dst_country']} only for {flight_info['price(EUR)']}EUR!\n\n
                *****
                Departure => From {flight_info['org_airport']}, {flight_info['org_city']}, {flight_info['org_country']} to {flight_info['dst_airport']}, {flight_info['dst_city']}, {flight_info['dst_country']}
                at {dep_date} {dep_hour} UTC with {flight_info['dep_airline']} flight no {flight_info['dep_flight_no']}!
                *****
                Return => From {flight_info['ret_airport_from']}, {flight_info['ret_city_from']} to {flight_info['ret_airport_to']}, {flight_info['ret_city_to']}
                at {ret_date} {ret_hour} UTC with {flight_info['ret_airline']} airlines flight no {flight_info['ret_flight_no']}!
                *****
                Link For Tickets : {flight_info['link']}
                """
        return ''.join(filter(lambda x: x in string.printable, content))

    @staticmethod
    def send_mails_to_users(smtp_addr, smtp_access, smtp_sender, user_mails, cheaper_flights):
        with smtplib.SMTP(smtp_addr) as connection:
            connection.starttls()
            connection.login(user=smtp_sender, password=smtp_access)
            for cheap_flight in cheaper_flights:
                for user_mail in user_mails:
                    connection.sendmail(from_addr=smtp_sender,
                                        to_addrs=user_mail,
                                        msg=NotificationManager.format_flight_string(cheap_flight.info))