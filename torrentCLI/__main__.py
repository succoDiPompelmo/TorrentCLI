from torrentCLI.inquiry import make_inquiry

import torrentCLI.torrent as torrent
import logging

from torrentCLI.rtorrent import add_torrent
from torrentCLI.log_module import init_logger
from torrentCLI.printer import display_results
from torrentCLI.parser import parse_results_command

import configparser
import pathlib

package_path = pathlib.Path(__file__).parent.absolute()

config = configparser.ConfigParser()
config.read(str(package_path) + '/settings.ini')

init_logger(config, package_path)
logger = logging.getLogger(__name__)

# TODO: Handle multipage search
# TODO: Schema Validation
# TODO: Rework, two main methods initilize and get_torrents
# TODO: Add verbosity level in order to debug response
# TODO: Add method check connectivity, or test to check plugins health state
# TODO: Implement save option and copy option
# TODO: If available add date to torrents info

# NOTE: torrent_indexes could be a good name

def torrent_cli():

    search_engines, name, count = make_inquiry()
    logger.info(f"SEARCH ENGINE: {search_engines}, NAME: {name},COUNT: {count}")
    torrents_data = torrent.search(search_engines, name)

    if len(torrents_data) == 0:
        print("No items retrived with the current search criteria !!")
        exit(1)
    
    # print_torrents
    display_results(torrents_data, count)
    # cli_logic
    input_str = ""

    while True:
        input_str = input("Select an ID to show the magnet or press q to quit : ")
        code, choice = parse_results_command(input_str)

        try:
            selected_magnet = torrents_data[choice]['magnet']
        except TypeError:
            selected_magnet = None

        if code == 'h':
            print('Options:',
                '[s<links>]: Display magnets to terminal',
                '[r<links>]: Launch download from rtorrent',
                '[q] Quit', sep='\n')
        if code == 's':
            try:
                print(selected_magnet)
            except ValueError:
                break
        if code == 'r':
            try:
                add_torrent(selected_magnet)
            except ValueError:
                break
        if code == 'q':
            exit(1)


if __name__ == '__main__':
    torrent_cli()