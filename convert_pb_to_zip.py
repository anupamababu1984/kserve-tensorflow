import zipfile
import os

def convert_pb_to_zip(pb_file_path, zip_file_path):
    # Ensure the .pb file exists
    if not os.path.isfile(pb_file_path):
        raise FileNotFoundError(f"The file {pb_file_path} does not exist.")
    
    # Create a zip file and add the .pb file to it
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(pb_file_path, os.path.basename(pb_file_path))
    print(f"Converted {pb_file_path} to {zip_file_path}")

# Replace 'yourfile.pb' and 'yourfile.zip' with your file paths
pb_file_path = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model\\0001\\saved_model.pb'
zip_file_path = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model\\saved_model.zip'

convert_pb_to_zip(pb_file_path, zip_file_path)
