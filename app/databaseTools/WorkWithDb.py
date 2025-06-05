import json

#TODO: обработка исключений
class WorkWithDb:
    @staticmethod
    def append_task(id: str, task: str, path: str):
        with open(path, 'r') as file:
            data = json.load(file)

        if id in data.keys():
            tasks = data[id]
            tasks.append(task)
            data[id] = tasks
        else:
            data[id] = [task]

        with open(path, 'w') as file:
            file.write(json.dumps(data))
    
    @staticmethod
    def delete_task(id: str, task: str, path: str):
        with open(path, 'r') as file:
            data = json.load(file)

        tasks = data[id]
        tasks.remove(task)
        data[id] = tasks

        with open(path, 'w') as file:
            file.write(json.dumps(data))
    
    @staticmethod
    def show_tasks(id: str, path: str):
        with open(path, 'r') as file:
            data = json.load(file)

        if id in data.keys():
            tasks = data[id]
        else:
            tasks = []
        return tasks