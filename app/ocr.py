import argparse, cv2, os, sys
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image


class OCR:

    LANGUAGES = {
        'en': 'eng',        # english
        'fr': 'fra',        # frensh
        'es': 'spa',        # Spanish
        'ar': 'ara',        # arabic
        'de': 'deu',        # German
        'zh': 'chi-sim',    # chinese
        'it': 'ita',        # Italian
        'ja': 'jpn',        # Japanese 
        'pt': 'por',        # Portuguese
        'ru': 'rus',        # russian
        'tr': 'tur',        # turkish
        'ko': 'kor'         # Korean
    }

    def _preprocess(self, image, method):
        
        ''' convert image to grayscale and apply preprocessing '''
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if method == 'thresh':
            return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        if method == 'blur':
            return cv2.medianBlur(image, 3)

    def _matchLanguage(self, lang):

        try:
            return self.LANGUAGES[lang]
        except Exception:
            sys.exit('Error: unsupported language "{}"'.format(lang))

    def imageToString(self, imagePath, preprocess, lang):

        image = self._preprocess(image=cv2.imread(imagePath), method=preprocess)

        try:
            return pytesseract.image_to_string(image, lang=self._matchLanguage(lang))
        except Exception as e:
            sys.exit(e)


class App:

    TEXT_PATH = './out.txt'

    def __init__(self):

        self.parseArgs()
        if not os.path.isfile(self.args['image']):
            sys.exit('No such file: {}'.format(self.args['image']))

    def parseArgs(self):

        argParser = argparse.ArgumentParser()
        argParser.add_argument('-i', '--image', required=True, help='Path to input image', type=str)
        argParser.add_argument('-l', '--language', required=True, help='Text\'s language', type=str,
            choices=['en', 'es', 'ar', 'fr', 'de', 'zh', 'it', 'ja', 'pt', 'ru', 'tr', 'ko'])
        argParser.add_argument('-p', '--preprocess', required=False, help='Type of preprocessing', type=str,
            choices=['thresh', 'blur'], default='thresh')
        
        self.args = vars(argParser.parse_args())

    def extractText(self):
        
        self.text = OCR().imageToString(
            imagePath = self.args['image'],
            preprocess = self.args['preprocess'],
            lang = self.args['language']
        )

    def saveText(self):

        try:
            file = open(self.TEXT_PATH, 'w')
            file.write(self.text)
        except Exception as e:
            print('Error writing text to file !\n{}'.format(e))
        finally:
            file.close()

    def main(self):

        self.extractText()
        self.saveText()

if __name__ == '__main__':
    App().main()
    