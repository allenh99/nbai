import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

def chat_decision_maker(agent_results):
    """
    Uses OpenAI's Chat API to analyze the results from agents and provide a final decision.
    
    Parameters:
        agent_results (dict): Results from agents, with agent names as keys and their outputs as values.
        
    Returns:
        dict: The final signal and reasoning.
    """
    # Prepare the input for the chat model
    messages = [
        {"role": "system", "content": "You are an assistant that analyzes agent outputs to make a final decision."},
        {"role": "user", "content": f"""
Agent Results:
{agent_results}

Based on the above results, determine the final signal ("over" or "under") and explain your reasoning clearly.

Return the output as:
Final Signal: <over/under>
Reasoning: <explanation>
        """}
    ]
    
    # Call the OpenAI Chat API
    response = client.chat.completions.create(
        model="gpt-4o",  # Adjust to your preferred model
        messages=messages,
    )
    
    # Extract the assistant's response
    choices = response.choices
    first_choice = choices[0]
    return first_choice.message.content

def managerAgent(data, agents):
    """
    Manager agent that coordinates multiple agents, aggregates their results, and uses OpenAI Chat API for final decision.
    
    Parameters:
        data (dict): The input data to be processed by the agents.
        agents (dict): A dictionary of agents, where the key is the agent name, and the value is the agent function.
    
    Returns:
        dict: The final decision and reasoning.
    """
    # Collect results from agents
    agent_results = {}
    for agent_name, agent_function in agents.items():
        agent_results[agent_name] = agent_function(data)
    
    # Use OpenAI Chat API to make a decision
    final_decision = chat_decision_maker(agent_results)
    
    return {
        "agent_results": agent_results,
        "final_decision": final_decision
    }