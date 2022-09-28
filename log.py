from datetime import datetime


def write_log(query, q_type):
    if q_type == "POST":
        log_file("Writing data in datebase", query)
    elif q_type == "GET":
        log_file("Getting data from database", query)


def log_file(text, query):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"{text} {datetime.now()}: {query}\n")
