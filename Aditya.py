import os
import pyrogram
from pyrogram import Client

api_id = 19181985
api_hash = "a2b23ca3a1c9b5dab4bf42dda7de4e79"

try:
   os.remove("aditya.session")
except:
     pass
with Client("aditya", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [𝐀𝐝𝐢𝐭𝐲𝐚 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/adityaserver) ✨**"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("AdityaServer")
        app.join_chat("AdityaDiscus")
        app.join_chat("kaalware")
        app.join_chat("Sanki_World")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("aditya.session")
