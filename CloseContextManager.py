import logging
from contextlib import closing
from filehandling import FileHandling

class FileCloseDemo:
    logging.basicConfig(filename='context.log', level=logging.INFO)
    def __init__(self):
        logging.info('Initialize..')
        file=FileHandling()
        file.writeToFile()
        file.appendToFile()

    def openFile(self):
        logging.info('open file to write')
        self._file = open("bitbucket_headline.txt",mode='at',encoding='utf-8')

    def appendFile(self):
        logging.info('append to file')
        self._file.write("\n____END TEXT____")

    def close(self):
        try:
            logging.info('Close file')
            self._file.close()
            self._file.seek(8)
        except:
            logging.info("File Already Closed")

def performFileFunc():
    with closing(FileCloseDemo()) as demo:
        demo.openFile()
        demo.appendFile()


performFileFunc()