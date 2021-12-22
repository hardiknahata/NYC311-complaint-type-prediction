import streamlit as st
from simpletransformers.classification import ClassificationModel
from constants import id_to_category

"""
ModelServing Class instantiates the transformer model and sets up the SteamLit App.
When the user enters text input and presses the submit button, the model predicts the
complaint category and prints on the Web App.
"""
class ModelServing():

    def __init__(self):
        self.model = ClassificationModel("roberta", "best_model", use_cuda = False)
        st.title('NYC 311 Complaint Type Prediction')

    def start_model_serving(self):

        form = st.form(key='my_form')
        complaint = form.text_input(label='Type your complaint here:')
        submit = form.form_submit_button(label='Predict')

        if submit:
            prediction, raw_outputs = self.model.predict([complaint])
            predicted_label = id_to_category[prediction[0]]       
            st.write(f'Complaint Type: {predicted_label}')
    
if __name__ == '__main__':
    ModelServing().start_model_serving()
    
    
