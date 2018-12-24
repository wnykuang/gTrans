from googletrans import Translator
import multiprocessing as mp
import os 
import json


def main():
    folder = os.listdir('./')
    folder = [x for x in folder if x.endswith('.json')]
    #jsonPath = folder[0]
    tc = 0
    for filepath in folder:
        if tc < 5:
            with open(filepath, 'r') as f:
                rawText = json.load(f)['text']
                print(trans(rawText))



def trans(text):
    """
    text: string
    returnt: cnText, string
    text translate happens here.
    """
    tL = Translator(timeout=12)
    cnText = tL.translate(text, dest='zh-cn')
    return cnText

if __name__ == '__main__':
    main()