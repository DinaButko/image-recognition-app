
## 🚀 Image Recognition Application
## Note: Data Set is not included in the folder as it was downloaded using kaggle
## 🌍 Demo:

Link: https://comp-377-image-recogn-project.herokuapp.com/

## 📚 Overview:

This is a simple image recognition application. Th trained model (model.tflite) takes an image as an input and predict the class of image from 0 to 7.
Dataset is from https://www.kaggle.com/datasets/puneet6060/intel-image-classification

## 💡 Instructions how to build a model:
1. Open Google Collaboration Notebook
2. In the Kaggle user should use json token to download the dataset
3. Run the Notebook after JSON token installation
4. First model was built using TF
5. But at the end we used TF Lite 
6. User might install dependencies
7. This model (model.tflite) wiil be used to generate predictions for the BackEnd

Google notebook with the model: https://colab.research.google.com/drive/1-2-cCbDPyjff2g2O22b6317TFnwvApK4?usp=sharing

## 📕 How to run the application:
1. Run the virtual environment. Fo Mac user's iw will be:  source venv/bin/activate
2. In the virtual requirement user mught instal dependencies uding command: pip3 install -r windows_requerements.txt
3. To tun the server using FAST-API user should add command on Mac: uvicorn main:app
4. After that user can open server and the application
5. But it's not neccesssary, as this app was deployed on Heroku. For Heroku we added dependencies (requirements.txt, Procfile, and runtime.txt)
6. Click "Choose File" and choose file for the future prediction
7. Select an image (.jpg) from the files
8. Clik "Upload" and see the Prediction Result
9. User is able to upload several images at the same time to predict several images
10. Image prediction will be displayed

## Technologies Used:
<img src="https://user-images.githubusercontent.com/97703238/178814355-928d855b-2bb8-46e7-a155-05fc63dd0a44.svg" align="left" width="150" height="100">
<img src="https://user-images.githubusercontent.com/97703238/178814383-62bafcf8-6e43-4123-bc39-1b6037ba0cf3.png" align="right" width="150" height="100">
<img src="https://user-images.githubusercontent.com/97703238/178814404-ce49ca3d-020b-4ac1-bed8-e809a97bdec0.png" align="left" width="150" height="100">
<img src= "https://user-images.githubusercontent.com/97703238/178814458-3fdc22af-766f-4e8a-a070-20983f44aad8.png" align="right" width="150" height="100">
<img src= "https://user-images.githubusercontent.com/97703238/178814585-c8acb4df-bc30-40f8-ab1a-a90e9bf4e937.png" align="left" width="150" height="100">

##Team



