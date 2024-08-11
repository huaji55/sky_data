import json

with open('your file path', 'r', encoding='utf-8') as file:
    file_content = file.read()
    file_content = file_content.replace('[]', '"None"')

start_index = file_content.find('"spirit_shops":')

start_index = file_content.find('[', start_index)
end_index = file_content.find(']', start_index) + 1

json_data = file_content[start_index:end_index]

data = json.loads(json_data)

with open('your file path', 'w', encoding='utf-8') as file:
    for item in data:
        json.dump(item, file, ensure_ascii=False)
        file.write('\n')
