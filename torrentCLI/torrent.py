from torrentCLI.utility import my_import

# search_engine is not a good name, doesn't imply the fact that is a string, hard to comprehend
# Move to dictionary and remove pandas, add parsing function for the results
def add_index_name_key(index_results, index_name):
    return [dict(torrent, **{'search engine': index_name}) for torrent in index_results]

def filter_no_magnets(results):
    return [torrent for torrent in results if torrent['magnet']]

def sort_by_peer(results):
    return sorted(results, key=lambda x: x['seeder'], reverse=True)

def search(engines, name):
    results = []
    for engine in engines:
        search_class = my_import(engine)
        search_instance = search_class()
        index_results = search_instance.get_results(name)
        results.extend(add_index_name_key(index_results, engine))

    # Filter here
    filtered_results = filter_no_magnets(results)
    # Sort Here
    sorted_results = sort_by_peer(filtered_results)

    return sorted_results