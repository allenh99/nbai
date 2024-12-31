def managerAgent(data, agents):
    """
    Manager agent that coordinates multiple agents and aggregates their results.

    Parameters:
        data (dict): The input data to be processed by the agents.
        agents (dict): A dictionary of agents, where the key is the agent name, and the value is the agent function.
    """
    results = {}
    
    for agent_name, agent_function in agents.items():
        result = agent_function(data)
        results[agent_name] = result
    
    return results