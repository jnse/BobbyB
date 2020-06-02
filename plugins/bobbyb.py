import re
import operator
import random
import json
from collections import defaultdict
from threading import Lock
from time import time, sleep

from sqlalchemy import Boolean, Column, Integer, PrimaryKeyConstraint, String, Table, and_, desc
from sqlalchemy.sql import select

from cloudbot import hook
from cloudbot.event import EventType
from cloudbot.util import database
from cloudbot.util.formatting import pluralize_auto, truncate
from cloudbot.util.func_utils import call_with_args

def get_random_quote():
    """ Returns random quote from quotes file"""
    with open('quotes.json', 'r') as quotes:
        bobbyb_quotes = json.load(quotes)
    return random.choice(bobbyb_quotes)

bobby_re = re.compile(r"^.*bobbyb.*$", re.IGNORECASE)
@hook.regex(bobby_re)
def bobbyb_regex(match, conn, nick, chan, message):
    message(get_random_quote())

