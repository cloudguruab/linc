<h1 align="center">🧠 LINC</h1>
<div align="center">Graph based service for your blockchain wallet</div>

## 💥 Why

Linc is a wallet service that comes with address configuration, tracking and token transfers, retrieving balance information. You can use linc to support your desktop, mobile, and web-based wallets. Linc supports multi provider connections regardless of hardware availability. The sole purpose is to allow service level support to blockchain platforms like Etherium. 

This project uses two primary functions for connecting to either a local or hosted node. Since local nodes require less service level authentication we recommend setting up your development environment using a local node such as Ganache from the truffle framework. 

Configuration for hosted environments will require setting up your project inside popular platforms like infura.io or others. The purpose of this API is to allow the developer to build on either a local or hosted node, and connect to establish wallet address, track and monitor token transfers as well as checking balances for each address. 


## 🕹️ Setting up your environment
Start by installing the project dependencies
```bash
# installing deps
pip install requirements.txt

# run the following commands
python3 -m venv env
source python3 env/bin/activate
```

Create your `.env` file
```zsh
# variables for hosted nodes
INFURA_HTTP
INFURA_WSS
INFURA_PROJECT_ID
INFURA_PROJECT_SECRET

#variables for local nodes
URL_HTTP
```

## ✂️ Running a local node
For our local client we have chosen Ganache due to its CLI or UI availability.
[information on setting up a local node](https://trufflesuite.com/docs/ganache/quickstart.html)

## 🥶 Running a hosted node
Linc uses infura for hosted nodes.
[Information on running a hosted node](https://infura.io/)

## 🏄‍♂️ Starting your server

Starting your server environment from django

```bash
python3 manage.py runserver
```

Once running, navigate to http://127.0.0.1:8000/graphql

```bash
Django version 4.0.1, using settings 'api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


## 🪓 Local vs Hosted Nodes

A local node requires less trust than a hosted one. A malicious hosted node can give you incorrect information, log your sent transactions with your IP address, or simply go offline. Incorrect information can cause all kinds of problems, including loss of assets.

On the other hand, with a local node your machine is individually verifying all the transactions on the network, and providing you with the latest state. Unfortunately, this means using up a significant amount of disk space, and sometimes notable bandwidth and computation. Additionally, there is a big up-front time cost for downloading the full blockchain history.

If you want to have your node manage keys for you (a popular option), you must use a local node. Note that even if you run a node on your own machine, you are still trusting the node software with any accounts you create on the node.


## 📖 Docs
- [Infura docs](https://infura.io/docs/ethereum#section/Make-Requests/JSON-RPC-Methods)
- [Web3.py docs](https://web3py.readthedocs.io/en/latest/quickstart.html)
- [Graphql docs](https://docs.graphene-python.org/en/latest/quickstart/)