# Mini Energy Efficiency Calculator - Terminal Version

try:
    area = float(input("Enter home/office area (m²): "))
    consumption = float(input("Enter monthly electricity consumption (kWh): "))

    max_consumption = area * 10
    score = (max_consumption / consumption) * 100
    score = min(score, 100)

    if score > 90:
        advice = "Excellent! Your energy efficiency is very high."
    elif score > 70:
        advice = "Moderate efficiency. Consider using LED lights and smart plugs."
    else:
        advice = "Low efficiency. Optimize heating/cooling and device usage."

    print(f"\nEnergy Efficiency Score: {score:.1f}/100")
    print(f"Advice: {advice}")

except ValueError:
    print("Error: Please enter valid numbers!")