import streamlit as st
import Fake_News_Detection_NLP.ModelsCombined as CombinedModelPredict
import os
import UtilityFunctions as uf

def save_uploaded_file(uploadedfile):
    with open(os.path.join("C:/Users/moyan/Desktop/Applications-of-AI-in-Fake-News-Mitigation/Article_Images/",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved file :{} in directory".format(uploadedfile.name))

#st.markdown("# Applications Of AI In Fake News Mitigation")
st.set_page_config(page_title = 'Applications of AI in FakeNews Mitigation')
st.title("Applications Of AI In Fake News Mitigation v1.0")
st.subheader("By Moyank Giri,Tarun Aditya")
option = st.sidebar.selectbox('Select the input type',['URL','Document','Text','Image'])


if option == 'URL':
    st.sidebar.info('Enter the URL to the news article')
    URLInput = st.sidebar.text_input("Enter the URL")
    ArticleText = uf.GetTextOfArticle(URLInput)
    ArticleImagesURLs = uf.GetListOfImageURLs(URLInput)
    ArticleImagePaths = []
    for iurl in ArticleImagesURLs:
        SavedFileName = uf.DownloadImageFromURL(iurl)
        if SavedFileName != "":
            ArticleImagePaths.append(SavedFileName)
    
    if st.sidebar.button('Predict'):
        ResultsList = CombinedModelPredict.ImagePrediction_URL(ArticleImagePaths)
        finalOutputImage = max(set(ResultsList), key = ResultsList.count)
        NumberOfTrue = ResultsList.count(True)
        NumberOfFalse = ResultsList.count(False)
        st.write("Number of True Images are:",NumberOfTrue)
        st.write("Number of Fake Images are:",NumberOfFalse)
        st.write("Final Image Prediction :",finalOutputImage)
        finalOutputText = CombinedModelPredict.PredictionFromAllTextModels(ArticleText)
        st.write("Final Text Prediction :",finalOutputText)

elif option == 'Document':
    st.sidebar.file_uploader("Please select your file",type=['pdf','txt'])

elif option == 'Text':
    st.sidebar.info('Enter the text body of the news article')
    NewsArticleTextInput = st.sidebar.text_area("Enter the Text of the news article")
    if st.sidebar.button('Predict'):
        FinalTextResult = CombinedModelPredict.PredictionFromAllTextModels(NewsArticleTextInput)
        if(str(FinalTextResult[0]) == 'True'):
            new_title = '<h style="font-family:sans-serif; color:Green; font-size: 42px;">' + str(FinalTextResult[0]) + '</h>'
            st.markdown(new_title, unsafe_allow_html=True)
        else:
            new_title = '<h style="font-family:sans-serif; color:Red; font-size: 42px;">' + str(FinalTextResult[0]) + '</h>'
            st.markdown(new_title, unsafe_allow_html=True)

else:
    UploadedImage = st.sidebar.file_uploader('Select the image file',type=['png','jpeg','jpg'])
    if UploadedImage is not None:
        file_details = {"FileName":"./Article_Images/" + UploadedImage.name,"FileType":UploadedImage.type}
        save_uploaded_file(UploadedImage)
    if st.sidebar.button('Predict'):
        if(UploadedImage != None):
            ImageResult = CombinedModelPredict.ImagePrediction_uploadedimage(UploadedImage)
            st.write(ImageResult)
        else:
            st.warning("Error, No file has been Uploaded.........Please upload an image to get results")
        
