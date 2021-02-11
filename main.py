from flask import *
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
   return render_template('home.html')


@app.route('/', methods = ['POST'])
def scanning():


	from PIL import Image
	import pytesseract
	import os
	import pickle

	valid_formats = [".jpg", ".png"]
	valid_files = []

	data = {}

	if not os.path.exists(".save.pickle"):

		def generate():

			for f in os.listdir():
				
				ext = os.path.splitext(f)[1]
				if ext.lower() not in valid_formats:
					continue

				# print("processing ", f)
				yield "processing " + str(f) + "<br>"
				text = pytesseract.image_to_string(Image.open(f).convert('LA')).lower()
				text = text.replace("\n", " ")

				data[f] = text


		# for i in data:
		# 	print(data[i])

		pickle.dump(data, open(".save.pickle", "wb"))

	data = pickle.load(open(".save.pickle", "rb"))

	# print(data["Story-of-my-life.jpg"])
	# print()

	search = "i"

	search = search.lower()

	for i in data:
		if search in data[i]:
			print(i)

	name = request.form['inputdir']



	return Response(generate())
	# return render_template('home.html', name=name)


if __name__ == '__main__':
   app.run()