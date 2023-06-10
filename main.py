from telethon.tl.functions.channels import JoinChannelRequest
import telethon
import telethon.events as events
import asyncio
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


async def main():
    client = telethon.TelegramClient(
        "client", api_id="21914867", api_hash="dac740fd98dd53ddf513ad19c53976a3", system_version="4.16.30-vxCUSTOM")

    await client.start()

    @client.on(events.NewMessage("https://t.me/+KKDQyEMlpUc0NDIy"))
    async def for_start_sending(message):
        users = set()
        with open("groups.txt", "r") as file:
            for line in file.readlines():
                messages = await client.get_messages(line, limit=10000)
                for message in messages:
                    try:
                        users.add(message.to_dict()['from_id']['user_id'])
                        print('yes')
                    except:
                        print("oops")
                time.sleep(400)
        for user in users:
            if user not in "5182790073, 649907279, 757000679".split(", "):
                await client.send_message(user, """Предлагаем вступить в группу <a href='https://t.me/remont_georgia'>Ремонт Грузия</a>. 
В группе можно размещать <i>бесплатно (всегда)</i> свои услуги по ремонту всего и вся в городах, в которых вы эти услуги предоставляете.
Цель создания группы - помочь русскоязычным в каждом уголке прекрасной Грузии.
<b>Всем мастерам предлагаем услуги мониторинга Телеграм по вашим ключевым словам.</b>""", parse_mode="HTML")
                time.sleep(10)

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
