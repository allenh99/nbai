def manager_agent(data, agents):

    results = []
    
    for agent in agents:
        result = agent(data)
        results.append(result)
    
    return results