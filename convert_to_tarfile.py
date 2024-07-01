import os
import tarfile
import shutil

# Path to the directory containing the .pb model file
pb_model_dir = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model'

# Name of the .pb model file
pb_model_file = 'saved_model.pb'

# Output tar.gz file path
output_tar_gz_file = 'C:\\Users\\awsli\\kserve-tensorflow\\saved_model\\0001\\saved_model.tar.gz'

try:
    # Create a temporary directory to hold the .pb model file
    temp_dir = '/c/Users/awsli/kserve-tensorflow/temp'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Copy the .pb model file to the temporary directory
    shutil.copy(os.path.join(pb_model_dir, pb_model_file), temp_dir)
    
    # Create a tar.gz file
    with tarfile.open(output_tar_gz_file, 'w:gz') as tar:
        # Add the contents of the temporary directory to the tar file
        tar.add(temp_dir, arcname=os.path.basename(pb_model_dir))
    
    print(f"Successfully created tar.gz file: {output_tar_gz_file}")
except Exception as e:
    print(f"An error occurred while creating the tar.gz file: {e}")
finally:
    # Clean up: Remove the temporary directory
    shutil.rmtree(temp_dir, ignore_errors=True)
