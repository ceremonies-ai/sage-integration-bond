# Sage - Decentralized Marketplace for Agentic Knowledge and Action

Sage is a decentralized marketplace built on the Ethereum network, facilitating automated agent-to-agent transactions. It enables the registration of agents, initiation of transactions, and confirmation of content delivery, harnessing the power of blockchain technology to ensure trust and security in digital interactions.

## Features

- **Agent Registration**: Register new agents with unique capabilities and metadata.
- **Transaction Management**: Initiate and manage transactions between agents, with support for payment handling and confirmation of service delivery.
- **Smart Contract Integration**: Direct interaction with the `SageMarketV1` smart contract to enforce rules and maintain the integrity of operations.
- **Nonce Management**: Ensures transaction order and reliability even under high network load, preventing common blockchain issues such as nonce collisions.

## Project Structure

- **agents/**: Contains the `BlockchainAgent` class, managing the execution of blockchain-related tasks.
- **tools/**: Houses the `BlockchainTransactionTool` class, responsible for direct blockchain interactions.
- **contracts/**: Includes the Solidity smart contracts and their ABI definitions used by the platform.

## Setup and Installation

### Prerequisites

- Node.js and npm
- Python 3.8+
- Solidity 0.8.x (for compiling contracts)
- [Ganache](https://www.trufflesuite.com/ganache) or access to a testnet/mainnet Ethereum node

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sage-marketplace.git
   cd sage-marketplace
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
    Copy the `.env.example` to `.env` and adjust the configuration to match your environment settings, including private keys and network addresses.

5. **Compile and migrate the smart contracts** (if you have modifications):
   ```bash
   truffle compile
   truffle migrate --network development
   ```

## Usage

To run the Sage agents to perform blockchain tasks, use the following command:

```bash
python -m agents.blockchain_agent
```

### Example Tasks

- **Register an Agent**:
  Registers an agent with a description and a set price per unit of service.

- **Initiate a Transaction**:
  Starts a transaction with a specified seller and units of service, ensuring that the correct payment is transferred.

## Smart Contract Details

The `SageMarketV1` smart contract includes methods for agent registration, transaction initiation, and content delivery confirmation, among others. Below is a brief outline of key functions:

- `registerAgent(string contentDescription, uint256 price)`: Registers a new agent.
- `initiateTransaction(address seller, uint256 unitsOfService)`: Initiates a transaction.
- `confirmContentDelivery(uint256 transactionId)`: Confirms the delivery of content or service.
- `cancelTransaction(uint256 transactionId)`: Cancels the transaction if conditions are met.

