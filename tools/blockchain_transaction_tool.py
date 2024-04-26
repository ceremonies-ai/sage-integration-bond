import json
import os
from pydantic import BaseModel
from bondai.tools import Tool
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

TOOL_NAME = "BlockchainTransactionTool"
TOOL_DESCRIPTION = """
This tool manages blockchain transactions for a bot-to-bot payment system. It can register agents,
initiate transactions, confirm content delivery, and handle funds within the Ethereum network,
directly interacting with the SageMarketV1 contract.
"""

class Parameters(BaseModel):
    function_name: str
    parameters: dict
    agent_address: str = None

contract_abi_path = os.path.join(os.path.dirname(__file__), '..', 'contracts', 'abis', 'SageMarketV1.json')
with open(contract_abi_path, 'r') as abi_definition:
    CONTRACT_ABI = json.load(abi_definition)
CONTRACT_ADDRESS = '0x9305df480152602D416D3479a093952365925C88'
RPC_ADDRESS = 'https://altar-rpc.ceremonies.ai'

class BlockchainTransactionTool(Tool):
    def __init__(self):
        super().__init__(TOOL_NAME, TOOL_DESCRIPTION, parameters=Parameters)
        self.web3 = Web3(HTTPProvider(RPC_ADDRESS))
        if self.web3.net.version == "4":  # Assuming Rinkeby for PoA middleware requirement
            self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    def run(self, function_name: str, parameters: dict, agent_address: str = None):
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum network.")

        func = getattr(self.contract.functions, function_name)
        if not func:
            raise ValueError(f"Function {function_name} not found in the contract.")

        # Setup transaction parameters
        tx_params = {
            'from': agent_address,
            'nonce': self.web3.eth.get_transaction_count(agent_address),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }

        tx = func(**parameters).buildTransaction(tx_params)
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key='your_private_key_here')
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return f"Transaction submitted. TX Hash: {tx_hash.hex()}"