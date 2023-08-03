from data_types import ResultItem


def simple_response_block(url: str, search_str: str, random_gif: ResultItem) -> dict:
    return {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "image",
                "image_url": url,
                "title": {
                    "type": "plain_text",
                    "text": search_str or "too lazy to write something"
                },
                "alt_text": random_gif.content_description
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2qIqHI7E1o0IFdT4Dm3eCoI5rPk-g7t7KTA&usqp=CAU",
                        "alt_text": "you have hovered upon the symbol of Trash!  Long live the great King Kadoshi and the fruit of his loins: Shiraz, Orpaz and Liraz"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "you have been UvTrashed! (if you cant see the gif go here: <https://help.ambition.com/hc/en-us/articles/5873432207899-How-can-I-automatically-display-large-GIFs-in-Slack-workflows-|change settings>)"
                    }
                ]
            }
        ]
    }