thisDictionary = {"Brand": "Toyota",
                  "Model": "Camry",
                  "Year": "2014",
                  'Drive': '4WD'
                  }
# How to Add
thisDictionary["Color"] = "Black"
print(thisDictionary)

# How to Remove
thisDictionary.pop("Model")  # Case sensitive
print(thisDictionary)

# How to clear
thisDictionary.clear()
print(thisDictionary)
