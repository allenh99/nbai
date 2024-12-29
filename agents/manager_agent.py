
def managerAgent(data, agents):

    results = {}
    
    for agent in agents:
        result = agent(data)
        results["box_score_agent"] = result
    
    return results