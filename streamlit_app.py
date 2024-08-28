# Assuming the model was trained on the first 3 features: Pregnancies, Glucose, BloodPressure

# Input fields in the sidebar
Pregnancies = st.sidebar.number_input('Pregnancies', min_value=0, max_value=17, value=1)
Glucose = st.sidebar.number_input('Glucose', min_value=0, max_value=200, value=1)
BloodPressure = st.sidebar.number_input('BloodPressure', min_value=0, max_value=122, value=1)

# Load the model
model_path = 'model.pkl'  # Ensure this is the correct path to your model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    # Button for prediction
    if st.sidebar.button('Predict'):
        # Predict using the model with only 3 features
        prediction = model.predict([[Pregnancies, Glucose, BloodPressure]])
        result = "Diabetic" if prediction[0] == 1 else "Non-diabetic"
        
        # Display the result
        st.success(f"The model predicts that the patient is: **{result}**")
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")
