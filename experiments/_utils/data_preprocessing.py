import datasets as ds

def convert_to_number(s):
    """
    Convert a string to a number (int or float).

    Parameters:
    s (str): The string to convert.

    Returns:
    int or float: The converted number.
    """
    if s is None:
        return None
    elif '.' in s or 'e' in s.lower():
        return float(s)
    elif "/" in s:
        num, denom = s.split("/")
        return int(num) / int(denom)
    else:
        return int(s)

def load_data(dataset_name):
    """
    Load the data from the specified dataset.
    
    Arguments:
        dataset_name (str): Name of the dataset to load.
    
    Returns:
        data (Dataset): The loaded dataset.
    """

    datasets = {
        "gsm8k": lambda: ds.load_dataset('gsm8k', 'main', split="test"),
        "gsmplus_numerical_substitution": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "numerical substitution"),
        "gsmplus_digit_expansion": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "digit expansion"),
        "gsmplus_integer_decimal_fraction_conversion": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "integer-decimal-fraction conversion"),
        "gsmplus_adding_operation": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "adding operation"),
        "gsmplus_reversing_operation": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "reversing operation"),
        "gsmplus_problem_understanding": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "problem understanding"),
        "gsmplus_distraction_insertion": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "distraction insertion"),
        "gsmplus_critical_thinking": lambda: ds.load_dataset('qintongli/GSM-Plus', split="test").filter(lambda x: x['perturbation_type'] == "critical thinking"),
        "commonsenseqa": lambda: ds.load_dataset('tau/commonsense_qa', 'default', split='validation'),
    }

    if dataset_name in datasets:
        data = datasets[dataset_name]()
    else:
        raise ValueError(f"Dataset {dataset_name} not recognized.")

    return data

def select_data(dataset, size_type, size, seed):
    """
    Selects a subset of data from the given dataset based on the specified size and size type.

    Arguments:
    - dataset: The input dataset to select data from.
    - size_type: The type of size to use for selecting data. Must be either "number" or "percentage".
    - size: The size of the subset to select. If size_type is "number", it represents the number of samples to select.
            If size_type is "percentage", it represents the percentage of the total dataset to select.
    - seed: Random seed for shuffling.

    Returns:
    - A subset of the input dataset based on the specified size and size type.

    Raises:
    - ValueError: If the size_type is not valid. Must be either "number" or "percentage".
    """
    if size_type == "number" and size <= len(dataset) and size > 0 and isinstance(size, int):
        selected_dataset = dataset.shuffle(seed=seed).select(range(size))
    elif size_type == "percentage" and size <= 1 and size > 0:
        selected_dataset = dataset.shuffle(seed=seed).select(range(int(len(dataset) * size)))
    else:
        raise ValueError("Invalid size_type and/or size. Please provide a valid size_type and size.")
    
    return selected_dataset

def preprocess_gsm8k(dataset):
    """
    Preprocess the loaded GSM8K data.
    
    Arguments:
        dataset (Dataset): The dataset to preprocess.
    
    Returns:
        preprocessed_data (Dataset): The preprocessed dataset.
    """
    def add_key(row):
        row["key"] = int(row["answer"].split("####")[1].replace(",", ""))  # Extract the key from the answer
        return row

    preprocessed_dataset = dataset.map(add_key)

    return preprocessed_dataset

def preprocess_commonsenseqa(dataset):
    """
    Preprocess the loaded CommonsenseQA data.
    
    Arguments:
        dataset (Dataset): The dataset to preprocess.
    
    Returns:
        preprocessed_data (Dataset): The preprocessed dataset.
    """

    def add_key(row):
        row["key"] = row["answerKey"]
        return row

    preprocessed_dataset = dataset.map(add_key)

    return preprocessed_dataset

def preprocess_gsmplus(dataset):
    """
    Preprocess the loaded GSM-Plus data.
    
    Arguments:
        dataset (Dataset): The dataset to preprocess.
    
    Returns:
        preprocessed_data (Dataset): The preprocessed dataset.
    """

    def add_key(row):
        row["key"] = convert_to_number(row["answer"])
        return row

    preprocessed_dataset = dataset.map(add_key)

    return preprocessed_dataset

def load_preprocess_data(dataset_name, seed=37, size_type="number", size=300):
    """
    Load and preprocess the loaded data.
    
    Arguments:
        dataset_name (str): Name of the dataset to load and preprocess
        seed (int): Random seed for shuffling.
        size_type (str): Type of size, either "number" or "percentage".
        size (int or float): The size of the set, either as a number or a percentage.
    
    Returns:
        preprocessed_data (Dataset): The preprocessed dataset.
    """

    preprocessors = {
        "gsm8k": preprocess_gsm8k,
        "gsmplus_numerical_substitution": preprocess_gsmplus,
        "gsmplus_digit_expansion": preprocess_gsmplus,
        "gsmplus_integer_decimal_fraction_conversion": preprocess_gsmplus,
        "gsmplus_adding_operation": preprocess_gsmplus,
        "gsmplus_reversing_operation": preprocess_gsmplus,
        "gsmplus_problem_understanding": preprocess_gsmplus,
        "gsmplus_distraction_insertion": preprocess_gsmplus,
        "gsmplus_critical_thinking": preprocess_gsmplus,
        "commonsenseqa": preprocess_commonsenseqa,
    }

    if dataset_name in preprocessors:
        raw_dataset = load_data(dataset_name)
        selected_dataset = select_data(raw_dataset, size_type, size, seed)
        preprocessed_dataset = preprocessors[dataset_name](selected_dataset)
    else:
        raise ValueError("Dataset not recognized.")

    return preprocessed_dataset
