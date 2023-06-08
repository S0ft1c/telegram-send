from telethon.tl.functions.channels import JoinChannelRequest
import telethon
import telethon.events as events
import asyncio


async def main():
    client = telethon.TelegramClient(
        "client", api_id="21914867", api_hash="dac740fd98dd53ddf513ad19c53976a3", system_version="4.16.30-vxCUSTOM")

    await client.start()

    @client.on(events.NewMessage("https://t.me/for_start_sending"))
    async def for_start_sending(message):
        with open("groups.txt", "r") as file:
            for line in file.readlines():
                updates = await client(JoinChannelRequest(line))
                try:
                    users = await client.get_participants(line)
                    for user in users:
                        try:
                            await client.send_message(user, """Предлагаем вступить в группу <a href='https://t.me/remont_georgia'>Ремонт Грузия</a>. 
В группе можно размещать <i>бесплатно (всегда)</i> свои услуги по ремонту всего и вся в городах, в которых вы эти услуги предоставляете.
Цель создания группы - помочь русскоязычным в каждом уголке прекрасной Грузии.
<b>Всем мастерам предлагаем услуги мониторинга Телеграм по вашим ключевым словам.</b>""", parse_mode="HTML")

                        except Exception as e:
                            print(e)
                except:
                    pass
    
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
