from datetime import datetime, timedelta
import msg 
import pytz
import csv

from redis import Redis
from rq import Queue

queue = Queue(connection=Redis())

contacts_file = open('samplecontacts.csv')
csv_file = csv.reader(contacts_file)

def get_next_contact():
    next_scheduled_time = datetime.now()
    delta = 0
    for row in csv_file:
        recipient_number = row[8]
        queue.enqueue_in(timedelta(seconds=delta), msg.send_text_message,
                                '+19145296977', recipient_number,
                                'Hello this is a message')
        delta += 15
        print("The next scheduled time is = ", next_scheduled_time, " for the phone #", recipient_number)

def main():
    get_next_contact()

if __name__ == "__main__":
    main()

