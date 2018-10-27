#!/usr/bin/env python3 -tt
"""
Tests the most basic function of the platform module, namely `putPipe`.
"""
if __name__ == '__main__':
    import campy.private.platform as _platform

    while True:
        choice = input('(P)ut or (G)et? ')
        if choice.lower().startswith('p'):
            cmd = input("putPipe: ")
            _platform.Platform().put_pipe(cmd)
        if choice.lower().startswith('g'):
            result = _platform.Platform().get_result()
            print(result)
