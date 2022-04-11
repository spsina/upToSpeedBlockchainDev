from dotenv import load_dotenv
from helpers import get_erc20_contract, get_web3_object, load_private_key, get_contract_address

load_dotenv()  # take environment variables from .env.

def run():
    private_key = load_private_key()
    contract = get_erc20_contract()    
    print(contract)

if __name__ == "__main__":
    run()
