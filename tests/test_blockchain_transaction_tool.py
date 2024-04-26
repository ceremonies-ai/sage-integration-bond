import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.blockchain_transaction_tool import BlockchainTransactionTool

def test_tool_initialization():
    print("Testing Blockchain Transaction Tool Initialization...")
    try:
        tool = BlockchainTransactionTool()
        print("Tool initialized successfully.")
    except Exception as e:
        print(f"Error during tool initialization: {str(e)}")

def test_network_connection(tool):
    print("Testing network connection...")
    if tool.web3.is_connected():
        print("Connected to Ethereum network successfully.")
    else:
        print("Failed to connect to Ethereum network.")

def test_contract_interaction(tool):
    print("Testing contract interaction...")
    try:
        # Example function to check availability
        agent_count = tool.contract.functions.transactionCount().call()
        print(f"Transaction count from contract: {agent_count}")
    except Exception as e:
        print(f"Error interacting with contract: {str(e)}")

if __name__ == "__main__":
    tool = BlockchainTransactionTool()
    test_tool_initialization()
    test_network_connection(tool)
    test_contract_interaction(tool)