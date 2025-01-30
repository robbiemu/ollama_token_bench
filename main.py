import ollama
import logging
import argparse
import pandas as pd
import ollama

# Set up logging to stderr by default
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--log-file', help='Log file path')
parser.add_argument('--log-response', action='store_true', help='log the response')
parser.add_argument('--prompt-file', help='Prompt file path', default='prompts.txt')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--model-path', help='Ollama model path')
group.add_argument('model_path_arg', nargs='?', help='Ollama model path (if --model-path is not used)')
args = parser.parse_args()

# If --log-file is specified, log to the file instead of stderr
log_response = args.log_file or args.log_response
if args.log_file:
    logger.handlers[0] = logging.FileHandler(args.log_file)

model_path = args.model_path or args.model_path_arg

# Load prompts from a file
with open(args.prompt_file, 'r') as file:
    prompts = [line.strip() for line in file.readlines()]

time_series = []
for prompt in prompts:
    # Run the model on the prompt
    tx = ollama.generate(model=model_path, prompt=prompt)

    if log_response:
        logger.info("PROMPT %s", prompt)
        logger.info(tx['response'])

    # Calculate the time taken
    tokens_sec = tx["eval_count"]/(tx["eval_duration"]/1e9)

    # Append time taken to time series
    time_series.append(tokens_sec)

# Log time series statistics
df = pd.DataFrame(time_series, columns=['Tokens per Second'])
logger.info(f'Time series statistics: {df["Tokens per Second"].describe()}')
