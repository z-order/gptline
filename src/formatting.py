import datetime
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML
import os

def formattedTime(timestamp):
    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    dt = dt.astimezone()
    return dt.strftime("%b %d, %Y at %I:%M %p")

def print_message(timestamp, role, content, deleted, prefix=""):
    s = prefix + f"[{formattedTime(timestamp)}] <i>{role}</i>: {content}"
    if deleted:
        print_formatted_text(HTML("<strike>" + s + "</strike>"))
    else:
        print_formatted_text(HTML(s))


def setMark():
    if 'TERM' in os.environ and os.environ['TERM'].startswith('screen'):
        osc = "\033Ptmux;\033\033]"
        st = "\a\033\\"
    else:
        osc = "\033]"
        st = "\a"

    print(f"{osc}1337;SetMark{st}", end='')

