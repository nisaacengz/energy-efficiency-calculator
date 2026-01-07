import tkinter as tk
from tkinter import messagebox

def calculate_efficiency():
    try:
        area = float(entry_area.get())
        consumption = float(entry_consumption.get())
                            
        max_consumption = area * 10
        score = (max_consumption / consumption) * 100
        score = min(score, 100)

        if score > 90:
            advice = "Excellent! Your energy efficiency is very high."
        elif score > 70:
            advice = "Moderate efficiency. Consider using LED lights and smart plugs."
        else:
            advice = "Low efficiency. Optimize heating/cooling and device usage."

        messagebox.showinfo("Result", f"Energy Efficiency Score: {score:.1f}/100\nAdvice: {advice}")
    except ValueError:

        messagebox.showerror("Error", "Please enter valid numbers!")

window = tk.Tk()
window.title("Mini Energy Efficiency Calculator")
window.geometry("400x250")

tk.Label(window, text="Home/Office Area (m²):").pack(pady=5)
entry_area = tk.Entry(window)
entry_area.pack(pady=5)
tk.Label(window, text="Monthly Electricity Consumption (kW):").pack(pady=5)
entry_consumption = tk.Entry(window)
entry_consumption.pack(pady=5)

tk.Button(window, text="Calculate", command=calculate_efficiency).pack(pady=20)

window.mainloop()