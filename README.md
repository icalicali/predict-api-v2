# Predict API

## Trigger the predict function from the model and get the API prediction endpoint :
This is a python code, so make sure you have python installed on your system.

1. Clone the repository then open it using your code editor.
2. This code is using Google Cloud Storage, so you have to make your own GCS Bucket, make a folder named __predict_uploads__ inside the bucket, get the credentials file (.json file) and name it "__credentials.json__" (to match with the scripts) then copy it to the root directory of this project.
3. Go to __main.py__ edit the code in line 34, change '__trashure-bucket__' with the name of the bucket that you created in the previous step.
4. Open terminal in the project root directory, then run `pip install -r requirements.txt` to install the dependencies.
5. Run the app using the command: `python main.py`.
6. By default, the server will run on the localhost with the port 5000, open [http://localhost:5000](http://localhost:5000) to view it in your browser.
7. If it shows 'OK' then you have successfully run the predict api.
