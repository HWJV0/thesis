def calculate_accuracy(correct, incorrect):
    total_attempts = correct + incorrect
    if total_attempts == 0:
        return 0
    return (correct / total_attempts) * 100

def append_stats(stats, method, strategy, dataset):
    result_file = os.path.join(RESULTS_DIR, method, strategy, f"{dataset}_{method}_{strategy}_stats.json")
    
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(result_file), exist_ok=True)
    
    # Append results
    if os.path.exists(result_file):
        with open(result_file, 'r+') as file:
            data = json.load(file)
            data.append(stats)
            file.seek(0)
            json.dump(data, file, indent=4)
    else:
        with open(result_file, 'w') as file:
            json.dump([stats], file, indent=4)
