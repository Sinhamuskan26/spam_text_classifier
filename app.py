import joblib
import streamlit as st

cv=joblib.load("count_vectorizer.pkl")
model=joblib.load("spam_detector_model.pkl")

st.title(
    " Spam Detector App"
)

st.write("Enter the text below to check whether its **Spam**  or **Not Spam** ")
user_input=st.text_area("enter the text Here:")


if st.button("Check Spam"):
    if user_input== "":
        st.warning("Please enter a message!")
    else:
        
        cv_text=cv.transform([user_input])
        prediction=model.predict(cv_text)
        print(prediction[0])

        if prediction[0] == 1:
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is NOT spam.")