from flask import Flask, render_template, request, redirect, jsonify 
from PIL import Image  # for image processing
import numpy as np # for numerical operations and arrays for pixels of images
import tensorflow as tf # this a macine learning library 
import urllib.parse

app = Flask(__name__)

#load the file
model = tf.keras.models.load_model('model.h5')

#size of the image
target_size = (224, 224) 

#function to preprocess the image
def preprocess_image(image_path):
    img=Image.open(image_path)
    #resize the image
    img = img.resize(target_size)
    #convert the image to array
    img_array = np.array(img)
    #normalize the image
    img_array = img_array / 255.0
    #expand the dimensions
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

@app.route("/")
def page():
    return render_template('index-1.html')

@app.route("/templates/programs.html")
def programs():
    return render_template('programs.html')

@app.route("/templates/index.html")
def food():
    return render_template('index.html')

@app.route("/templates/tips.html")
def tips():
    return render_template('tips.html')

@app.route("/templates/index-1.html")
def home():
    return render_template('index-1.html')

@app.route("/templates/form-in.html")
def form1():
    return render_template('form-in.html')

@app.route("/templates/form-out.html")
def form2():
    return render_template('form-out.html')


@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp():
    Name = request.form['Name']
    Email = request.form['Email']
    Phone = request.form['Phone']
    Message = request.form['Message']

    data = {
        "*Name* ": Name,
        "*Email* ": Email,
        "*Phone* ": Phone,
        "*Message* ": Message
    }

    lines = []
    for key, value in data.items():
        line = f"{key}: {value}"  
        lines.append(line)

    message = "\n".join(lines)
    encoded_message = urllib.parse.quote(message)

    phone = "201093971431"
    whatsapp_link = f"https://wa.me/{phone}?text={encoded_message}"

    return redirect(whatsapp_link)
    


