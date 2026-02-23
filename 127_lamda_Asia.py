words = ["india", "malaysia", "nepal", "indonesia", "russia", "asia"]

result = list(filter(lambda x: x.endswith("asia"), words))

print(result)