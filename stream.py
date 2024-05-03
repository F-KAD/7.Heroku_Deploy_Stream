import streamlit as st
from PIL import Image
import requests
import os

# Définition de la fonction pour afficher l'image associée au sentiment

def sentiment_image(sentiment): 
    if sentiment == "Positive":
        return Image.open("images/Positif.png").resize((250, 250))
    else:
        return Image.open("images/Negatif.png").resize((250, 250))

# Définition de la fonction pour obtenir le sentiment à partir de l'API
def get_sentiment_API(User_Tweet):
    try:
        #response = requests.get(url=f"http://127.0.0.1:8000/predict?tweet={User_Tweet}")
        response = requests.get(url=f"https://sentimentapi-dcc39a5227fd.herokuapp.com/predict?tweet={User_Tweet}")
        if response.status_code == 200:
            response_json = response.json()
            pred, sentiment = response_json.values()
            return pred, sentiment
        else:
            st.error(f"Erreur {response.status_code} lors de la requête vers l'API.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Une erreur de connexion s'est produite : {e}")
        return None

# Définition de la fonction pour obtenir les sentiments
def get_sentiments(User_Tweet): 
    # Prédiction et le sentiment associé
    result = get_sentiment_API(User_Tweet)
    
    if result is not None:  # Vérifier si result est différent de None
        pred, sentiment = result
            
        # Affichage de l'accuracy de mon model associé à cette prédiction de sentiment
        st.latex(r"Predicted\,Accuracy: \textcolor{blue}{" + str(round(pred, 4)) + "}")

        # Affichage du sentiment associé au tweet
        st.latex(r"The\,associated\,Sentiment\,: \textcolor{blue}{" + sentiment + "}")

        # Affichage de l'image associée au sentiment
        st.image(sentiment_image(sentiment))
    else:
        st.error("Erreur lors de la prédiction du sentiment.")

# Fonction principale pour l'interface utilisateur
def Render():
    # Titre de l'application
    st.title(" Application for Sentiment Analysis ")
    st.divider() 
    
    # En-tête de l'application
    st.latex("Deep\,Learning\,for\,Sentiment\,Analysis")  
   
    # Ligne de séparation avec des émoticônes
    st.latex("😍   😁   😊   😐   😕   🙁   😡")
    st.divider()
    
    # Demande à l'utilisateur d'entrer un tweet
    st.latex("Insert\,And\,Predict\,the\,associated\,sentiment\,of\,your\,Tweet")
    User_Tweet = st.text_input("", placeholder="Insert your English Tweet for prediction")

    # Bouton pour lancer la prédiction
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        if st.button("Predict", help="Click to make prediction"):
            if User_Tweet != "":  
                get_sentiments(User_Tweet)  

    st.divider()
    st.latex(r"\textcolor{black}{\textbf{Sentiment\,Analysis\,Prediction\,using\,LSTM\,Stematisation\,with\,Glove\,Embedding\,Model}}")
    st.divider()        

# Appel de la fonction Render pour exécuter l'interface utilisateur
Render()
