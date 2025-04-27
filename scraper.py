import json
from groq import Groq

# Setup Groq client
client = Groq(
    api_key="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"
)

def get_ingredients(drug_name, model="llama3-70b-8192", temperature=0.2):
    prompt = f"""
    You are a pharmaceutical assistant please keep in mind i will provide egyptian drugs, please scrap egyptian website drug eye. 
    For the drug "{drug_name}", list the ingredients in two categories:
    
    1. Active Ingredient(s)
    2. Inactive Ingredients (excipients)
    
    Return the result as a JSON object like:
    {{
        "active": ["..."],
        "inactive": ["..."]
    }}
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model=model,
            temperature=temperature
        )

        content = chat_completion.choices[0].message.content
        print("Raw Groq Output:\n", content)

        # Parse the response safely
        ingredients_dict = json.loads(content.strip())
        if isinstance(ingredients_dict, dict) and "active" in ingredients_dict and "inactive" in ingredients_dict:
            return ingredients_dict
        else:
            print("⚠️ Unexpected format.")
            return None

    except Exception as e:
        print("❌ Groq API Error:", e)
        return None

# Run
if __name__ == "__main__":
    drug_name = input("Enter drug name: ")
    ingredients = get_ingredients(drug_name)
    if ingredients:
        print("\n🧪 Active Ingredients:", ingredients['active'])
        print("🔬 Inactive Ingredients:", ingredients['inactive'])
    else:
        print("Could not retrieve ingredients.")
