# Email-SMS-Spam-Classifier

Build a spam classifier program in python which can tell whether a given message is spam or not. processes I followed to build this classifier are:

- Data Cleaning: dropping the columns with very less non-nun values
- EDA to get insights of the data
- NLTK for text preprocessing (Text Lower case, Tokenization, Removing stop words and punctuation, Stemming)
- Various plotting (Pairplot, heatmap, WordCloud)
- Converting text data into vectors (CountVectorizer, TfidfVectorizer)
- Tried multiple classifiers but the accuracy_score & precision_score of naive_bayes's BernoulliNB was best
- Deployment using Heroku
- Click Here To Visit Web Page: [The Sparks Foundation.](https://esclassifier.herokuapp.com/)
