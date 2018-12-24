import googletrans
import os 
import json


def main():
    folder = os.listdir('./')
    folder = [x for x in folder if x.endswith('.json')]
    jsonPath = folder[0]
    with open(jsonPath) as f:
        print(json.load(f)['text'])

def trans(text):
    """
    text translate happens here.
    """
    return

if __name__ == '__main__':
    main()