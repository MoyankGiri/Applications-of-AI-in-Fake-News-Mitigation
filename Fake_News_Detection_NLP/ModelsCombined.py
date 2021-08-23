import pickle
from ELA import ErrorLevelAnalysis
from pylab import array
import numpy as np
from keras.models import load_model

def PredictionFromAllTextModels(newsArticle = ''):
    DecisionTreeModel = pickle.load(open("Fake_News_Detection_NLP\Saved_Models\FakeNews_DecisionTree.sav", 'rb'))
    result_dt = DecisionTreeModel.predict([newsArticle])
    RandomForestClassifierModel = pickle.load(open("Fake_News_Detection_NLP\Saved_Models\FakeNews_RandomForestClassifier.sav", 'rb'))
    result_rf = RandomForestClassifierModel.predict([newsArticle])
    MultinomialNaiveBayesModel = pickle.load(open("Fake_News_Detection_NLP\Saved_Models\FakeNews_MultinomialNaiveBayes.sav", 'rb'))
    result_nb = MultinomialNaiveBayesModel.predict([newsArticle])
    return (result_dt and result_rf and result_nb)


def ImagePrediction_uploadedimage(UploadedImage):
    if UploadedImage == None:
        return False
    else:
        UploadedImage_ELA = [array(ErrorLevelAnalysis("C:/Users/moyan/Desktop/Applications-of-AI-in-Fake-News-Mitigation/Article_Images/" + UploadedImage.name, 90).resize((128, 128))).flatten() / 255.0]
        UploadedImage_ELA = np.array(UploadedImage_ELA)
        UploadedImage_ELA = UploadedImage_ELA.reshape(-1, 128, 128, 3)
        #loaded_model = pickle.load(open("Fake_Image_Detection_CNN/FakeImage_CNNModel.sav", 'rb'))
        #result = loaded_model.predict(UploadedImage_ELA)
        model1 = load_model('C:/Users/moyan/Desktop/Applications-of-AI-in-Fake-News-Mitigation/Fake_Image_Detection_CNN/FakeImage_CNNModel_resaved.h5')
        result = (model1.predict(UploadedImage_ELA)).argmax(axis = 1)[0]
        if result == 1:
            return True
        else:
            return False

def ImagePrediction_URL(ImagePathLists = []):
    if ImagePathLists == []:
        return [True]
    else:
        resultsList = []
        for ipath in ImagePathLists:
            ImageRef = [array(ErrorLevelAnalysis(ipath, 90).resize((128, 128))).flatten() / 255.0]
            ImageRef = np.array(ImageRef)
            ImageRef = ImageRef.reshape(-1, 128, 128, 3)
            model1 = load_model('C:/Users/moyan/Desktop/Applications-of-AI-in-Fake-News-Mitigation/Fake_Image_Detection_CNN/FakeImage_CNNModel_resaved.h5')
            result = (model1.predict(ImageRef)).argmax(axis = 1)[0]
            if result == 1:
                resultsList.append(True)
            else:
                resultsList.append(False)
        return resultsList