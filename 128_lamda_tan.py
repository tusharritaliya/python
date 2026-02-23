words = ["pakistan", "india", "bhutan", "china", "afghanistan", "nepal"]

result = list(filter(lambda x: x.endswith("tan"), words))

print(result)