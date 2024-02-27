import datetime


class DateFormat():

    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
    @classmethod
    def convert_date_to_API(self, date):
        return datetime.datetime.strftime(date, '%Y-%m-%d')
    @classmethod
    def convert_hour(self, hour):
        return datetime.time.strftime(hour, '%H:%M')
    @classmethod
    def convert_hour_to_API(self, hour):
        return datetime.time.strftime(hour, '%H:%M:00.000')
    @classmethod
    def convert_str_date(self, str_date):
        return datetime.datetime.strptime(str_date, '%d/%m/%Y %H:%M')
