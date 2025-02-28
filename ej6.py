import re

log_input = input().strip()

pattern = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3} +([a-zA-Z0-9_]+) +[0-9]+ --- \[([a-zA-Z0-9]+)\] +([a-zA-Z0-9_.]+) +: +(.*)')
match = pattern.search(log_input)

if match:
    log_level, thread, clazz, message = match.groups()
    clazz = clazz.split('.')[-1]
    print(f'"{log_level}","{thread}","{clazz}","{message}"')