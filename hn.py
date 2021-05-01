import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

def get_top_stories():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

    return response.json()

def get_item(item_id):
    response = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(item_id) + '.json')

    return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='hn.py - yet another Hacker News script for the terminal')
    parser.add_argument('items', nargs='?', type=int, default=50, help='Number of items to fetch')
    args = parser.parse_args()

    print('Hacker News\n')

    top_stories = get_top_stories()[:args.items]

    with ThreadPoolExecutor(max_workers=args.items) as pool:
        front_page = list(pool.map(get_item, top_stories))

    for index, story in enumerate(front_page, start=1):
        print('%s. %s [%s]' % (index, story['title'], story['score']))

        try:
            print(story['url'], '\n')
        except KeyError:
            try:
                print(story['text'], '\n')
            except KeyError:
                print('\n')
