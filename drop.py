import dropbox

import os

import argparse

import string


parser = argparse.ArgumentParser(description='Process some keys.')
parser.add_argument('--token', type=str)
parser.add_argument('--dir', type=str)


# Set up Dropbox API connection
args = parser.parse_args()

dbx = dropbox.Dropbox(str(args.token))

# Set the path to the Dropbox folder containing the video files

folder_path = args.dir

# Get a list of all files in the folder

files = dbx.files_list_folder(folder_path).entries

# Create a new playlist file

playlist_file = open('drop.m3u', 'w')

# Write the header to the playlist file

playlist_file.write('#EXTM3U\n')

# Loop through each file in the folder

for file in files:

# Check if the file is a video file

  if file.name.endswith(('.mp4', '.avi', '.mkv', '.mov')):

    # Create a Dropbox shared link to the file

    shared_link = dbx.sharing_create_shared_link(folder_path+'/'+file.name)

    # Replace the URL's domain to dl.dropboxusercontent.com

    shared_link_url = shared_link.url.replace('www.dropbox.com', 'dl.dropboxusercontent.com')

    # Write the file path to the playlist file

    playlist_file.write('#EXTINF:0,{0}\n{1}\n'.format(file.name, shared_link_url))

    # Close the playlist file

    playlist_file.close()

    print('Playlist created successfully!')
