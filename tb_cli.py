import argparse
from datetime import datetime, date, timedelta

def init_cli():
    parser = argparse.ArgumentParser(description='View your MiBand data analytics from Gadgetbridge database in yor terminal')
    parser.add_argument('-d', nargs=1, type=str, help='Select device')
    parser.add_argument('-info', action="store_true", help='Show device info')
    parser.add_argument('--steps', type=lambda d: datetime.strptime(d, '%Y-%m-%d'), nargs=2,
                        help='Get steps [from_date] [to_date] optionals to acquire data')
    parser.add_argument('--sleep', action="store_true", help='Show sleep data')
    parser.add_argument('--histogram', action="store_true", help='Show histogram representation')
    parser.add_argument('-date', type=lambda d: datetime.strptime(d, '%Y-%m-%d'), nargs=2, help='[from_date] [to_date] to acquire data')

    args = vars(parser.parse_args())

    return args
