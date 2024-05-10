import panel as pn  # GUI

# Define predefined responses for the bot
responses = {
    "Hi": "Hello! Welcome to our pizza restaurant. How can I assist you today?",
    "Order": "Sure, let's start with your order. What would you like to have? We have pepperoni, cheese, and eggplant "
             "pizzas, as well as sides like fries and drinks like coke and sprite.",
    "Delivery": "Great choice! Could you please provide your address for delivery?",
    "Menu": "Here's our menu:\n- Pepperoni Pizza: $12.95, $10.00, $7.00\n- Cheese Pizza: $10.95, $9.25, "
            "$6.50\n- Eggplant Pizza: $11.95, $9.75, $6.75\n- Fries: $4.50, $3.50\n- Greek Salad: $7.25\nToppings: "
            "extra cheese $2.00, mushrooms $1.50, sausage $3.00, canadian bacon $3.50, AI sauce $1.50, "
            "peppers $1.00\nDrinks: coke $3.00, $2.00, $1.00, sprite $3.00, $2.00, $1.00, bottled water $5.00",
    "Thank you": "You're welcome! If you have any more questions or would like to place an order, just let me know."
}


# Define a function to process user inputs and generate bot responses
def process_input(user_input):
    return responses.get(user_input, "I'm sorry, I didn't understand that.")


# Define a function to handle user interactions
def handle_interaction(event):
    user_input = inp.value_input.strip().lower()  # Convert user input to lowercase and remove leading/trailing
    # whitespace
    inp.value = ''
    bot_response = process_input(user_input)
    context.append({'role': 'user', 'content': user_input})
    context.append({'role': 'assistant', 'content': bot_response})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(user_input, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(bot_response, width=600)))


# Set up the user interface
pn.extension()
panels = []  # collect display
context = []

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(handle_interaction, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

# Display the dashboard
dashboard
