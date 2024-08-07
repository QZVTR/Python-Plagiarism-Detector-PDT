class er:
    def __init__(self, id, n):
        self.name = id
        self.g = n
        self.sgd = []

    def assign_project(self, p):
        self.sgd.append(p)

    def __str__(self):
        return f"User ID: {self.name}, Name: {self.g}"  # Comment


"""
Comment 1
"""


class d:
    def __init__(self, x, y):  # T
        self.id = x
        self.project = y
        self.jobs = []

    def add_task(self, a):
        self.jobs.append(a)  # T

    def __str__(self):
        return f"Project ID: {self.id}, Name: {self.project}"


"""
1
2
3
4
5
6
"""


class Task:
    def __init__(self, task_id, description, status="To Do"):
        self.jobId = task_id
        self.notADescription = description
        self.gdp = status

    def update_status(self, new_status):
        self.gdp = new_status

    def __str__(self):
        return f"Task ID: {self.jobId}, Description: {self.notADescription}, Status: {self.gdp}"


class P:
    def __init__(self):
        self.people = {}
        self.proj = {}
        self.jobs = {}

    def userCreation(self, user_id, name):
        user = er(user_id, name)
        self.people[user_id] = user
        return user

    def cT(self, project_id, name):
        project = d(project_id, name)
        self.proj[project_id] = project
        return project

    """
    Comment 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    """

    def TaskCreation(self, task_id, description, project_id):
        task = Task(task_id, description)
        self.jobs[task_id] = task
        if project_id in self.proj:
            self.proj[project_id].add_task(task)
        return task

    def asPro(self, project_id, user_id):
        if user_id in self.people and project_id in self.proj:
            self.people[user_id].assign_project(self.proj[project_id])

    def __str__(self):
        users_str = "\n".join(str(user) for user in self.people.values())
        projects_str = "\n".join(str(project) for project in self.proj.values())
        tasks_str = "\n".join(str(task) for task in self.jobs.values())
        return (
            f"Users:\n{users_str}\n\nProjects:\n{projects_str}\n\nTasks:\n{tasks_str}"
        )


def main():
    taser = P()

    # Create users
    user5 = taser.userCreation(1, "Alice")
    user3 = taser.userCreation(2, "Bob")

    # Create projects
    project2 = taser.cT(1, "Project A")
    project7 = taser.cT(2, "Project B")

    # Create tasks
    task6 = taser.TaskCreation(1, "Task 1 for Project A", 1)
    task8 = taser.TaskCreation(2, "Task 2 for Project A", 1)
    task9 = taser.TaskCreation(3, "Task 1 for Project B", 2)

    # Assign projects to users
    taser.asPro(1, 1)
    taser.asPro(2, 2)

    # Print information
    print(taser)


if __name__ == "__main__":
    main()
