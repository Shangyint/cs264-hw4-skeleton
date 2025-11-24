## CS 264 HW Starter: Minimal ReAct Agent Scaffold

This folder contains a scaffold you must complete to build a minimal ReAct agent for SWE-Bench.

You will:
- Implement a textual function-call protocol (no JSON/XML) and parse it with rfind
- Implement the ReAct Agent logic (main loop, context management, tool execution)
- Run on SWE-Bench verified subset; report your accuracy

### Entry point 
The entry point to the code is `run_agent.py`. It wires up the model, parser, agent, and environment, and provides the CLI. 
You don't need to modify this code. 

### Files to complete
- `agent.py` — Implement main logic of ReAct agent (tools and main loop)
- `envs.py` - Implement additional functions to run inside the environment 
- `response_parser.py` — Implement `ResponseParser.parse` using rfind

### Function-call protocol (required)
LLM must output a single function call at the end:
```
your_thoughts_here
...
----BEGIN_FUNCTION_CALL----
function_name
----ARG----
arg_name
----VALUE----
arg_value
...
----END_FUNCTION_CALL----
```
Parse using `str.rfind` to avoid issues with earlier markers.

### Required tools
- `run_bash_cmd(command: str)` — Execute a shell command via your SWE environment
- `finish(result: str)` — Finalize and return result string from `agent.run`

### Limits and evaluation
- Backend model: GPT-5 mini (medium reasoning)
- `MAX_STEPS` must be capped at 100
- Report accuracy with your implementation and any custom tools you add

### Setup
1) Install dependencies
```bash
uv pip install -r requirements.txt
```

2) Configure your API key.


For full evaluation, follow the course README/evaluation harness instructions and produce the JSON results specified in the assignment.
