import random
import requests
import json
from data_types import JsonData, ResultItem, SlackCommand
import logging
from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from slack_bolt import App
from blocks import simple_response_block


load_dotenv()
logger = logging.getLogger(__name__)
apikey = os.environ.get("TENOR_API_KEY")
limit = os.environ.get("GIFS_PRE_REQUEST_LIMIT")
client_key = os.environ.get("TENOR_CLIENT_KEY")
tenor_user_prefix = os.environ.get("TENOR_USER_PREFIX")

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.command("/trash")
def handle_command(ack, respond, command):
    # Acknowledge command request
    ack()
    command_obj = SlackCommand.model_validate(command)
    search_str = command_obj.text
    search_term = f"{tenor_user_prefix} {search_str}" if search_str else tenor_user_prefix
    r = requests.get(f"https://tenor.googleapis.com/v2/search?q={search_term}&key={apikey}&client_key={client_key}&limit={limit}")

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_gifs = json.loads(r.content)
        obj = JsonData.model_validate(top_gifs)
        #if no results return a random one. better than nothing I guess :-\
        if not obj.results:
            r = requests.get(f"https://tenor.googleapis.com/v2/search?q={tenor_user_prefix}&key={apikey}&client_key={client_key}&limit={limit}")
            top_gifs = json.loads(r.content)
            obj = JsonData.model_validate(top_gifs)

    random_gif: ResultItem = random.choice(obj.results)
    url = random_gif.media_formats.gif.url
    # url = random_gif.media_formats.mediumgif.url # also an option to reduce size
    block_response = simple_response_block(url=url, search_str=search_str, random_gif=random_gif)

    respond(block_response)


# Start your app - in deployment
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))


# # Start your app for local testing in socket mode
# if __name__ == "__main__":
#     SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

