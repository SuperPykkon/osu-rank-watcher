#
# WARNING!!!
# EXTREME CRINGE AHEAD
# PROCEED WITH CAUTION
# (I don't know why I didn't delete this)
#

from ossapi import Ossapi
import requests
import datetime
import time

# create a new client at https://osu.ppy.sh/home/account/edit#oauth
api = Ossapi("<redacted>", "<redacted>")

def send_message(message):
    payload = {"content": message, "embeds": None, "attachments": []}
    response = requests.post("<redacted>", json = payload)
    print(datetime.datetime.now(), "Sent message to discord with response:", response)

while True:
    # see docs for full list of endpoints
    teevee = api.user(26424193, mode="osu")
    oniialex = api.user(18361076, mode="osu")
    with open(teevee.username + ".txt", "r") as teevee_f:
        teevee_p = int(teevee_f.read())
        with open(oniialex.username + ".txt", "r") as oniialex_f:
            oniialex_p = int(oniialex_f.read())

            if teevee.statistics.global_rank > teevee_p:
                send_message(teevee.username + " fell off by " + str(teevee.statistics.global_rank - teevee_p) + " rank(s)! " + teevee.username + ": " + str(teevee.statistics.global_rank) + ", " + oniialex.username + ": " + str(oniialex.statistics.global_rank) + ", diff: " + str(teevee.statistics.global_rank - oniialex.statistics.global_rank))
            elif teevee.statistics.global_rank < teevee_p:
                send_message(teevee.username + " gained " + str(teevee.statistics.global_rank - teevee_p) + " rank(s)! " + teevee.username + ": " + str(teevee.statistics.global_rank) + ", " + oniialex.username + ": " + str(oniialex.statistics.global_rank) + ", diff: " + str(teevee.statistics.global_rank - oniialex.statistics.global_rank))

            if oniialex.statistics.global_rank > oniialex_p:
                send_message(oniialex.username + " fell off by " + str(oniialex.statistics.global_rank - oniialex_p) + " rank(s)! " + teevee.username + ": " + str(teevee.statistics.global_rank) + ", " + oniialex.username + ": " + str(oniialex.statistics.global_rank) + ", diff: " + str(teevee.statistics.global_rank - oniialex.statistics.global_rank))
            elif oniialex.statistics.global_rank < oniialex_p:
                send_message(oniialex.username + " gained " + str(oniialex.statistics.global_rank - oniialex_p) + " rank(s)! " + teevee.username + ": " + str(teevee.statistics.global_rank) + ", " + oniialex.username + ": " + str(oniialex.statistics.global_rank) + ", diff: " + str(teevee.statistics.global_rank - oniialex.statistics.global_rank))

    with open(teevee.username + ".txt", "w") as teevee_f:
        with open(oniialex.username + ".txt", "w") as oniialex_f:
            teevee_f.write(str(teevee.statistics.global_rank))
            oniialex_f.write(str(oniialex.statistics.global_rank))
    time.sleep(1 * 60)