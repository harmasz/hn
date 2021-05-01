# hn.py - yet another 'Hacker News for the terminal' script
Written in under 40 lines of Python. Based on the [Hacker News API](https://github.com/HackerNews/API).

## Usage
Clone this repo and run the script:
    git clone
    python hn.py [items]

The script accepts an optional argument called 'items' - the amount of stories to fetch from HN.
By default it will return 50 top stories. The HN API can return up to 500 stories at once.
