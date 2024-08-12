
from web3 import Web3
import json
synapse_values = []

chains_info = [
    {
        'network_name': 'Ethereum Mainnet',
        'contract_address': '0xd10eF2A513cEE0Db54E959eF16cAc711470B62cF',
        'rpc_url': 'https://eth.llamarpc.com'
    },
    {
        'network_name': 'BSC',
        'contract_address': '0x8F5BBB2BB8c2Ee94639E55d5F41de9b4839C1280',
        'rpc_url': 'https://binance.llamarpc.com'
    },
    {
        'network_name': 'Arbitrum',
        'contract_address': '0x73186f2Cf2493f20836b17b21ae79fc12934E207',
        'rpc_url': 'https://arbitrum.llamarpc.com'
    },
    {
        'network_name': 'Polygon',
        'contract_address': '0x7875Af1a6878bdA1C129a4e2356A3fD040418Be5',
        'rpc_url': 'https://polygon.llamarpc.com'
    },
    {
        'network_name': 'Aurora',
        'contract_address': '0x809DC529f07651bD43A172e8dB6f4a7a0d771036',
        'rpc_url': 'https://aurora-mainnet.gateway.tatum.io'
    },

    {
        'network_name': 'Optimism',
        'contract_address': '0xe8c610fcb63A4974F02Da52f0B4523937012Aaa0',
        'rpc_url': 'https://optimism.llamarpc.com'
    },

    {
        'network_name': 'Canto',
        'contract_address': '0x93124c923dA389Bc0f13840fB822Ce715ca67ED6',
        'rpc_url': 'https://canto.slingshot.finance'
    },

    {
        'network_name': 'Avalanche',
        'contract_address': '0x3a01521F8E7F012eB37eAAf1cb9490a5d9e18249',
        'rpc_url': 'https://avax.meowrpc.com'
    },
    {
        'network_name': 'Base',
        'contract_address': '0xfFC2d603fde1F99ad94026c00B6204Bb9b8c36E9',
        'rpc_url': 'https://base.llamarpc.com'
    },

    {
        'network_name': 'Metis',
        'contract_address': '0xaB0D8Fc46249DaAcd5cB36c5F0bC4f0DAF34EBf5',
        'rpc_url': 'https://metis-mainnet.public.blastapi.io'
    },
    {
        'network_name': 'Moonriver',
        'contract_address': '0x432036208d2717394d2614d6697c46DF3Ed69540',
        'rpc_url': 'https://moonriver.public.blastapi.io'
    },
    {
        'network_name': 'Boba',
        'contract_address': '0xd5609cD0e1675331E4Fb1d43207C8d9D83AAb17C',
        'rpc_url': 'https://mainnet.boba.network'
    },
    {
        'network_name': 'Blast',
        'contract_address': '0x3100dC8464A8523306c3C5034de24a8927d6E590',
        'rpc_url': 'https://rpc.blast.io'
    },
]

contract_abi_json = """[[{"inputs":[{"internalType":"contract IERC20","name":"_synapse","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Harvest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"allocPoint","type":"uint256"},{"indexed":true,"internalType":"contract IERC20","name":"lpToken","type":"address"},{"indexed":true,"internalType":"contract IRewarder","name":"rewarder","type":"address"}],"name":"LogPoolAddition","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"allocPoint","type":"uint256"},{"indexed":true,"internalType":"contract IRewarder","name":"rewarder","type":"address"},{"indexed":false,"internalType":"bool","name":"overwrite","type":"bool"}],"name":"LogSetPool","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"synapsePerSecond","type":"uint256"}],"name":"LogSynapsePerSecond","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"lastRewardTime","type":"uint64"},{"indexed":false,"internalType":"uint256","name":"lpSupply","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accSynapsePerShare","type":"uint256"}],"name":"LogUpdatePool","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"SYNAPSE","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"contract IERC20","name":"_lpToken","type":"address"},{"internalType":"contract IRewarder","name":"_rewarder","type":"address"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"calls","type":"bytes[]"},{"internalType":"bool","name":"revertOnFail","type":"bool"}],"name":"batch","outputs":[{"internalType":"bool[]","name":"successes","type":"bool[]"},{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"claimOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"harvest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lpToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"pids","type":"uint256[]"}],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingSynapse","outputs":[{"internalType":"uint256","name":"pending","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permitToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"uint128","name":"accSynapsePerShare","type":"uint128"},{"internalType":"uint64","name":"lastRewardTime","type":"uint64"},{"internalType":"uint64","name":"allocPoint","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"pools","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rewarder","outputs":[{"internalType":"contract IRewarder","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IRewarder","name":"_rewarder","type":"address"},{"internalType":"bool","name":"overwrite","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_synapsePerSecond","type":"uint256"}],"name":"setSynapsePerSecond","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"synapsePerSecond","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"},{"internalType":"bool","name":"direct","type":"bool"},{"internalType":"bool","name":"renounce","type":"bool"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"}],"name":"updatePool","outputs":[{"components":[{"internalType":"uint128","name":"accSynapsePerShare","type":"uint128"},{"internalType":"uint64","name":"lastRewardTime","type":"uint64"},{"internalType":"uint64","name":"allocPoint","type":"uint64"}],"internalType":"struct MiniChefV2.PoolInfo","name":"pool","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"int256","name":"rewardDebt","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdrawAndHarvest","outputs":[],"stateMutability":"nonpayable","type":"function"}]]"""
contract_abi = json.loads(contract_abi_json)[0]

for chain in chains_info:
    connection = Web3(Web3.HTTPProvider(chain['rpc_url']))
    contract = connection.eth.contract(address=chain['contract_address'], abi=contract_abi)
    synapse_value_per_second = contract.functions.synapsePerSecond().call()
    # Convert to monthly and add commas
    synapse_value_per_month = "{:,.0f}".format((synapse_value_per_second * 30 * 24 * 60 * 60)/10**18)
    synapse_values.append({
        'network_name': chain['network_name'],
        'value': synapse_value_per_month,
    })
def get_synapse_values():
    synapse_values = []
    for chain in chains_info:
        try:
            connection = Web3(Web3.HTTPProvider(chain['rpc_url']))
            contract = connection.eth.contract(address=chain['contract_address'], abi=contract_abi)
            synapse_value_per_second = contract.functions.synapsePerSecond().call()
            synapse_value_per_month = "{:,.0f}".format((synapse_value_per_second * 30 * 24 * 60 * 60) / 10**18)
            synapse_values.append({
                'network_name': chain['network_name'],
                'value': synapse_value_per_month,
            })
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
            print(f"RPC error occurred on {chain['network_name']}: {e}")
            synapse_values.append({
                'network_name': chain['network_name'],
                'value': "RPC error"
            })
    return synapse_values

    return synapse_values