#!/usr/bin/env python3
import sys

FILE_NAME = 'Data_Bot'

def main():
    try:
        for line in sys.stdin:
            message = line.rstrip('\n')
            with open(FILE_NAME, 'a', encoding='utf-8') as f:
                f.write(message + '\n')
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
