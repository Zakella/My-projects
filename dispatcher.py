import db_management


def write_data_in_db(data):
    db_management.write_data(data)


def read_data_from_db(data):
    db_management.find_data(data)

