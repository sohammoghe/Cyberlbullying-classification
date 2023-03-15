# Imports
import pickle
import streamlit
import sklearn

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer


# Streamlit title
st.title(" Cyberbullying classification (Hinglish) ")

# Getting text input 
input_text = st.text_input("Enter text to check for cyberbullying: ")

# Button for prediction
trained_model=pickle.load(open("DecisionTreeClassifier.pkl", 'rb'))
if st.button(" Predict whether cyberbullying or not"):
  data = [input_text]
  tfidf_vector = TfidfVectorizer(stop_words= content_list, lowercase = True,vocabulary=pickle.load(open("tfidf_vector_vocabulary.pkl", "rb")))
  data= tfidf_vector.fit_transform(data)
  print(data.shape)

  
  print(trained_model.predict(data))
  if(trained_model.predict(data)==1):
    st.warning('Cyberbullying present', icon="⚠️")
  else:
    st.success('Cyberbullying not present', icon="✅")
