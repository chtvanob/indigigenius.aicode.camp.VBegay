from fastai.vision.all import *
# import timm
import gradio as gr

path_to_pkl_model = 'model.pkl'

learn = load_learner(path_to_pkl_model)

# get our categories from our model
categories = learn.dls.vocab

# set aside our original categories because we're going to need them in a function below
original_categories = categories

# the name_map variable let's use use our original, one word, categories and attach more information to those values
# we use this information to put Lakota into the output and any other things we want to have
# NOTE: IF YOU WANT TO ADD MORE ELEMENTS, YOU WILL NEED MODIFY THE get_additional_info function
name_map = {
            "Dinosaur": {
                "Museum_location": "In the center of Museum",  
                "desc": "Dino description, they are Massive"
            },
            "Mammoth": {
                "Museum_location": "By the steps",                 
                "desc": "Usually large size, very long tusks that curve upward, and well-developed body hair."
            },
            "Chairs": {
                "Museum_location": "Chairs",  
                "desc": "type of seat, typically designed for one person and consisting of one or more legs, a flat or slightly angled seat and a back-rest."
            }
           }


# create a space to hold remapped categores
new_categories = []

# for each element in our model's categories, make a new element that is "Lakota name (English name)"
# if there isn't a Lakota name in our name_map, just keep the English name
for category in categories:
    if category in name_map.keys():
        new_categories.append(f" ({category})")
    else:
        new_categories.append(category)
        print(category)

# replace the categories from our model with our "Lakota name (English name)" categories
# don't forget that we still have those original categories in the variable "original categories"
categories = new_categories

# from the paramenter "predicted category", use the name_map dictionary to create text of more information for that category
def get_additional_info(predicted_category):
    if predicted_category in name_map.keys():
        return f"Lakota: {name_map[predicted_category]['Museum_location']}\nDescription: {name_map[predicted_category]['desc']}"
    else:
        return "No additional information available."

# from the parameter "img", make a prediction on what category that img is most likely to be according to our model
# this will return a list that includes 1. "predicted_category" and 2. "probabilities", this is just returning data
# we need the probabilities to create content to show the Label
# we need the predicted_category to create content for the Additional Information textbox
def classify_image(img):
    img = PILImage.create(img).resize((192, 192))
    pred, idx, probs = learn.predict(img)
    predicted_category = original_categories[idx]
    return {
        "predicted_category": predicted_category,
        "probabilities": dict(zip(categories, map(float, probs)))
    }

# from the parameter "img", both classify the image and create the additional information for the most likely category
# returns what will go in the label and text boxes and makes the data human readable
def classify_and_display(img):
    result = classify_image(img)
    predicted_result = result["predicted_category"]
    additional_info = get_additional_info(predicted_result)
    return result["probabilities"], additional_info

with gr.Blocks() as demo: #sets a space on the page that will be launched as demo
    gr.Markdown("# My Plant Recognition Demo") # creates a title type text on the page
    with gr.Row(): # creates a row
        with gr.Column(): # in the row above, creates a column
            image = gr.Image() # places an image element in this column, this is where we collect the image
            classify_btn = gr.Button("Classify") # places a button element in the column that triggers classification
        with gr.Column(): # in the row above, creates a new column
            additional_info = gr.Textbox(label="Additional Information", lines=5, interactive=False) # creates a textbox for the additional info
            #gr.Label("Output")
    with gr.Row(): # create a new row
        label = gr.Label() # creat a label element where our classification probabilities will be placed
    
    # the code below is for a "click" event on the classify_button element we placed above
    # this code runs the function classify_and_display, sends that function an image from the image elemement
    # classify_and_display returns the content for the label and additional_info elements, and outputs sends that data to those elements
    classify_btn.click(fn=classify_and_display, inputs=image, outputs=[label, additional_info])

# launch the page    
demo.launch(inline=False)