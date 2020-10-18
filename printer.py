
from tabulate import tabulate


def display_results(results, count):

    tabulate_results = [
        [
            result['name'],
            result['size'],
            result['seeder'],
            result['search engine']
            ] for result in results]
    print(tabulate(
        tabulate_results[:count], 
        headers=['NAME', 'SIZE', 'SEEDER', 'SEARCH ENGINE'], 
        showindex=True))
    print("\n")

    return None