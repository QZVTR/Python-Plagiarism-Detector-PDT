class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.name}"


class ProjectManager:
    def __init__(self):
        self.users = {}
        self.projects = {}
        self.tasks = {}

    def create_user(self, user_id, name):
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def assign_project_to_user(self, project_id, user_id):
        if user_id in self.users and project_id in self.projects:
            self.users[user_id].assign_project(self.projects[project_id])

    def create_project(self, project_id, name):
        project = Project(project_id, name)
        self.projects[project_id] = project
        return project

    def create_task(self, task_id, description, project_id):
        task = Task(task_id, description)
        self.tasks[task_id] = task
        if project_id in self.projects:
            self.projects[project_id].add_task(task)
        return task

    def __str__(self):
        users_str = "\n".join(str(user) for user in self.users.values())
        projects_str = "\n".join(str(project) for project in self.projects.values())
        tasks_str = "\n".join(str(task) for task in self.tasks.values())
        return (
            f"Users:\n{users_str}\n\nProjects:\n{projects_str}\n\nTasks:\n{tasks_str}"
        )


def main():
    project_manager = ProjectManager()

    # Create users
    user1 = project_manager.create_user(1, "Alice")
    user2 = project_manager.create_user(2, "Bob")

    # Create projects
    project1 = project_manager.create_project(1, "Project A")
    project2 = project_manager.create_project(2, "Project B")

    # Create tasks
    task1 = project_manager.create_task(1, "Task 1 for Project A", 1)
    task2 = project_manager.create_task(2, "Task 2 for Project A", 1)
    task3 = project_manager.create_task(3, "Task 1 for Project B", 2)

    # Assign projects to users
    project_manager.assign_project_to_user(1, 1)
    project_manager.assign_project_to_user(2, 2)

    # Print information
    print(project_manager)


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.assigned_projects = []

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"

    def assign_project(self, project):
        self.assigned_projects.append(project)


class Task:
    def __init__(self, task_id, description, status="To Do"):
        self.task_id = task_id
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status}"


if __name__ == "__main__":
    main()
