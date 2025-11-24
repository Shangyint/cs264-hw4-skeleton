class ResponseParser:
    """
    Parses LLM responses to extract a single function call using a rigid textual format.

    The LLM must output exactly one function call at the end of its response.
    Do NOT use JSON or XML. Use rfind to locate the final markers.
    """

    BEGIN_CALL = "----BEGIN_FUNCTION_CALL----"
    END_CALL = "----END_FUNCTION_CALL----"
    ARG_SEP = "----ARG----"
    VALUE_SEP = "----VALUE----"

    # Students should include this exact template in the system prompt so the LLM follows it.
    response_format = f"""
your_thoughts_here
...
{BEGIN_CALL}
function_name
{ARG_SEP}
arg1_name
{VALUE_SEP}
arg1_value (can be multiline)
{ARG_SEP}
arg2_name
{VALUE_SEP}
arg2_value (can be multiline)
...
{END_CALL}

DO NOT CHANGE ANY TEST! AS THEY WILL BE USED FOR EVALUATION.
"""

    def parse(self, text: str) -> dict:
        """
        Parse the function call from `text` using string.rfind to avoid confusion with
        earlier delimiter-like content in the reasoning.

        Returns a dictionary: {"thought": str, "name": str, "arguments": dict}
        
        TODO(student): Implement this function using rfind to parse the function call
        """
        raise NotImplementedError("parse method must be implemented by the student")
