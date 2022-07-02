from opentele.tl import TelegramClient
from opentele.api import API,UseCurrentSession,CreateNewSession
from opentele.tl import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import asyncio
import sys
import os
from anyascii import anyascii
import random
import glob
import string

async def main(argv):
    list_images = glob.glob('images/*.jpg')
    file = random.choice(list_images)
    if len(list_images) == 0:
        return -1
    sessionfilepath = argv[0]
    mode = argv[1]
    password  = argv[2]
    hint = argv[3]
    if len(argv) > 4:
        proxy_ip = argv[4]
        proxy_port = argv[5]
    else:
        proxy_ip = None
        proxy_port = None

    listapi = [API.TelegramAndroid.Generate, API.TelegramDesktop.Generate, API.TelegramAndroidX.Generate, API.TelegramIOS.Generate, API.TelegramMacOS.Generate]
    api = random.choice(listapi)()
    if proxy_ip:
        client = TelegramClient(sessionfilepath, api=api, proxy=("http", proxy_ip, proxy_port))
    else:
        client = TelegramClient(sessionfilepath, api=api)
    sessionbasedir = os.path.dirname(sessionfilepath)
    phone_number = os.path.basename(os.path.splitext(sessionfilepath)[0])
    
    count = 0
    while count <= 3:
        count += 1
        try:
            if count == 3:
                client  = TelegramClient(sessionfilepath, api=api)
            await client.connect()
            break
        except:
            if count == 3:
                return -1

    me = await client.get_me()
    if me is None:
        return -1

    try:
        isSetUserName = me.username is None
        if isSetUserName:
            name = me.first_name
            if me.last_name is not None:
                name = f'{name}{me.last_name}'

            name = anyascii(name).replace(" ", "")

            if not (name[0].isalpha() and name.isalnum()):
                nchars = name
                name = ''.join(random.choices(string.ascii_lowercase, k=nchars))

            username = f'{name}{phone_number[-6:]}'
        else:
            username = me.username

        listmode = [UseCurrentSession, CreateNewSession]
        modeconvert = listmode[int(mode)]
        tdesk = await client.ToTDesktop(flag=modeconvert,api=api)
        tdesk.SaveTData(os.path.join(sessionbasedir, 'tdata'))
        try:
            status = await client.edit_2fa(new_password=password, hint=hint)
            if status == False:
                await client.send_message(me.id, "2FA password is incorrect")
                return -1
        except Exception as e:
            await client.send_message(me.id, f"{e}")
            return -1
        if isSetUserName:
            try:
                await client(UpdateUsernameRequest(f'{username}'))
            except Exception as e:
                await client.send_message(me.id, f"{e}")
                return -1

        with open(os.path.join(sessionbasedir, 'info.txt'), 'w') as f:
            f.writelines(f'{phone_number}|{username}|{password}\n')

        try:
            await client(UploadProfilePhotoRequest(file=await client.upload_file(file)))
        except Exception as e:
            await client.send_message(me.id, f"Lỗi khi set avatar file: {file}")
            await client.send_message(me.id, f"{e}")
            return -1

    except Exception as e:
        await client.send_message(me.id, f"{e}")
        return -1
    await client.disconnect()
    
    return 0

if __name__ == '__main__':
    sys.tracebacklimit = 0
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    exitcode = asyncio.run(main(sys.argv[1:]))
    sys.exit(exitcode)
