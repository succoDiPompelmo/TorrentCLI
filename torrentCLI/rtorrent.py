import torrentCLI.rtorrent_client

def add_torrent(magnet):

    rtorrent_client.load_magnet(magnet)
    download_list = rtorrent_client.get_download_list()

    for item_hash in download_list:
        rtorrent_client.start_torrent(item_hash)