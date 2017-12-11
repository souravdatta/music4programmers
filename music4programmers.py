# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:27:26 2017

@author: sourav
"""

import urllib.request as request
import os
import sys
import feedparser
import multiprocessing
import time


FEED_URL = 'https://musicforprogramming.net/rss.php'
DARWIN_COMMAND = 'open "{}"'


def show_progress():
    while True:
        print('.', end='')
        sys.stdout.flush()
        time.sleep(1)


class Music:
    @staticmethod
    def build_file_path(title):
        title = title.replace(' ', '_')
        title = title.replace(':', '_')
        path = title + '.mp3'
        home_dir = os.path.expanduser('~') + os.sep + 'music4programming'

        if not os.path.exists(home_dir):
            os.makedirs(home_dir)

        return '{}{}{}'.format(home_dir, os.sep, path)

    @staticmethod
    def download_file(url, file_name):
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        process = multiprocessing.Process(target=show_progress)
        process.start()

        downloaded_binary = request.urlopen(req).read()

        with open(file_name, 'wb') as f:
            f.write(downloaded_binary)

        process.terminate()
        print()
        print('Music downloaded: {}'.format(file_name))

    @staticmethod
    def play_a_music(file_name):
        if sys.platform == 'darwin':
            # for mac
            os.system(DARWIN_COMMAND.format(file_name))
        elif sys.platform == 'win32':
            # for windows
            os.startfile(file_name)
        else:
            print('Do not know how to play {}, please play it with your music player'.format(file_name))

    @staticmethod
    def create_album_data():
        data = [Music(f['id'], f['subtitle']) for f in feedparser.parse(FEED_URL)['entries']]
        data.reverse()

        return data

    def __init__(self, url, title):
        self.url = url
        self.title = title
        self.playing = False
        self.txt = None
        self.audio = None

    def play(self):
        path = self.build_file_path(self.title)

        if not os.path.exists(path):
            self.download_file(self.url, path)

        self.playing = True
        self.play_a_music(path)

    def __str__(self):
        return '{} ==> {}'.format(self.title, self.url)


def list_musics(mdata):
    i = 1
    for m in mdata:
        print('{}. {}'.format(i, m))
        i += 1


def main():
    mdata = Music.create_album_data()
    list_musics(mdata)

    choice_accepted = False
    choice = 0

    while True:
        while not choice_accepted:
            choice = input('Which song? (type exit or quit to stop the program, list to list music again)\n: ')

            if choice == 'quit' or choice == 'exit':
                sys.exit(0)

            if choice == 'list':
                list_musics(mdata)
                continue

            try:
                choice = int(choice)
                choice -= 1

                if (choice < 0) or (choice >= len(mdata)):
                    raise ValueError()

            except ValueError:
                print('Hmm, bad input that is. Not in range of (1 - {}) it was.'.format(len(mdata)))
            else:
                choice_accepted = True

        mdata[choice].play()
        print('ok')
        choice_accepted = False


if __name__ == '__main__':
    main()



