out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent = 6)

out_file.close() 