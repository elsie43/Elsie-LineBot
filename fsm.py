from transitions.extensions import GraphMachine
from utils import send_sticker_message, send_text_message, send_image_message, myAddress

import random

jokes = ["Q: 夕陽西下，斷腸人在哪裡？\nA: 醫院。",
         "Q: 濁水溪跟高屏溪為什麼不能在一起？\nA: 因為他們不是（適）河（合）。",
         "Q: 哪裡的河流速最快？\nA: 鄉下，因為鄉間河太急。",
         "Q: 巫婆死掉變什麼？\nA: Switch.",
         "媽媽跟小陳說不要指月亮\n小東: 蛤？",
         "Q: 為什馬克杯跟玻璃杯打招呼，但是玻璃杯不理他？\nA: 因為玻璃杯沒耳朵。",
         "Q: 家貓的叫聲是喵，山貓的叫聲是什麼？\nA: 喵的啦。"]

stores = ["迷客夏", "五十嵐", "圓石", "鮮茶道", "不知道"]  # 大苑子 御私藏 茶湯會
menus = ['https://www.milkshoptea.com/upload/price/2111020819100000002.jpg',
         'https://twcoupon.com/images/menu/p_50lan_20140730.jpg',
         'https://user-images.strikinglycdn.com/res/hrscywv4p/image/upload/c_limit,fl_lossy,h_9000,w_1200,f_auto,q_auto/5032892/441445_248482.jpeg',
         'https://scontent.ftpe7-4.fna.fbcdn.net/v/t1.6435-9/155226190_5028806183856854_7587239303416551165_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=c4c01c&_nc_ohc=SXCCCw6YJWcAX_U2VsM&_nc_ht=scontent.ftpe7-4.fna&oh=00_AT9Cjhs9vpMi9BZ-BYsYoe2kSOqIBCbhT2PXaU_Ri_zzOw&oe=61F5BB92']


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_joke(self, event):
        text = event.message.text
        return (text.lower() == "joke" or text == "講笑話")

    def on_enter_joke(self, event):
        print("I'm entering joke")
        reply_token = event.reply_token
        thejoke = random.choice(jokes)
        send_text_message(reply_token, thejoke)
        self.go_back()

    def is_going_to_drink(self, event):
        text = event.message.text
        return (text.lower() == "drink" or text == "喝飲料")

    def on_enter_drink(self, event):
        print("I'm entering drink")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "輸入店名可取得該店「台南地區」菜單，目前本服務提供的店家有:\n\n迷客夏\n五十嵐\n圓石\n鮮茶道\n\n其餘店家持續更新中...\n如果不知道喝什麼就輸入『不知道』，將提供您隨機菜單！")
        #thestore = "已取得" + random.choice(stores) + "的菜單"
        #send_text_message(reply_token, thestore)
        # self.go_back()

    def is_going_to_selectStore(self, event):
        text = event.message.text
        return (text in stores)

    def on_enter_selectStore(self, event):
        print("I'm entering select")
        text = event.message.text
        reply_token = event.reply_token
        #thestore = "已取得" + text + "的菜單"
        if text == "不知道":
            menuIndex = random.randint(0, len(menus))
        else:
            menuIndex = stores.index(text)
        send_image_message(reply_token, menus[menuIndex])
        self.go_back()

    def is_going_to_state1(self, event):
        text = event.message.text
        return ("選擇障礙" in text)

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "想問什麼？我能幫你二選一喔！")

    def is_going_to_state3(self, event):
        text = event.message.text
        return ("新年" in text)

    def on_enter_state1(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "新年快樂！")
        self.go_back()

    def is_going_to_state2(self, event):
        return 1

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        result = random.random()
        if result < 0.5:
            send_sticker_message(reply_token, '8525', '16581290')
        else:
            send_sticker_message(reply_token, '8522', '16581287')
        self.go_back()

    '''
    def on_exit_state1(self):
        print("Leaving state1")
    def on_exit_state2(self):
        print("Leaving state2")
    '''
