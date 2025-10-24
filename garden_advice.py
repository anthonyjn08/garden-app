# Code refactored into a function.
def get_advice(season, plant_type):
    """
    Returns advice to user based on their input.

    - param: season, the season the user input.
    - param: plant_type, the plant type the user input.
    - return: advice based on the user input.
    """
    advice = ""

    # Determine what advice to give based on season entered.
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determin further advice based on the plant type.
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


def main():
    """
    Main function call to take input from user, and return adviced based
    on their input.
    """
    season = input("Enter the season (summer/winter/other): ").lower()
    plant_type = input(
        "Enter the plant type (flower/vegetable/other): ").lower()

    advice = get_advice(season, plant_type)
    print("\n--- Gardening Advice ---")
    print(advice)


if __name__ == "__main__":
    main()
