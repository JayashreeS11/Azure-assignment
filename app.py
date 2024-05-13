from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient, ContainerClient

app = Flask(__name__)

# Azure Blob Storage credentials
connection_string = "DefaultEndpointsProtocol=https;AccountName=jayashrees11storage;AccountKey=bJ2ea2c5vvcH34JiPh3xSeOxbdgWZaPXZyV+zPdE1weL88rl8kW5iX/kO7xvlsguBoHXlWEbcbV8+ASthPqVbA==;EndpointSuffix=core.windows.net"
container_name = "jayashrees11container"

@app.route('/list_files', methods=['GET'])
def list_files():
    folder_name = request.args.get('folder_name')

    if not folder_name:
        return jsonify({"error": "Folder name is required"}), 400

    try:
        # Connect to Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # List blobs in the folder
        blob_list = container_client.list_blobs(name_starts_with=folder_name)

        # Extract filenames
        file_list = [blob.name.split('/')[-1] for blob in blob_list]

        return jsonify({"folder_name": folder_name, "files": file_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
