import argparse

from experiments._utils.data_preprocessing import load_preprocess_data
from experiments._utils.model_evaluation import calculate_accuracy, append_stats
from experiments._utils.logging import setup_logging, log_experiment_info, log_response

def execute_experiment(method, strategy, dataset, logging):
    if method == "reflexion":
        if strategy == "few_shot":
            print("Executing reflexion few-shot experiment: ", dataset)
        else: # strategy == "zero_shot"
            print("Executing reflexion zero-shot experiment with dataset: ", dataset)
    
    elif method == "self_reflection":
        if strategy == "zero_shot":
            print("Executing self-reflection few-shot experiment with dataset: ", dataset)
        else: # strategy == "few_shot"
            print("Executing self-reflection zero-shot experiment with dataset: ", dataset)
            
    elif method == "peer_reflection":
        if strategy == "few_shot":
            print("Executing peer-reflection few-shot experiment with dataset: ", dataset)
        else:
            print("Executing peer-reflection zero-shot experiment with dataset: ", dataset)

def select_prompts(method, strategy, dataset_name, reasoning_type, reflection_prompt_type, example_type):
    """
    Select the appropriate prompts for the experiment.

    Arguments:
        method (str): Method to use [reflexion, selfreflection, peerreflection]
        strategy (str): Strategy to use [zero_shot, few_shot]
        dataset_name (str): Dataset to use [gsm8k, other_dataset]
        reasoning_type (str): Reasoning type [direct, cot, pot, cot+pot]
        reflection_prompt_type (str): Prompt type to use [negative, conservative]
        example_type (str): Type of examples [negative, mixed]

    Returns:
        tuple: Tuple containing the prompt, examples, reflect_examples, and reflect_prompt 
    """

    method_dict = {
        "reflexion": "REFLEXION",
        "self_reflection": "SELFREFLECTION",
        "peer_reflection": "PEERREFLECTION"
    }

    strategy_dict = {
        "zero_shot": "ZEROSHOT",
        "few_shot": "FEWSHOT"
    }

    reasoning_type_dict = {
        "direct": "DIRECT",
        "cot": "COT",
        "pot": "POT",
        "cot+pot": "COT+POT"
    }

    reflection_prompt_type_dict = {
        "negative": "NEGATIVE",
        "conservative": "CRITICAL"
    }

    example_type_dict = {
        "negative": "NEGATIVE",
        "mixed": "MIXED"
    }


    # prompt=REFLEXION_COT_INSTRUCTION_GSM8K,
    # based on the above write the f"" string to get the prompt
    prompt_name = f"{method_dict[method]}_{reasoning_type_dict[reasoning_type]}_INSTRUCTION_{dataset_name.upper()}"
    prompt = globals().get(prompt)

    # examples=GSM8K_FEWSHOT_EXAMPLES_COT
    # based on the above write the f"" string to get the examples
    examples_name = f"{dataset_name.upper()}_FEWSHOT_EXAMPLES_{reasoning_type_dict[reasoning_type]}"
    examples = globals().get(examples)

    # reflect_examples=GSM8K_FEWSHOT_EXAMPLES_SELFREFLECTION_COT_REFLECT,
    # based on the above write the f"" string to get the 
    reflect_examples_name = f"{dataset_name.upper()}_FEWSHOT_EXAMPLES_{method_dict[method]}_{reasoning_type_dict[reasoning_type]}_REFLECT"
    reflect_examples = globals().get(reflect_examples_name)

    # reflect_prompt=REFLEXION_COT_REFLECT_INSTRUCTION_GSM8K,
    # based on the above write the f"" string to get the reflect_prompt
    reflect_prompt_name = f"{method_dict[method]}_{reasoning_type_dict[reasoning_type]}_REFLECT_INSTRUCTION_{dataset_name.upper()}"
    reflect_prompt = globals().get(reflect_prompt_name)

    if prompt is None or examples is None or reflect_examples is None or reflect_prompt is None:
        raise ValueError("Could not find the required prompts and examples for the experiment")

    return prompt, examples, reflect_examples, reflect_prompt
    
def run_experiment(method, strategy, dataset_name, model_name, logging, reasoning_type, reflection_prompt_type, example_type, model_name_2):
    """
    Run an experiment with a specific method, strategy, and dataset.

    Arguments:
        method (str): Method to use [reflexion, selfreflection, peerreflection]
        strategy (str): Strategy to use [zero_shot, few_shot]
        dataset_name (str): Dataset to use [gsm8k, other_dataset]
        model_name (str): Model to use
        logging (bool): Whether to log the experiment results
        reasoning_type (str): Reasoning type [direct, cot, pot, cot+pot]
        reflection_prompt_type (str): Prompt type to use [negative, conservative]
        example_type (str): Type of examples [negative, mixed]
        model_name_2 (str): Second model to use (for peer-reflection only)

    Returns:
        None
    """

    # Load the dataset
    dataset = load_preprocess_data(dataset_name)

    # Set up logging if required
    if logging:
        setup_logging(method, strategy, dataset_name, model_name, logging, reasoning_type, reflection_prompt_type, example_type, model_name_2)

    # Execute the experiment
    execute_experiment(method, strategy, dataset, logging)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run an experiment with a specific method, strategy, and dataset.")
    
    # Main parameters
    parser.add_argument("--method", type=str, required=True, help="Method to use [reflexion, selfreflection, peerreflection]")
    parser.add_argument("--strategy", type=str, required=True, help="Strategy to use [zero_shot, few_shot]")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset to use [gsm8k, gsmhard, commonsenseqa, strategyqa]")
    parser.add_argument("--model", type=str, required=True, help="Model to use")

    # Additional parameters
    parser.add_argument("--logging", type=bool, required=False, default=True, help="Whether to log the experiment results")
    parser.add_argument("--reasoning_type", type=str, required=False, default="cot", choices=["direct", "cot", "pot", "cot+pot"], help="Reasoning type [direct, cot, pot, cot+pot]")
    parser.add_argument("--reflection_prompt_type", type=str, required=False, default="negative", choices=["negative", "conservative"], help="Prompt type to use [negative, conservative]")
    parser.add_argument("--example_type", type=str, required=False, default="negative", choices=["negative", "mixed"], help="Type of examples [negative, mixed]")
    parser.add_argument("--model_2", type=str, required=False, help="Second model to use (for peer-reflection only)")

    args = parser.parse_args()

    if args.method == "peerreflection" and args.model_2 is None:
        raise ValueError("Model 2 must be provided for peer-reflection method")
    
    # Run the experiment with the provided parameters
    run_experiment(args.method, args.strategy, args.dataset, args.model, args.logging, args.reasoning_type, args.reflection_prompt_type, args.example_type, args.model_2)
