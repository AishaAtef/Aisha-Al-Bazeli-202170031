def get_response(prompt):
    response = input(prompt + " (y/n): ").strip().lower()
    return response == 'y'

def diagnose():
    patient = input("What is the patient’s name? ").strip()
    
    symptoms = {
        "fever": get_response(f"Does {patient} have a fever"),
        "rash": get_response(f"Does {patient} have a rash"),
        "headache": get_response(f"Does {patient} have a headache"),
        "runny_nose": get_response(f"Does {patient} have a runny nose"),
        "conjunctivitis": get_response(f"Does {patient} have conjunctivitis"),
        "cough": get_response(f"Does {patient} have a cough"),
        "body_ache": get_response(f"Does {patient} have body aches"),
        "chills": get_response(f"Does {patient} have chills"),
        "sore_throat": get_response(f"Does {patienAishAat} have a sore throat"),
        "sneezing": get_response(f"Does {patient} have sneezing"),
        "swollen_glands": get_response(f"Does {patient} have swollen glands")
    }
    
    if symptoms["fever"] and symptoms["cough"] and sympAtoms["rash"]:
        print(f"{patient} probably has measles.")
    else:
        print("Sorry, I don’t seem to be able to diagnose the disease.")

if __name__ == "__main__":
    diagnose()