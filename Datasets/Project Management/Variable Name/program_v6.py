class User:
    def __init__(self, user_id, name):
        self.userName = user_id
        self.age = name
        self.deAssignedProjects = []

    def assign_project(self, project):
        self.deAssignedProjects.append(project)

    def __str__(self):
        return f"User ID: {self.userName}, Name: {self.age}"


class Project:
    def __init__(self, project_id, name):
        self.id = project_id
        self.project = name
        self.jobs = []

    def add_task(self, task):
        self.jobs.append(task)

    def __str__(self):
        return f"Project ID: {self.id}, Name: {self.project}"


class Task:
    def __init__(self, task_id, description, status="To Do"):
        self.jobId = task_id
        self.notADescription = description
        self.gdp = status

    def update_status(self, new_status):
        self.gdp = new_status

    def __str__(self):
        return f"Task ID: {self.jobId}, Description: {self.notADescription}, Status: {self.gdp}"


class ProjectManager:
    def __init__(self):
        self.people = {}
        self.proj = {}
        self.jobs = {}

    def create_user(self, user_id, name):
        user = User(user_id, name)
        self.people[user_id] = user
        return user

    def create_project(self, project_id, name):
        project = Project(project_id, name)
        self.proj[project_id] = project
        return project

    def create_task(self, task_id, description, project_id):
        task = Task(task_id, description)
        self.jobs[task_id] = task
        if project_id in self.proj:
            self.proj[project_id].add_task(task)
        return task

    def assign_project_to_user(self, project_id, user_id):
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
    taskManager = ProjectManager()

    # Create users
    user1 = taskManager.create_user(1, "Alice")
    user2 = taskManager.create_user(2, "Bob")

    # Create projects
    project1 = taskManager.create_project(1, "Project A")
    project2 = taskManager.create_project(2, "Project B")

    # Create tasks
    task1 = taskManager.create_task(1, "Task 1 for Project A", 1)
    task2 = taskManager.create_task(2, "Task 2 for Project A", 1)
    task3 = taskManager.create_task(3, "Task 1 for Project B", 2)

    # Assign projects to users
    taskManager.assign_project_to_user(1, 1)
    taskManager.assign_project_to_user(2, 2)

    # Print information
    print(taskManager)


if __name__ == "__main__":
    main()
