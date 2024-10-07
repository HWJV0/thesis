import logging

def setup_logging(method, strategy, dataset_name, model_name, logging, reasoning_type, reflection_prompt_type, example_type, model_name_2):

    """
    Set up logging for the experiment.

    Arguments:
    log_file (str): The file where logs will be saved.

    Returns:
    None
    """

    if method == "peer_reflection":
        logging.basicConfig(
            filename=f"results/{dataset_name}/{strategy}/{method}/{model_name}_{model_name_2}/{reasoning_type}/{reflection_prompt_type}_{example_type}.log",
            filemode='a',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    else:
        logging.basicConfig(
            filename=f"results/{dataset_name}/{strategy}/{method}/{model_name}/{reasoning_type}/{reflection_prompt_type}_{example_type}.log",
            filemode='a',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

def log_error(message):
    """Log an error message.

    Arguments:
    message (str): The error message to log.
    
    Returns:
    None
    """

    logging.error(message)

def log_warning(message):
    """Log an warning message.

    Arguments:
    message (str): The error message to log.
    
    Returns:
    None
    """

    logging.warning(message)

def log_success(message):
    """Log an warning message.

    Arguments:
    message (str): The error message to log.
    
    Returns:
    None
    """

    logging.info(message)

def log_experiment_info(method, strategy, dataset_name, model_name, logging, reasoning_type, reflection_prompt_type, example_type, model_name_2):
    """
    Log basic experiment information.

    Parameters:
    method (str): The method used in the experiment.
    strategy (str): The strategy used (e.g., zero_shot, few_shot).
    dataset (str): The dataset used in the experiment.
    """

    if method == "peer_reflection":
        logging.info(f"""
                 ------------------------------------------------------------------
                 Running experiment with the following parameters:
                 -----------
                 Method: {method}
                 -----------
                 Strategy: {strategy}
                 -----------
                 Dataset: {dataset_name}
                 -----------
                 Model 1: {model_name}
                 -----------
                 Model 2: {model_name_2}
                 -----------
                 Reasoning Type: {reasoning_type}
                 -----------
                 Reflection Prompt Type: {reflection_prompt_type}
                 -----------
                 Example Type: {example_type}
                ------------------------------------------------------------------
                """
            )
    else:
        logging.info(f"""
                    ------------------------------------------------------------------
                    Running experiment with the following parameters:
                    -----------
                    Method: {method}
                    -----------
                    Strategy: {strategy}
                    -----------
                    Dataset: {dataset_name}
                    -----------
                    Model: {model_name}
                    -----------
                    Reasoning Type: {reasoning_type}
                    -----------
                    Reflection Prompt Type: {reflection_prompt_type}
                    -----------
                    Example Type: {example_type}
                    ------------------------------------------------------------------
                    """
                )

def log_response(out):
    """
    Log the response to the log file.

    Arguments:
    out (list): List of Output objects

    Returns:
    None
    """

    for i, o in enumerate(out, start=1):
        log_success(f"""
            ------------------------------------------------------------------
            Output {i}
            -----------
            Thought:\t{o.thought}
            ----------
            Action Type:\t{o.action_type}
            ----------
            Observation:\t{o.observation}
            ----------
            Answer:
            {o.answer}
            ----------
            Is Correct:\t{o.is_correct}
            ----------
            Reflections:\t{o.reflections if o.reflections else 'None'}
            ------------------------------------------------------------------
            """
        )

