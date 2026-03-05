import json
import os

def analyze_scam_logic(text):
    text = str(text).lower()
    # Research-backed risk factors
    risk_keywords = ["urgent", "free visa", "no experience", "immediate", "commission", "deposit", "rebate", "crypto", "mining"]
    high_risk_locs = ["cambodia", "poipet", "dubai", "uae", "armenia", "sihanoukville", "bavet"]
    
    found_flags = [f for f in risk_keywords if f in text]
    found_locs = [l for l in high_risk_locs if l in text]
    
    if found_flags or found_locs:
        return "high_risk_scam", f"Flags: {', '.join(found_flags + found_locs)}"
    return "legitimate", "Standard professional post"

def run_full_analysis():
    path = "cleaned_data/large_formatted_dataset.json"
    
    if not os.path.exists(path):
        print("❌ Error: Cannot find the data file!")
        return

    with open(path, 'r') as f:
        data = json.load(f)

    print(f"🚀 Processing COMPLETE dataset ({len(data)} records)... Please wait.")

    full_results = []
    for item in data:
        msg = item.get('message_text', '')
        label, reason = analyze_scam_logic(msg)
        
        # Add the AI labels to the data
        item['ai_label'] = label
        item['ai_reasoning'] = reason
        full_results.append(item)

    # Save EVERYTHING to a new file
    output_file = 'final_full_analysis.json'
    with open(output_file, 'w') as f:
        json.dump(full_results, f, indent=4)
    
    print(f"✅ SUCCESS! All {len(data)} records analyzed and saved to {output_file}")

if __name__ == "__main__":
    run_full_analysis()