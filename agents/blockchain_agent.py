import os
import sys
from bondai.agents import Agent
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from tools.blockchain_transaction_tool import BlockchainTransactionTool, Parameters

AGENT_ADDRESS='0xA93a4469dA2299f6E524c8BE65289e74CDa689b7'
class BlockchainAgent(Agent):
    def __init__(self):
        # Initialize the BlockchainTransactionTool
        self.blockchain_tool = BlockchainTransactionTool()

    def perform_task(self, function_name: str, parameters: dict, agent_address: str):
        """
        Perform a blockchain operation using the specified function name and parameters.
        """
        # Execute the blockchain transaction
        result = self.blockchain_tool.run(function_name=function_name, parameters=parameters, agent_address=agent_address)
        return result

    def process_tasks(self, tasks):
        """
        Process a list of tasks where each task is a dictionary specifying the function name, parameters, and agent address.
        """
        results = []
        for task in tasks:
            result = self.perform_task(task['function'], task['params'], task['agent_address'])
            results.append(result)
        return results

# Example Usage
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
            "params": {"seller": "0xSellerAddress", "unitsOfService": 5},
            "agent_address": AGENT_ADDRESS
        }
    ]
    results = agent.process_tasks(tasks)
    for result in results:
        print(result)