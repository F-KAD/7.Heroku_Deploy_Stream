import streamlit as st
import requests

# Fonction pour envoyer une requête à l'API Flask
def get_prediction(tweet):
    try:
        response = requests.get(f"https://sentimentapi-dcc39a5227fd.herokuapp.com/predict?tweet={tweet}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Erreur {response.status_code} lors de la requête vers l'API Flask."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Une erreur de connexion s'est produite : {e}"}

# Fonction principale pour l'interface utilisateur
def main():
    st.title("Application for Sentiment Analysis")
    st.write("Insert and predict the sentiment of your tweet")

    tweet = st.text_input("Enter your tweet:", "")

    if st.button("Predict", key="predict_button", help="Click to make prediction"):
        if tweet:
            prediction = get_prediction(tweet)
            if "error" in prediction:
                st.error(prediction["error"])
            else:
                st.write("Predicted sentiment:", prediction["sentiment"])
                st.write("Predicted accuracy:", prediction["accuracy"])
        else:
            st.error("Please enter a tweet to predict.")

if __name__ == "__main__":
    main()
