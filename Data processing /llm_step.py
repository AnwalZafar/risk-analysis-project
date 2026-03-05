import json
import os

# --- THE RESEARCH-BASED BRAIN ---
def analyze_scam_logic(text):
    text = text.lower()
    
    # Factors from your research articles
    risk_keywords = ["urgent", "free visa", "no experience", "immediate", "commission", "deposit", "rebate"]
    high_risk_locs = ["cambodia", "poipet", "dubai", "uae", "armenia"]
    
    found_flags = [f for f in risk_keywords if f in text]
    found_locs = [l for l in high_risk_locs if l in text]
    
    if found_flags or found_locs:
        return "high_risk_scam", f"Flags: {', '.join(found_flags + found_locs)}"
    return "legitimate", "Standard professional post"

def run_analysis():
    # Looking inside your cleaned_data folder
    folder = "cleaned_data"
    file_name = "large_formatted_dataset.json"
    full_path = os.path.join(folder, file_name)
    
    print(f"📂 Looking for data in: {full_path}")
    
    if not os.path.exists(full_path):
        print(f"❌ Error: Cannot find {file_name} in {folder} folder!")
        return

    with open(full_path, 'r') as f:
        data = json.load(f)

    # --- THE LINE YOU ASKED TO CHANGE ---
    # We use [-5:] to look at the very end of the file (the scams)
    print(f"🚀 Analyzing the LAST 5 records (The High-Risk section)...")
    
    results = []
    for item in data[-5:]: 
        msg = item.get('message_text', '')
        label, reason = analyze_scam_logic(msg)
        
        item['ai_label'] = label
        item['ai_reasoning'] = reason
        results.append(item)
        
        print(f"\n[ID: {item.get('message_id')}] -> {label}")
        print(f"Reason: {reason}")

    # Save the output
    with open('llm_analysis_output.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    print("\n✅ DONE! Stage 3 & 4 complete. Check your terminal for the High Risk results!")

if __name__ == "__main__":
    run_analysis()