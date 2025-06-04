import json

class WorkWithDb:
    @staticmethod
    def append_task(id: str, task: str):
        with open('database.json', 'r') as file:
            data = json.load(file)

        if id in data.keys():
            tasks = data[id]
            tasks.append(task)
            data[id] = tasks
        else:
            data[id] = [task]

        with open('database.json', 'w') as file:
            file.write(json.dumps(data))
    
    @staticmethod
    def delete_task(id: str, task: str):
        with open('database.json', 'r') as file:
            data = json.load(file)

        tasks = data[id]
        tasks.remove(task)
        data[id] = tasks

        with open('database.json', 'w') as file:
            file.write(json.dumps(data))