import sys

SYSTEM_PROMPT = (
    "Friendly Medical Assistant Chatbot initialized.\n"
    "CRITICAL SAFETY RULE: This AI is for educational purposes. Never diagnose or prescribe. "
    "Always advise consulting a professional medical practitioner."
)

knowledge_base = {
    "sore throat": "A sore throat is often caused by viral infections like the common cold or flu, or bacterial infections like strep throat. Dry air or allergies can also cause it. \nSAFETY NOTE: Please consult a doctor if you experience difficulty swallowing or breathing.",
    "paracetamol": "Paracetamol is generally safe for children when given in the correct dosage based on their age and weight. \nSAFETY NOTE: Never guess the dose. Always consult a pediatrician or pharmacist to get the precise dosage instructions.",
    "fever": "A fever is usually a sign that your body is fighting off an infection. Stay hydrated and rest. \nSAFETY NOTE: Seek immediate medical care if the fever is very high or lasts more than 3 days.",
    "cough": "Coughs can be caused by viral infections, allergies, or asthma. Drinking warm fluids can help soothe it. \nSAFETY NOTE: If coughing persists for weeks or is accompanied by blood, see a physician immediately."
}

def query_chatbot(user_message):
    message_lower = user_message.lower()
    
    response = ""
    matched = False
    
    for key, value in knowledge_base.items():
        if key in message_lower:
            response = value
            matched = True
            break
            
    if not matched:
        response = "I can provide general educational information about common symptoms (like sore throat, fever, cough, or paracetamol safety). For specific cases, please consult a qualified healthcare professional."
        
    friendly_response = f"[Medical Assistant]: {response}\n(Disclaimer: I am an AI, not a doctor.)"
    return friendly_response

print("--- General Health Chatbot Initialized (100% Offline Mode) ---")
print(f"System Settings: {SYSTEM_PROMPT}")
print("Type 'exit' to quit.\n")

sample_queries = [
    "What causes a sore throat?",
    "Is paracetamol safe for children?"
]

for query in sample_queries:
    print(f"User: {query}")
    bot_reply = query_chatbot(query)
    print(f"{bot_reply}\n" + "-"*50)

while True:
    user_input = input("\nAsk a health question: ")
    if user_input.lower() == 'exit':
        print("Chatbot session closed.")
        break
    
    reply = query_chatbot(user_input)
    print(f"{reply}")
