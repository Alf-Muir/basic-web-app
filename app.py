from flask import Flask, request, redirect, url_for, render_template
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

app = Flask(__name__)

connect_str = "DefaultEndpointsProtocol=https;AccountName=alfstorageaccount1;AccountKey=1wWmxeeecJgf0gURR6hYWGKPHKB1gc6w00mWq6DBVlU8I3o6vwypv18Dwu6muCXxFNb+3hskz5ol+AStF9JAsQ==;EndpointSuffix=core.windows.net"
container_name = "container1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container_name, uploaded_file.filename)
        blob_client.upload_blob(uploaded_file.read())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
