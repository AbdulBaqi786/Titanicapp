import streamlit as st
import pickle
from PIL import Image
#UI: User Interface, How things look like.
#UX: User Experience, How does the user feel interacting with the app.


with open('titanicpickle.pkl' ,'rb') as pickleFile:    #here we Load the pretrained model

    #Opens a file named titanicpickle.pkl: The open() function is used to open the file located at
    #  'titanicpickle.pkl'. If the file exists, it is opened; if not, a FileNotFoundError will be raised.
   # Specifies the mode 'rb': The 'r' stands for "read", and the 'b' stands for "binary". This means the file is opened in read-only mode, and the data is read as binary. This is essential when working with binary files, such as those created by the pickle module, to ensure that the data is read correctly without any unintended transformations.
   # Uses a context manager (with statement): The with statement ensures that the 
   # file is properly closed after its suite finishes, even if an exception is raised.
   #  This is a best practice for handling file operations, as it automatically manages file closing, 
   # reducing the risk of file corruption or memory leaks.

   # Assigns the opened file to pickleFile: Within the indented block following the with 
   # statement, pickleFile can be used as a file object to perform operations like reading.

    model=pickle.load(pickleFile)
    #The pickle.load(pickleFile) function reads the binary data from 
    # the file and converts it back into the original Python object.
    #The restored object is then assigned to the variable model.

    st.title('AB Titanic Survival Prediction Web Application')
    st.image('TitanicIMG.jpg',caption='Predict Passengers Survival on the Titanic')
    #Set the title and Display an Image for Branding

#Function for making the predictions
def PredictionFunction(Pclass, sex, Age, SibSp, Parch, Fare, Embarked): #Defines a function named PredictionFunction that takes in seven inputs related to a Titanic passenger's details.
    try: #Attempts to execute the code within this block. If an error occurs, it will be caught by the except block.
     prediction=model.predict([[Pclass, sex, Age, SibSp, Parch, Fare, Embarked]]) #Uses the pre-trained machine learning model (model) to predict the survival outcome based on the input features. 
    #model.predict(...): Calls the predict method of the model to make a prediction.
     return 'Survivd' if prediction[0] ==1 else 'Did not Survive' #prediction: Stores the result, which is typically an array like [1] (survived) or [0] (did not survive).
    #prediction[0]: Accesses the first (and only) element of the prediction array.
    #If the prediction is 1, it returns 'Survived'; otherwise, it returns 'Did not Survive'.
    except Exception as e:#Exception as e: Captures the exception and assigns it to the variable e.
        return f'Error:{str(e)}' #str(e): Converts the exception message to a string.

#Sidebar for Instructions
st.sidebar.header('How to Use Or instructions') # This refers to Streamlit's sidebar, a vertical panel on the left side of the app where you can place widgets, text, and other elements.
#.header('How to Use Or instructions'): This adds a header titled "How to Use Or instructions" to the sidebar. Headers are typically used to label or separate different sections within the sidebar.
st.markdown("""    
1. Please Enter the Passenger Details in the form
2. the Click the 'Predict Button' to see the SUrvival Results
3. Adjust Values to Test Different Scenarios
""")   #Triple Quotes """...""": This denotes a multi-line string in Python, allowing you to write text that spans multiple lines.     
st.sidebar.info('Example: A 30 years old male, 3rd class, $20 Fare, travelling alone from port southhampton.')

#main input form 
def main(): #def is key word used for function definition, main is the name function here, and : the colon shows the starT of a function
 st.subheader('Enter the passenger details: ')#.subheader(...): This function displays text in a subheader format,
col1, col2=st.columns(2)#st.columns(2): This function creates two equal-width columns in your Streamlit app
                            #These are variables representing the two columns created.


#Organize inputs in columns
with col1:
      Pclass = st.selectbox('Passenger Class: ', options = [1,2,3], format_func= lambda X: f'class{X}')
      Sex = st.radio('Sex:', options=['male', 'female'])
      Age = st.slider('Age:', min_value=0, max_value=100, value=30)

with col2:
      SibSp = st.slider('Siblings/Spouses Aboard:', min_value=0, max_value=10, value=0)
      Parch = st.slider('Parents/Children Aboard:', min_value=0, max_value=10, value=0)
      Fare = st.slider('Fare($):', min_value=0.0, max_value=500.0, value=50.0, step=0.1)
      Embarked = st.radio('Port of Embarkation: ', options=['C','Q','S'], format_func= lambda X :f'port{X}')

#Convert Categorical inputs to numeric values  
Sex = 1 if Sex == 'female' else 0
Embarked = {'C':0, 'Q':1, 'S':2}[Embarked]   


 #Button for Prediction
if st.button('Predict'):
        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        st.markdown(f'{result}')
        st.balloons()

#Run the main function
if __name__ == '__main__':
    main()

