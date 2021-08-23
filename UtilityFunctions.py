from newspaper import Article
import requests # to get image from the web
import shutil # to save it locally
import os
#url = 'https://www.ndtv.com/india-news/no-coercive-action-against-news-broadcasters-association-over-non-compliance-with-new-it-rules-says-kerala-high-court-2482677'

def GetTextOfArticle(url):

    if(url.isspace() or url == ''):
        return []
    else:
        try:
            article = Article(url)
            article.download()
            article.parse()
            textArticle = (article.text).replace("\n"," ")
            return textArticle
        except:
            return ""
    
def GetListOfImageURLs(url = ''):

    if(url.isspace() or url == ''):
        return []
    else:
        try:
            article = Article(url)
            article.download()
            article.parse()
            ImageList = []
            for i in article.images:
                ImageList.append(i)
            return ImageList
        except:
            return []


def DownloadImageFromURL(image_url = ''):

    try:
        filename = "./Article_Images/" + image_url.split("/")[-1]
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream = True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ',filename)
            return filename
        else:
            print('Image Couldn\'t be retreived')
            return ""
    except OSError:
        return ""


def DeleteAllArticleImages(PathToDirectory = ''):
    if (PathToDirectory.isspace() or PathToDirectory == './Article_Images'):
        return False
    else:
        for f in os.listdir(PathToDirectory):
            os.remove(os.path.join(PathToDirectory, f))
        return True