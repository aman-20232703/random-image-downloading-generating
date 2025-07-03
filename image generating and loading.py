import requests
import multiprocessing

# Define the URL for the image source (random high-res image)
url = "https://picsum.photos/2000/3000"

# Function to download and save the image file
def download_file(url, name):
    print(f"📥 Started downloading file {name} ...")
    
    # Send a GET request to fetch the image
    response = requests.get(url)
    
    # Save the image in the 'multiprocessing' folder with a unique name
    with open(f"foldername/filename{name}.jpg", "wb") as file:
        file.write(response.content)

    print(f"✅ Finished downloading file {name}!")

# ---------------------------
# 👇 Method 1: Sequential Download
# ---------------------------
print("🔁 Starting SEQUENTIAL image downloads...\n")
for i in range(5):
    download_file(url, i)

# ---------------------------
# 👇 Method 2: Parallel Download using multiprocessing
# ---------------------------
print("\n🚀 Starting PARALLEL image downloads using multiprocessing...\n")

# Create a list to keep track of process objects
processes = []

for i in range(5):
    # Create a new process for each download task
    process = multiprocessing.Process(target=download_file, args=(url, i))
    process.start()
    processes.append(process)

# Wait for all download processes to complete
for process in processes:
    process.join()

print("\n🎉 All downloads completed successfully!")


