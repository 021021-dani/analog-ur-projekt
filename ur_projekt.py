import os 
import tkinter as tk # Import the tkinter to create a GUI
import time # Import time to current time
import math # Import math to use mathematical functions
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Analog clock") # Set the title of the window

# Create a canvas to draw the clock((Canvas er der, hvor man tegner uret, altså den “flade”, hvor al grafik bliver placeret)
canvas_size = 400
canvas = tk.Canvas(root, width=canvas_size,height=canvas_size, bg="black") # Create a white canvas
canvas.pack() # Pack the canvas into the window

# Clock's centerum (Define centrum og radius for uret)
center_x = canvas_size // 2
center_y = canvas_size // 2 
radius = 180 # Radius of the clock

# Tilføjes og redigeres  logoet
script_dir = os.path.dirname(os.path.abspath(__file__))   # Få stien til mappen hvor loget ligger
image_path = os.path.join(script_dir, "logo.png")         # Byg en fuld sti til logo.pn

# Åben billedet og skaler det ned (f.eks. til 100x100 pixels)
original_image = Image.open(image_path)
resized_image = original_image.resize((373, 373), Image.LANCZOS) # Her kan ændres størrelse af logoet
logo = ImageTk.PhotoImage(resized_image) # # Konvertér til noget Tkinter kan bruge
canvas.create_image(center_x, center_y - radius + 180, image=logo)  # Placer over uret
canvas.logo = logo     

# Function to draw the clock face whith 12 hours marks
def draw_clock_face():
    # Draw the clock face circle
    canvas.create_oval(center_x - radius, center_y - radius, 
                       center_x + radius, center_y + radius,
                       outline= "black", width=4) 
     # Romertal
    roman_numerals = ["XII", "I", "II", "III", "IV", "V", 
                  "VI", "VII", "VIII", "IX", "X", "XI"]
    # Draw the hour marks by use for loop(Denne linje tegner en cirkel, som bliver urskiven)
    for i in range(12): 
        angle = math.radians(i * 30) # 360 degrees / 12 hours = 30 degrees per hour
        x_start = center_x + (radius +0) * math.sin(angle) # Calculate the start x position of the hour mark
        y_start = center_y - (radius + 0) * math.cos(angle) # Calculate the start y position of the hour mark
        x_end = center_x + radius * math.sin(angle) # Calculate the end x
        y_end = center_y - radius * math.cos(angle) # Calculate the end y
        canvas.create_line(x_start, y_start, x_end, y_end,fill="black", width=2) # Draw the hour mark
        
        # Romertal restens tilføjelse og farver
        numeral = roman_numerals [i]
        text_x = center_x + (radius - 10) * math.sin(angle)
        text_y = center_y - (radius - 10) * math.cos(angle)
        canvas.create_text(text_x, text_y, text=numeral, font=("caribli", 18, "bold"), fill="lime green")

        
# Funktion to update clock hands(Hver gang klokken opdateres
def update_clock():
    canvas.delete("hands")  # Remove the previous hands by deleting item tags "hands"
        
#  First remove the old hands so they don't overlap)
    t = time.localtime()    # Get the current local time
    hours = t.tm_hour % 12  # Convert to 12-hour format
    minutes = t.tm_min      
    seconds = t.tm_sec     
        
    # Calculate angels for each hand(beregnes visernes vinkler)
    sec_angle = math.radians(seconds * 6) # 6 deggres per second
    min_angle = math.radians(minutes * 6 + seconds * 0.1) # 6 degrees per minute + fraction by seconds
    hour_angle = math.radians(hours * 30 + minutes * 0.5) # 30 deegres per hour + fraction by minutes
        
        
    # Calculate end points for the second hand(Sekundviser tynd og rød)
    sec_x = center_x + (radius - 30) * math.sin(sec_angle)
    sec_y = center_y - (radius - 30) * math.cos(sec_angle)
    canvas.create_line(center_x, center_y, sec_x, sec_y, fill= "white", width=3, tag="hands")
        
    # Calculate end points for the minute hand
    min_x = center_x + (radius - 50) * math.sin(min_angle)
    min_y = center_y - (radius - 50) * math.cos(min_angle)
    canvas.create_line(center_x, center_y, min_x, min_y, fill="red", width=3, tag="hands")
        
        # Calculate end points for the hour hand
    hour_x = center_x + (radius - 80) * math.sin(hour_angle)
    hour_y = center_y - (radius - 80) * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill="red", width=5, tag="hands")
        
        # Schedule this fuctions to be called again after 1000 mlliseconds(1 seconds)
    root.after(1000, update_clock)
        
# Draw the clock face once
draw_clock_face()

#  Start the pointers and update every second
update_clock()

# Run the GUI
root.mainloop()
    
        
        
        
        
        
        
