from datetime import datetime

log_file = 'my_app.log'

def parse_line(line):
    parts = line.split(" — ")
    if len(parts):
        try:
            timestamp = datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S,%f')
            return {"timestamp": timestamp, "hostname": parts[1], "name": parts[2], "level": parts[3], "message": parts[4] }
        except Exception as e:
            print(e)
            return None
    return None

with open(log_file, 'r') as file:
    logs = file.readlines()

previous_line_time = None
for n, line in enumerate(logs):
    parsed_line = parse_line(line)
    if parsed_line:
        if previous_line_time and parsed_line["timestamp"] < previous_line_time:
            print(f"Log order error on line {n+1}")
        previous_line_time = parsed_line["timestamp"]
    else:
        print(f"Log format error on line {n+1}")
