import sqlite3
from datetime import date, timedelta
import tb_graph
import tb_cli

class Device:

    def __init__(self, db_file, name):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

        self.name = name

        device_info = self.get_device_info()
        
        self.manufacturer = device_info[2]
        self.identifier = device_info[3]
        self.dtype = device_info[4]
        self.model = device_info[5]
        self.alias = device_info[6]

    def get_device_info(self):
        self.cur.execute('SELECT * FROM DEVICE')
        for row in self.cur:
            if row[1] == self.name:
                return row

class MiBand(Device):

    def get_daily_steps_date(self, from_date=date.today()-timedelta(7), to_date=date.today()):
        self.cur.execute('''
            SELECT 
	            date(TIMESTAMP, "unixepoch"), 
	            sum(STEPS) 
            FROM 
	            MI_BAND_ACTIVITY_SAMPLE 
            WHERE 
	            date(TIMESTAMP, 'unixepoch') BETWEEN '{dfrom}' AND '{to}'
            GROUP BY
	            date(TIMESTAMP, 'unixepoch')'''.format(dfrom=from_date, to=to_date))
        days_dict = {}
        for row in self.cur:
            days_dict[row[0]] = row[1]
        return days_dict


cli = tb_cli.init_cli()

#Device selection to fetch data
if "Mi Band 3" in cli["d"]:
    device = MiBand("miband", "Mi Band 3")
    if cli["info"]:
        print("Device: "+str(device.name))
        print("Manufacturer: "+str(device.manufacturer))
        print("Identifier: "+str(device.identifier))
        print("Alias: "+str(device.alias))
        print("Device: "+str(device.name))
        print("Model: "+str(device.model)) 
    
    if cli["steps"]:
        if cli["date"] == None:
            steps_adq = device.get_daily_steps_date()
        else:
            steps_adq = device.get_daily_steps_date(cli["date"][0], cli["date"][1])

        if cli["histogram"]:
            tb_graph.histogram(steps_adq)
        else:
            print(steps_adq)    
