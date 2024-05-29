from flask import Flask, request, render_template, redirect, url_for
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans 

app = Flask(__name__)


#-------------Functions-----------------

def find_top_colors(image, num_top_colors=10)
# Step1 - Convert Image to numpy array
img_array = np.array(image)

# Step2 - Reshape array to a list of Pixels
# width * height = pixels
img_array = img_array.reshape(img_array[0] * img_array[1],3)

# Step3 - Use Kmeasure to find top colors
kmeans = KMeans(n_clusters = num_top_colors)
kmeans.fit(img_array)
colors = kmeans.cluster_centers_

return colors.astype(int)


@app.route('/')
def home():
  file = request.files['files']
  if 'file' not in request.files:
    return redirect ("index.html)

  if file.filename == '':
    pass

  if file:
  image = Image.open(file.stream)
  top_colors = find_top_colors(image)
  return render_template('result.html', top_colors=top_colors)

  if __name__ =='__main__':
    app.run(debug=True)

