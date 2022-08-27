import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()



# we can also import transform_txt as a pickle file
def transform_txt(txt):
    txt = txt.lower()
    txt = nltk.word_tokenize(txt)

    y = []
    for i in txt:
        if i.isalnum():
            y.append(i)

    txt = y[:]
    y.clear()

    for i in txt:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    txt = y[:]
    y.clear()

    for i in txt:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))



## lottie animation code
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return none
    return r.json()

lottie_coding = load_lottieur("https://assets10.lottiefiles.com/packages/lf20_4x9a2h9p.json")
st_lottie(lottie_coding, height=200, key="Mail Animation")



# streamlit codes
st.markdown("<h1 style='text-align: center; color: red;'>Email/SMS Spam Classifier</h1>", unsafe_allow_html=True)
input_sms = st.text_area("Please Enter The Message In The Below Box")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_txt(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")





# name
st.markdown("<h4 style='text-align: center;color:grey; font-size: 15px;'>©2022 Neeraj Kumar </h4>", unsafe_allow_html=True)


    # streamlit run app.py