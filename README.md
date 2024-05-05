# Ollama token bench

ollama-token-bench is a Python script that utilizes the [ollama-python](https://github.com/ollama/ollama-python) library to benchmark tokens per second for a model. This is a very simple script, only generating details about tokens per second. It is meant for reuse and to serve as a base for extension. 

## Overview

Ollama token bench is designed to benchmark models' tokens/s in Ollama, by generating responses based on prompts, logging the results, and computing time series statistics. It provides a command-line interface for easy interaction.

## Installation

- Clone the repository to your local machine: `git clone https://github.com/username/my-app.git`
- Install the required dependencies using pip: `pip install -r requirements.txt`

## Usage

Run the script using the following command: `python main.py [options]`

### Command-line Options
- --log-file FILE: Specify the log file path.
- --log-response: Also log the response generated.
- --prompt-file FILE: Specify the prompt file path (default: prompts.txt).
- --model-path PATH or model_path_arg: Specify the Ollama model path.
- --help: Display help information.

### Example Usage
`python main.py llama3:8b-instruct-fp16 --log-file mylog.log --log-response`

## License

This project is licensed under the MIT License.

## See also:

- [ollama-python](https://github.com/ollama/ollama-python) - Python library for Ollama models.
- [ollama api reference](https://github.com/ollama/ollama/blob/main/docs/api.md)