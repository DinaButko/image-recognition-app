from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# using FastApi to upload pages
app = FastAPI()

# create the main function


@app.get("/", response_class=HTMLResponse)
async def main():
    content = head_html + """
    <marquee width="525" behavior="alternate"><h1 style="color:red;font-family:Arial">Please Upload Your Scenes!</h1></marquee>
    """
    return content


head_html = """
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
<body style="background-color:powderblue;">
<center>
"""


# Create a function to generate a table
def get_html_table(image_paths, names, column_labels):
    s = '<table align="center">'
    if column_labels:
        s += '<tr><th><h4 style="font-family:Arial">' + \
            column_labels[0] + '</h4></th><th><h4 style="font-family:Arial">' + \
            column_labels[1] + '</h4></th></tr>'

    for name, image_path in zip(names, image_paths):
        s += '<tr><td><img height="80" src="/' + image_path + '" ></td>'
        s += '<td style="text-align:center">' + name + '</td></tr>'
    s += '</table>'

    return s
