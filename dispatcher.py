import db_management


def write_data_in_db(data):
    db_management.create_table()
    print(data)


def read_data_from_db(data):
    print(data)
