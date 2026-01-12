def check_serum(answer):
    if answer == "y":
        return {
            "complete": True,
            "message": "Serum applied. Step 1 complete."
        }
    elif answer == "n":
        return {
            "complete": False,
            "message": "Apply serum before continuing."
        }
    else:
        return {
            "complete": False,
            "message": "Invalid input."
        }
def check_moisturizer(answer):
    if answer == "y":
        return {"message": "Moisturizer applied. Step complete."}
    elif answer == "n":
        return {"message": "Please apply moisturizer."}
    else:
        return {"message": "Invalid input."}
    
def check_sunscreen(answer):
    if answer == "y":
        return {"message": "Sunscreen applied. Skincare routine complete."}
    elif answer == "n":
        return {"message": "Please apply sunscreen."}
    else:
        return {"message": "Invalid input."}