#route to handle the image upload 
@app.route("/upload", methods=["POST"])
def upload():
  

    if 'file' not in request.files:
        return jsonify({
            "error" : "No file "
        })

    #get the file
    file = request.files['file']

    if file.filename == " " :
        return jsonify({
            "error" : "No Selected file"
        })

    try:
        #preprocess the image
        img_array= preprocess_image(file)

        #predict the image
        prediction = model.predict(img_array)
        class_index= np.argmax(prediction[0])
        
        if class_index == 0:
            result = "Apple",
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-apple (182g)\n\nAmount per serving:"
            header2 = "Calories: 72"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.23g → 0%"
            p2sub = "- Saturated Fat: 0.039g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.07g\n- Monounsaturated Fat: 0.01g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 1mg → 0%\n▸Total Carbohydrate 19.06g → 7%"
            p3sub = "- Dietary Fiber: 3.3g → 12%\n- Sugars: 14.43g"
            p4 = "▸Protein 0.36g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 8mg → 1%\n▸Iron: 0.17mg → 1%\n▸Potassium: 148mg → 3%\n▸Vitamin A: 4mcg → 0%\n▸Vitamin C: 6.3mg → 7%"
        elif class_index == 1:
            result = "Apricot",
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-apricot (35g)\n\nAmount per serving:"
            header2 = "Calories: 17"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.14g → 0%"
            p2sub = "- Saturated Fat: 0.009g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.027g\n- Monounsaturated Fat: 0.06g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 0mg → 0%\n▸Total Carbohydrate 3.89g → 1%"
            p3sub = "- Dietary Fiber: 0.7g → 3%\n- Sugars: 3.23g"
            p4 = "▸Protein 0.49g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 5mg → 0%\n▸Iron: 0.14mg → 1%\n▸Potassium: 91mg → 2%\n▸Vitamin A: 34mg → 4%\n▸Vitamin C: 3.5mg → 4%"
        elif class_index == 2:
            result = "Avocado",
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-avocado (100g)\n\nAmount per serving:"
            header2 = "Calories: 160"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 14.66g → 19%"
            p2sub = "- Saturated Fat: 2.126g → 11%\n- Trans Fat: _\n- Polyunsaturated Fat: 1.816g\n- Monounsaturated Fat: 9.799g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 7mg → 0%\n▸Total Carbohydrate 8.53g → 3%"
            p3sub = "- Dietary Fiber: 6.7g → 24%\n- Sugars: 0.66g"
            p4 = "▸Protein 2g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 12mg → 1%\n▸Iron: 0.55mg → 3%\n▸Potassium: 485mg → 10%\n▸Vitamin A: 7mg → 1%\n▸Vitamin C: 10mg → 11%"
        elif class_index == 3:
            result = "Banana",
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-banana (118g)\n\nAmount per serving:"
            header2 = "Calories: 105"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.39g → 0%"
            p2sub = "- Saturated Fat: 0.132g → 1%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.086g\n- Monounsaturated Fat: 0.038g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 1mg → 0%\n▸Total Carbohydrate 26.95g → 10%"
            p3sub = "- Dietary Fiber: 3.1g → 11%\n- Sugars: 14.43g"
            p4 = "▸Protein 1.29g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\nC▸alcium: 6mg → 0%\n▸Iron: 0.31mg → 2%\n▸Potassium: 422mg → 9%\n▸Vitamin A: 4mcg → 0%\n▸Vitamin C: 10.3mg → 11%"
        elif class_index == 4:
            result = "Berry"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: berry-pieces(1 cup) (100g) \n\nAmount per serving:"
            header2 = "Calories: 48"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.43g → 1%"
            p2sub = "- Saturated Fat: 0.023g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.225g\n- Monounsaturated Fat: 0.062g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 1mg → 0%\n▸Total Carbohydrate 11.49g → 4%"
            p3sub = "- Dietary Fiber: 3g → 11%\n- Sugars: 7.01g"
            p4 = "▸Protein 0.98g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 23mg → 2%\n▸Iron: 0.6mg → 3%\n▸Potassium: 216mg → 5%\n▸Vitamin A: 1mcg → 0%\n▸Vitamin C: 81.4mg → 90%"
        elif class_index == 5:
            result = "Cantaloupe"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-Cantaloupe (177g)\n\nAmount per serving:"
            header2 = "Calories: 60"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.34g → 0%"
            p2sub = "- Saturated Fat: 0.09g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.143g\n- Monounsaturated Fat: 0.005g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 28mg → 1%\n▸Total Carbohydrate 14.44g → 5%"
            p3sub = "- Dietary Fiber: 1.6g → 6%\n- Sugars: 13.91g"
            p4 = "▸Protein 1.49g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 16mg → 1%\n▸Iron: 0.37mg → 2%\n▸Potassium: 473mg → 10%\n▸Vitamin A: 299mcg → 33%\n▸Vitamin C: 65mg → 72%"
        elif class_index == 6:
            result = "Cherry"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: cherry-pieces(12p) (100g) \n\nAmount per serving:"
            header2 = "Calories: 63"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.2g → 0%"
            p2sub = "- Saturated Fat: 0.038g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.052g\n- Monounsaturated Fat: 0.047g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 0mg → 0%\n▸Total Carbohydrate 16.01g → 6%"
            p3sub = "- Dietary Fiber: 2.1g → 8%\n- Sugars: 12.82g"
            p4 = "▸Protein 1.06g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 13mg → 1%\n▸Iron: 0.36mg → 1%\n▸Potassium: 222mg → 5%\n▸Vitamin A: 3mcg → 0%\n▸Vitamin C: 7mg → 8%"
        elif class_index == 7:
            result = "Coconut"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 piece-Coconut (45g)\n\nAmount per serving:"
            header2 = "Calories: 159"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 15.07g → 19%"
            p2sub = "- Saturated Fat: 13.364g → 67%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.165g\n- Monounsaturated Fat: 0.641g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 9mg → 0%\n▸Total Carbohydrate 6.85g → 2%"
            p3sub = "- Dietary Fiber: 4g → 14%\n- Sugars: 2.8g"
            p4 = "▸Protein 1.5g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 6mg → 0%\n▸Iron: 1.09mg → 6%\n▸Potassium: 160mg → 3%\n▸Vitamin A: 0mcg → 0%\n▸Vitamin C: 1.5mg → 2%"
        elif class_index == 8:
            result = "Grapes"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: grap-pieces(20-21p) (100g) \n\nAmount per serving:"
            header2 = "Calories: 69"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.16g → 0%"
            p2sub = "- Saturated Fat: 0.045g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.048g\n- Monounsaturated Fat: 0.007g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 2mg → 0%\n▸Total Carbohydrate 18.1g → 7%"
            p3sub = "- Dietary Fiber: 0.9g → 3%\n- Sugars: 15.48g"
            p4 = "▸Protein 0.72g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 10mg → 1%\n▸Iron: 0.36mg → 2%\n▸Potassium: 191mg → 4%\n▸Vitamin A: 3mcg → 0%\n▸  Vitamin C: 10.8mg → 12%"
        elif class_index == 9:
            result = "Guava"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-Guava (100g) \n\nAmount per serving:"
            header2 = "Calories: 68"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.95g → 1%"
            p2sub = "- Saturated Fat: 0.272g → 1%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.401g\n- Monounsaturated Fat: 0.087g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 2mg → 0%\n▸Total Carbohydrate 14.32g → 5%"
            p3sub = "- Dietary Fiber: 5.4g → 19%\n- Sugars: 8.92g"
            p4 = "▸Protein 2.55g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 18mg → 1%\n▸Iron: 0.26mg → 1%\n▸Potassium: 417mg → 9%\n▸Vitamin A: 31mcg → 3%\n▸Vitamin C: 228.3mg → 254%"
        elif class_index == 10:
            result = "Kiwi"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-kiwi (75g) \n\nAmount per serving:"
            header2 = "Calories: 46"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.4g → 1%"
            p2sub = "- Saturated Fat: 0.022g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.218g\n- Monounsaturated Fat: 0.036g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 2mg → 0%\n▸Total Carbohydrate 11.14g → 4%"
            p3sub = "- Dietary Fiber: 2.3g → 8%\n- Sugars: 6.83g"
            p4 = "▸Protein 0.87g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 26mg → 2%\n▸Iron: 0.24mg → 1%\n▸Potassium: 237mg → 5%\n▸Vitamin A: 3mcg → 0%\n▸Vitamin C: 70.5mg → 78%"
        elif class_index == 11:
            result = "Mandarin"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-mandarin (84g) \n\nAmount per serving:"
            header2 = "Calories: 35"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.25g → 0%"
            p2sub = "- Saturated Fat: 0.000g → 0%\n- Trans Fat: 0.000g\n- Polyunsaturated Fat: 0.000g\n- Monounsaturated Fat: 0.000g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 0mg → 0%\n▸Total Carbohydrate 11.00g → 4%"
            p3sub = "- Dietary Fiber: 1.5g → 5%\n- Sugars: 9.00g"
            p4 = "▸Protein 0.50g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 40mg → 3%\n▸Iron: _\n▸Potassium: 140mg → 3%\n▸Vitamin A: 112mcg → 12%\n▸Vitamin C: 31.5mg → 35%"
        elif class_index == 12:
            result = "Mango"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-Mango (336g) \n\nAmount per serving:"
            header2 = "Calories: 202"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 1.3g → 2%"
            p2sub = "- Saturated Fat: 0.3g → 2%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.2g\n- Monounsaturated Fat: 0.5g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 3.4mg → 0%\n▸Total Carbohydrate 50g → 18%"
            p3sub = "- Dietary Fiber: 5.4g → 19%\n- Sugars: 46g"
            p4 = "▸Protein 2.8g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 37mg → 3%\n▸Iron: 0.5mg → 3%\n▸Potassium: 564.5mg → 12%\n▸Vitamin A: 227mcg → 14%\n▸Vitamin C: 167.2mg → 82%"
        elif class_index == 13:
            result = "Orange"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-Orange (140g) \n\nAmount per serving:"
            header2 = "Calories: 69"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.2g → 0%"
            p2sub = "- Saturated Fat: 0.04g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.066g\n- Monounsaturated Fat: 0.06g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 0mg → 0%\n▸Total Carbohydrate 18g → 7%"
            p3sub = "- Dietary Fiber: 3.1g → 11%\n- Sugars: 12g"
            p4 = "▸Protein 1.3g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 60mg → 5%\n▸Iron: 0.2mg → 1%\n▸Potassium: 232.4mg → 5%\n▸Vitamin A: 17mcg → 2%\n▸Vitamin C: 74.4mg → 79%"
        elif class_index == 14:
            result = "Peach"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: 1 medium-Peach (100g) \n\nAmount per serving:"
            header2 = "Calories: 39"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.25g → 0%"
            p2sub = "- Saturated Fat: 0.019g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.086g\n- Monounsaturated Fat: 0.067g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 0mg → 0%\n▸Total Carbohydrate 9.54g → 3%"
            p3sub = "- Dietary Fiber: 1.5g → 5%\n- Sugars: 8.39g"
            p4 = "▸Protein 0.91g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 6mg → 1%\n▸Iron: 0.25mg → 1%\n▸Potassium: 190mg → 4%\n▸Vitamin A: 16mcg → 2%\n▸Vitamin C: 6.6mg → 7%"
        elif class_index == 15:
            result = "Pineapple"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: pineapple-slices (100g) \n\nAmount per serving:"
            header2 = "Calories: 48"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.12g → 0%"
            p2sub = "- Saturated Fat: 0.009g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.042g\n- Monounsaturated Fat: 0.014g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 1mg → 0%\n▸Total Carbohydrate 12.63g → 5%"
            p3sub = "- Dietary Fiber: 1.4g → 5%\n- Sugars: 2.26g"
            p4 = "▸Protein 0.54g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 13mg → 1%\n▸Iron: 0.28mg → 2%\n▸Potassium: 115mg → 2%\n▸Vitamin A: 3mcg → 0%\n▸Vitamin C: 36.2mg → 40%"
        elif class_index == 16:
            result = "Strawberry"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: strawberry-pieces(5-6p) (100g) \n\nAmount per serving:"
            header2 = "Calories: 32"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.3g → 0%"
            p2sub = "- Saturated Fat: 0.015g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.155g\n- Monounsaturated Fat: 0.043g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 1mg → 0%\n▸Total Carbohydrate 7.68g → 3%"
            p3sub = "- Dietary Fiber: 2g → 7%\n- Sugars: 4.66g"
            p4 = "▸Protein 0.67g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 16mg → 1%\n▸Iron: 0.42mg → 2%\n▸Potassium: 153mg → 3%\n▸Vitamin A: 1mcg → 0%\n▸Vitamin C: 58.8mg → 65%"
        else:
            result = "Watermelon"
            header1 = "Nutrition Facts"
            sep1 = "----------------------------------------"
            p1 = "Serving size: watermelon-slices (100g) \n\nAmount per serving:"
            header2 = "Calories: 30"
            sep2 = "----------------------------------------"
            p2 = "▸Total Fat 0.15g → 0%"
            p2sub = "- Saturated Fat: 0.15g → 0%\n- Trans Fat: _\n- Polyunsaturated Fat: 0.05g\n- Monounsaturated Fat: 0.037g"
            p3 = "▸Cholesterol 0mg → 0%\n▸Sodium 1mg → 0%\n▸Total Carbohydrate 7.55g → 3%"
            p3sub = "- Dietary Fiber: 0.4g → 1%\n- Sugars: 6.2g"
            p4 = "▸Protein 0.61g"
            sep3 = "----------------------------------------",
            p5 = "▸Vitamin D: _\n▸Calcium: 7mg → 1%\n▸Iron: 0.24mg → 1%\n▸Potassium: 112mg → 2%\n▸Vitamin A: 28mcg → 3%\n▸Vitamin C: 8.1mg → 9%"

        return jsonify ({
            "result" : result,
            "header1" : header1,
            "p1" : p1,
            "header2" : header2,
            "p2" : p2,
            "p2sub" : p2sub,
            "p3" : p3,
            "p3sub" : p3sub,
            "p4" : p4,
            "p5" : p5,
            "sep1" : sep1,
            "sep2" : sep2,
            "sep3" : sep3
            
        })


    except IOError as e:
        return jsonify ({
            "error" : str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)