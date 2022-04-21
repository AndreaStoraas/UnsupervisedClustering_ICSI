#Create a script that makes 1 html file per cluster
import os

#This is a folder with 29 folders: one for each cluster. Each cluster folder contains the video frames belonging to that specific cluster
source_dir = 'gMeans_tSNE_29clusters'
#Target folder for the html-pages
target_dir = 'htmlpages_gMeans_tSNE'
folder_names = os.listdir(source_dir)
folder_names = folder_names[1:]
print(folder_names)
print(len(folder_names))
num_clusters = 29

common_filename = 'CNNfeatures_GMeans_tSNE_'

for cluster in range(num_clusters):
    image_path =  source_dir + '/' + folder_names[cluster]
    print(image_path)
    image_files = os.listdir(image_path)
    #filename = common_filename + folder_names[cluster] + '.html'
    filename = target_dir + '/' + common_filename + folder_names[cluster] + '.html'
    print(image_files)
    print(filename)
    html_file = open(filename, 'w')
    header = '''
    <!DOCTYPE html>
    <html>
    <body>
    <h2>Images for
    '''
    cluster_text = folder_names[cluster]
    
    end_text = '''
    </body>
    </html>
    '''
    html_file.write(header)
    html_file.write(cluster_text + '</h2>')
    for image in image_files:
        html_file.write('<img src="/Users/username/Documents/projectFolder/') #Change this to appropriate string
        html_file.write(str(image_path) + '/' + str(image))
        html_file.write('" alt="Sperm_cluster2" width="350" height="200">')
    html_file.write(end_text)
    html_file.close()
