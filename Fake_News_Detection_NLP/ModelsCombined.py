import pickle

def PredictionFromAllModels(newsArticle = ''):
    DecisionTreeModel = pickle.load(open("Fake_News_Detection_NLP\Saved_Models\FakeNews_DecisionTree.sav", 'rb'))
    result_dt = DecisionTreeModel.predict([newsArticle])
    RandomForestClassifierModel = pickle.load(open("Fake_News_Detection_NLP\Saved_Models\FakeNews_RandomForestClassifier.sav", 'rb'))
    result_rf = RandomForestClassifierModel.predict([newsArticle])
    MultinomialNaiveBayesModel = pickle.load(open("Fake_News_Detection_NLP\Saved_Models\FakeNews_MultinomialNaiveBayes.sav", 'rb'))
    result_nb = MultinomialNaiveBayesModel.predict([newsArticle])
    return (result_dt and result_rf and result_nb)