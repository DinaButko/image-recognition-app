from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import numpy as np
import cv2
from PIL import Image
import tflite_runtime.interpreter as tflite

# Added a model
model = tflite.Interpreter("static/model.tflite")
model.allocate_tensors()

# Create a variable to keep input details (image)
input_details = model.get_input_details()

# Create a variable to to show predicted value
output_details = model.get_output_details()

# Create a mapping for the class
class_mapping = {0: 'Building',
                 1: 'Forest',
                 2: 'Glacier',
                 3: 'Mountain',
                 4: 'Sea',
                 5: 'Street'}


# Create a function to predict a value
def model_predict(images_arr):
    predictions = [0] * len(images_arr)

    for i, val in enumerate(predictions):
        model.set_tensor(input_details[0]['index'],
                         images_arr[i].reshape((1, 150, 150, 3)))
        model.invoke()
        predictions[i] = model.get_tensor(
            output_details[0]['index']).reshape((6,))

    prediction_probabilities = np.array(predictions)
    argmaxs = np.argmax(prediction_probabilities, axis=1)

    return argmaxs


# Using FastApi
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Change image input size, because in model size is 150*150


def resize(image):
    return cv2.resize(image, (150, 150))

# Post images from the user


@app.post("/uploadfiles/", response_class=HTMLResponse)
# Create async function which helps to upload several images at the same time
async def create_upload_files(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        f = await file.read()
        images.append(f)

    images = [np.frombuffer(img, np.uint8) for img in images]
    images = [cv2.imdecode(img, cv2.IMREAD_COLOR) for img in images]
    images_resized = [resize(img) for img in images]
    images_rgb = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                  for img in images_resized]

    names = [file.filename for file in files]

    for image, name in zip(images_rgb, names):
        pillow_image = Image.fromarray(image)
        pillow_image.save('static/' + name)


# Create a path  for images
    image_paths = ['static/' + name for name in names]

    images_arr = np.array(images_rgb, dtype=np.float32)

    class_indexes = model_predict(images_arr)

    class_predictions = [class_mapping[x] for x in class_indexes]

    column_labels = ["Image", "Prediction"]

# Create html table
    table_html = get_html_table(image_paths, class_predictions, column_labels)

    content = head_html + """
    <marquee width="525" behavior="alternate"><h1 style="color:red;font-family:Arial">The Predictions IS!</h1></marquee>
    """ + str(table_html) + '''<br><form method="post" action="/">
    <button type="submit">Home</button>
    </form>'''

    return content


@app.post("/", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def main():
    content = head_html + """
    <marquee width="525" behavior="scroll"><h1 style="color:black;font-family:Arial">Upload Yourself A Picture</h1></marquee>
    <h3 style="font-family:Arial">The AI Will Predict Which of These Categories They Are:</h3><br>
    """

    original_paths = ['building_1.jpg', 'forest_1.jpg', 'glacier_1.jpg',
                      'mountain_1.jpg', 'sea_1.jpg', 'street_1.jpg']

    full_original_paths = ['static/original/' + x for x in original_paths]

    display_names = ['Building', 'Forest',
                     'Glacier', 'Mountain', 'Sea', 'Street']

    column_labels = []

    content = content + \
        get_html_table(full_original_paths, display_names, column_labels)

    content = content + """
    <br/>
    <br/>
    <form  action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """

    return content


head_html = """
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
<body style="background-image:url(../AI_Pic.jpg);">
<center>
"""

# Create a function to make a table


def get_html_table(image_paths, names, column_labels):
    s = '<table align="center">'
    if column_labels:
        s += '<tr><tr><h4 style="font-family:Arial">' + \
            column_labels[0] + '</h4></th><th><h4 style="font-family:Arial">' + \
            column_labels[1] + '</h4></tr></tr>'

    for name, image_path in zip(names, image_paths):
        s += '<tr><td><img height="80" src="/' + image_path + '" ></td>'
        s += '<td style="text-align:center">' + name + '</td></tr>'
    s += '</table>'

    return s
