import pickle
import streamlit as st

# ModelServing Class instantiates the transformer model and sets up the SteamLit App.
# When the user enters text input and presses the submit button, the model predicts the
# complaint category and prints on the Web App.
class ModelServing():

    def __init__(self):
        self.model = pickle.load( open( "linear_svc_model.pkl", "rb" ) )
        self.tfidf_vectorizer = pickle.load( open( "tfidf_vectorizer.pickle", "rb" ) )
        st.title('NYC 311 Complaint Type Prediction')
        st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
        # st.footer('Made by <a href="http://hardiknahata.com>"')

    def start_model_serving(self):

        form = st.form(key='my_form')
        complaint = form.text_input(label='Type your complaint here:')
        submit = form.form_submit_button(label='Predict')

        if submit:
            if not complaint:
                 st.write(f'Complaint Description Cannot be Empty')
            else:
                vectorizer_input = self.tfidf_vectorizer.transform([complaint])
                predicted_label = self.model.predict(vectorizer_input)[0]      
                # st.write(f'Complaint Category: {predicted_label}')
                st.metric('Complaint Category', predicted_label)
    


if __name__ == '__main__':
    ModelServing().start_model_serving()