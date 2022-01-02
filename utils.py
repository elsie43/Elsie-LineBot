import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImageCarouselColumn
from linebot.models import StickerSendMessage, ImageCarouselTemplate, URITemplateAction, ButtonsTemplate, MessageTemplateAction, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
#myAddress = 'https://hwbotelsie.herokuapp.com'
myAddress = 'https://a1bf-218-166-130-174.ngrok.io'


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"


def send_sticker_message(reply_token, packageID, stickerID):
    line_bot_api = LineBotApi(channel_access_token)
    sticker_message = StickerSendMessage(
        package_id=packageID,
        sticker_id=stickerID
    )
    line_bot_api.reply_message(reply_token, sticker_message)
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
