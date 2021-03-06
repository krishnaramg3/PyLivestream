#!/usr/bin/env python
"""
LIVE STREAM using FFmpeg -- webcam

https://www.scivision.co/youtube-live-ffmpeg-livestream/

Windows: get DirectShow device list from::

   ffmpeg -list_devices true -f dshow -i dummy
"""
from typing import List
from pathlib import Path
import pylivestream as pls
import signal
from argparse import ArgumentParser

R = Path(__file__).parent


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    p = ArgumentParser(description="livestream webcam")
    p.add_argument('site', help='site to stream: [youtube,periscope,facebook,twitch]',
                   nargs='?', default='localhost')
    p.add_argument('-i', '--ini', help='*.ini file with stream parameters',
                   default=R/'stream.ini')
    p.add_argument('-y', '--yes', help='no confirmation dialog',
                   action='store_true')
    P = p.parse_args()

    site = P.site.split()

    S = pls.Webcam(P.ini, site, yes=P.yes)
    sites: List[str] = list(S.streams.keys())
# %% Go live
    if P.yes:
        print('going live on', sites)
    else:
        input(f"Press Enter to go live on {sites}.    Or Ctrl C to abort.")

    S.golive()


if __name__ == '__main__':
    main()
