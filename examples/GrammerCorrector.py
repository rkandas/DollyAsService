from DollyClientProxy import DollyClientProxy

ai = DollyClientProxy()
result = ai.instruct_generate(f"Correct this to standard English with correct spelling: \
                               I eating a appl yeasterday.")
print(result)