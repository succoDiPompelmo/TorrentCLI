# simple test program (from the XML-RPC specification)
from xmlrpc.client import ServerProxy, Error

# TODO: Add wrapper to manage server proxy
# TODO: Add checks before starting the torrent

def load_magnet(magnet):

    with ServerProxy("http://192.168.1.218:8000") as proxy:
        proxy.load.normal("", magnet)


def start_torrent(hash):

    with ServerProxy("http://192.168.1.218:8000") as proxy:
        proxy.d.start(hash)


def get_torrent_name(hash):

    with ServerProxy("http://192.168.1.218:8000") as proxy:
        torrent_name = proxy.d.name("", hash)
    return torrent_name


def get_download_list(state='stopped'):

    with ServerProxy("http://192.168.1.218:8000") as proxy:
        download_list = proxy.download_list("", state)
    return download_list


# with ServerProxy("http://192.168.1.218:8000") as proxy:

#     try:
        # print(proxy.system.listMethods())

    #     print(proxy.d.state("A4A26F7C35DA01920D8D15B30221344D67055D08"))

    #     print(proxy.d.complete("A4A26F7C35DA01920D8D15B30221344D67055D08"))

    #     print(proxy.d.start("A4A26F7C35DA01920D8D15B30221344D67055D08"))

    # except Error as v:
    #     print("ERROR", v)