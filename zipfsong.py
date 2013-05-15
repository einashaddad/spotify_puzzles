#!/usr/bin/env python
'''
Usage:
$python zipfsongs.py <tests.txt>
'''
import sys

def zipfsongs(file_content):
    '''
    Returns a list of of m songs with the highest quality, in decreasing
    order of quality, giving precedence to order in album
    '''
    l_songs = file_content.split('\n')
    output_count = get_output_count(l_songs)
    song_frequencies = [song.split(' ') for song in l_songs[1:]]
    quality = calc_quality(song_frequencies)
    return [quality[i][0] for i in xrange(output_count)]

def calc_quality(song_frequencies):
    '''
    Calculates the quality according to zipf score and actual frequency,
    returns a list of tuples sorted by quality first and position
    in album second. 
    '''
    first_song_freq = float(song_frequencies[0][0])
    quality = []    
    for i, song in enumerate(song_frequencies):
        song_name = song[1]
        song_frequency = float(song[0])
        track_num = i + 1
        zipf = first_song_freq / track_num
        quality.append((song_name, song_frequency/zipf))
    return sorted(quality, key=lambda tup: tup[1], reverse=True)

def get_output_count(l_songs):
    stats = l_songs[0].split(' ')
    return int(stats[1])

if __name__ == '__main__':
    print zipfsongs(sys.stdin.read())

