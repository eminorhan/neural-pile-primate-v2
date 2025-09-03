import requests
import subprocess

ACCESS_TOKEN = input("Enter your Zenodo access token:")
record_id = "3854034"

r = requests.get(f"https://zenodo.org/api/records/{record_id}", params={'access_token': ACCESS_TOKEN})
download_urls = [f['links']['self'] for f in r.json()['files']]
filenames = [f['key'] for f in r.json()['files']]

print(f"{len(download_urls)} files to download")

for filename, url in zip(filenames, download_urls):
    try:
        # Construct the wget command
        wget_command = ["wget", "-O", filename, url]

        # Execute the command using subprocess.run
        subprocess.run(wget_command, check=True)  # check=True raises an exception on non-zero exit code
        print(f"Downloaded {filename} successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error downloading {filename}: {e}")
    except FileNotFoundError:
        print("Error: wget is not installed. Please install it (e.g., 'apt-get install wget' or 'brew install wget').")
    except Exception as e: # Catching a broad exception to handle other potential issues
        print(f"An unexpected error occurred: {e}")

print("Download process complete.")