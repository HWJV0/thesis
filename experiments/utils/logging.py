import logging

def print_response(out):
    for i, o in enumerate(out, start=1):
        print("---------------------------------")
        print(f"Output {i}")
        print("-----------")
        print("-----------")
        print(f"Thought:\t{o.thought}")
        print("----------")
        print(f"Action Type:\t{o.action_type}")
        print("----------")
        print(f"Observation:\t{o.observation}")
        print("----------")
        print(f"Answer:\n{o.answer}")
        print("----------")
        print(f"Is Correct:\t{o.is_correct}")
        print("----------")
        print(f"Reflections:\t{o.reflections if o.reflections else 'None'}")
        print("---------------------------------\n")

def log_response(f, out):
    for i, o in enumerate(out, start=1):
        log_output = f"""
            ---------------------------------
            Output {i}
            -----------
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
            ---------------------------------
            """
        f.write(log_output)
