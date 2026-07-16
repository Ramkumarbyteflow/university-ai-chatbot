# Concept1 = Functions
def get_university_info(topic):
    if topic == "admission":
        return "Admissions are open from June to Sep"
    elif topic == "fees":
        return "Full Free"
    elif topic == "courses":
        return "All courses available"
    else :
        return "I am not feeded about that"
    
print(get_university_info("courses"))
print(get_university_info("fees"))
print(get_university_info("admission"))

# Concept2 = Dictionary
# University data stored as a dictionary
University = {
    "Name" : "Karpagam University",
    "Location" : "Coimbatore",
    "Established" : "1992",
    "Courses" : ["B.A", "B.Com", "BBA", "B.E"],
    "Fees" : {
        "B.A" : 50000,
        "B.Com" : 55000,
        "BBA" : 25000,
        "B.E" : 75000

    }
    
}

print(University["Name"])
print(University["Courses"])
print(University["Fees"]["B.E"])

University["Principal"] = "BabuRaj"

for courses, fees in University["Fees"].items():
    print(f"{courses} cost rs {fees} per Year"  )

import json
university_dict = {
    "Name" : "Karpagam University",
    "Location" : "Coimbatore",
    "Established" : "1992"
}

json_string = json.dumps(university_dict, indent=4)
print("JSON String:")
print(json_string)
print(type(json_string))

back_to_dict = json.loads(json_string)
print("\nDictionary:")
print(back_to_dict["Name"])

# =================================================================================

# Dictionary testing :
def get_university_info(topic):
    if topic == "admission":
        return "Admissions are open from June to Sep"
    elif topic == "fees":
        return "Full Free"
    elif topic == "courses":
        return "All courses available"
    else :
        return "I am not feeded about that"
    

student_query = {
    "student_name" : "Ramkumar",
    "question" : "what is BBA fees?",
    "topic" : "fees",
    "timestamp" : "16/07/2026"
       
}

print(f"{student_query['student_name']} asks {student_query['question']}")
topic = student_query["topic"]
answer = get_university_info(topic)
print("Answer =", answer)