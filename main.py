import tkinter as tk
from langchain_community.llms import Ollama

# Load model
llm = Ollama(model="tinyllama")


def generate():
    country = country_entry.get()
    city = city_entry.get()

    prompt = f"""
    Suggest a fancy restaurant name in {city}, {country}.
    Also suggest 5 famous dishes from that culture.

    Format:
    Restaurant Name:
    Dishes:
    """

    response = llm.invoke(prompt)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, response)


# Create window
root = tk.Tk()
root.title("Restaurant AI 🍽️")
root.geometry("500x500")

# Labels and inputs
tk.Label(root, text="Enter Country:").pack()
country_entry = tk.Entry(root, width=40)
country_entry.pack()

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root, width=40)
city_entry.pack()

# Button
tk.Button(root, text="Generate", command=generate).pack(pady=10)

# Output box
output_text = tk.Text(root, height=15, width=60)
output_text.pack()

# Run app
root.mainloop()
