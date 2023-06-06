import logging
import requests
import json
import time
import os
from dotenv import load_dotenv
from ossapi import Ossapi

load_dotenv()
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

api = Ossapi(CLIENT_ID, CLIENT_SECRET)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

try:
    with open("scores.json", "x") as scores:
        logging.info("Created new scores file.")
except Exception:
    pass

def compare_scores(osu_users, scores):
    diff = osu_users["TeeVee20105"] - osu_users["OniiAlex"]
    for osu_user in osu_users.keys():
        rank_diff = osu_users[osu_user] - scores[osu_user]
        if rank_diff > 0:
            announce_rank_change(osu_user, "fell off by", abs(rank_diff), osu_users, diff)
        elif rank_diff < 0:
            announce_rank_change(osu_user, "gained", abs(rank_diff), osu_users, diff)


def announce_rank_change(user, change, rank_diff, osu_users, diff):
    message = "{user} {change} {rank_diff} rank(s)! {ranks}, diff: {diff}".format(
        user = user,
        change = change,
        rank_diff = rank_diff,
        ranks = osu_users,
        diff = diff
    )
    print(message)

def send_webhook_message(message):
    payload = {
        "content": message,
        "embeds": None,
        "attachments": []
    }
    response = requests.post(WEBHOOK_URL, json = payload)
    logging.info("Sent message to discord with response:", response)

while True:
    teevee = api.user(26424193, mode="osu")
    oniialex = api.user(18361076, mode="osu")

    osu_users = {
        teevee.username: teevee.statistics.global_rank,
        oniialex.username: oniialex.statistics.global_rank,
    }

    with open("scores.json", "r") as scores:
        if os.path.getsize("scores.json") != 0:
            compare_scores(osu_users, json.loads(scores.read()))

        
    with open("scores.json", "w") as scores:
        json.dump(osu_users, scores)
    time.sleep(1 * 60)