import  argparse
from utils import entrainement
from utils import classification
import os

print(os.getcwd())

# Initialisation des arguments du script : 
parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, required=True)
parser.add_argument('-n', type=int, required=True)
#parser.add_argument('--display', type=str, required=False)
parser.add_argument('--output', type=str, required=False)
args = parser.parse_args()

# Récupération des arguments dans des variables : 
input_path = args.i
input_number = args.n
#display = args.display
output = args.output

entrainement(input_number)

classification(input_path, output)