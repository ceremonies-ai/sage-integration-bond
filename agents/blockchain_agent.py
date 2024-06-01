#agents/blockchain_agents.py
import os
import sys
from bondai.agents import Agent
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from tools.blockchain_transaction_tool import BlockchainTransactionTool, Parameters

AGENT_ADDRESS = '0xA93a4469dA2299f6E524c8BE65289e74CDa689b7'

class BlockchainAgent(Agent):
    def __init__(self):
        self.blockchain_tool = BlockchainTransactionTool()

    def perform_task(self, function_name: str, parameters: dict, agent_address: str):
        print(f"Performing {function_name} with parameters: {parameters} and agent address: {agent_address}")  # Debugging output
        result = self.blockchain_tool.run(function_name=function_name, parameters=parameters, agent_address=agent_address)
        return result

    def process_tasks(self, tasks):
        results = []
        for task in tasks:
            print(f"Processing task: {task}")  # Debugging output
            result = self.perform_task(task['function'], task['params'], task['agent_address'])
            results.append(result)
        return results

if __name__ == "__main__":
    agent = BlockchainAgent()
    tasks = [
        {
            "function": "registerAgent",
            "params": {"contentDescription": "Data Analyzer", "price": 10},
            "agent_address": AGENT_ADDRESS
        },
        {
            "function": "initiateTransaction",
            "params": {"seller": AGENT_ADDRESS, "unitsOfService": 5},
            "agent_address": AGENT_ADDRESS
        }
    ]
    results = agent.process_tasks(tasks)
    for result in results:
        print(result)