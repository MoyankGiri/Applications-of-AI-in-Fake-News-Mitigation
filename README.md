# Applications-of-AI-in-Fake-News-Mitigation

This repository is the implementation for the paper titled: Automated and Interpretable Fake News Detection with Explainable Artificial Intelligence <br>
The paper is available here: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4076594

## Abstract
Fake news is a piece of misleading/forged information which affects society, business, governments etc and hence is an imperative issue. The solution presented here to detect fake news involves purely making use of rigorous machine learning approaches in implementing a hybrid of simple
yet accurate fake text detection models and fake image detection models in order to detect fake news. The solution takes into consideration the text and images of any news article, extracted using web scraping, where text segment of a news article is analyzed using an ensemble model of the
Naïve Bayes, Random Forest and Decision Tree Classifier which showed improved results than the individual models. The image segment of a news article is analyzed using only Convolution Neural Network which showed optimal accuracy similar to the text model. To better train the text models, data pre-processing and aggregation methods were used to combine various fake-real news datasets in order to have ample amounts of data. Similarly, to train the image model, CASIA dataset was used over which Error Level Analysis was performed to detect fake images. Model results are represented as Confusion Matrices and are measured using various performance metrics. Also, to provide an explanation for predictions from the hybrid model, Explainable Artificial Intelligence is used.
