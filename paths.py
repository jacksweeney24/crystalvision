import os

# Define the paths
destination_file = os.path.join('lionsgate', 'index.html')

# Read the content of the file
with open(destination_file, 'r') as file:
    content = file.read()

# Update the paths
content = content.replace('href="css/', 'href="../css/')
content = content.replace('src="js/', 'src="../js/')
content = content.replace('src="images/', 'src="../images/')
content = content.replace('poster-url="images/', 'poster-url="../images/')
content = content.replace('video-urls="images/', 'video-urls="../images/')

# Write the updated content back to the file
with open(destination_file, 'w') as file:
    file.write(content)

print(f"Updated paths in {destination_file}.")