try:
    from yt_dlp import YoutubeDL as ytdl
except ModuleNotFoundError:
    print("please install pip package `yt_dlp` before running")

def download(download, search = False):
    if search:
        download = "ytsearch:" + download
    with ytdl({}) as ydl:
        ydl.download([download])

num = 0
print("type `exit` or press ctrl + c to exit")

while True:
    try:
        inp = input(f"[{num}] enter youtube link to download or download first search result by +<what to search>\n> ").strip()
        inpt = inp.split("+", 1)[1].strip() if "+" in inp else inp
        print(f"your input: `{inp}`")
        if inp.lower() == "exit":
            break
        try:
            if inp.startswith("+"):
                download(inpt, True)
            else:
                download(inpt)
        except KeyboardInterrupt:
            print(f"\n[{num}] stopped download for `{inpt}`")
        except Exception as e:
            print(f"[{num}] error occured while downloading `{inpt}`\n[{num}] err: {repr(e)}")
        print(f"[{num}] download for `{inpt}` complete")
        num = num + 1
        print()
    except KeyboardInterrupt:
        break

print("\nexited loop")