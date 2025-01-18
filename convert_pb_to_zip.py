import os
import zipfile

def zip_folder(folder_path, output_path):
    """
    Zips the contents of a folder.

    :param folder_path: The path to the folder to zip.
    :param output_path: The path where the zipped file will be saved.
    """
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

# Example usage:
folder_to_zip = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model2'
output_zip_file = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model2.zip'
zip_folder(folder_to_zip, output_zip_file)
