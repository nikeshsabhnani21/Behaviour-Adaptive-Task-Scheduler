
class Task:

    def __init__(self, name, duration_minutes, difficulty, deadline, days_left, status="pending", priority_score=0):
        """
        Initialization includes all essential attributes of a task, useful information for adaptive scheduling.
        Attributes are utilized to compute priority based on deadline, difficulty and duration of a task.
        """
        self.name = name
        self.duration_minutes = duration_minutes 
        self.difficulty = difficulty
        self.deadline = deadline
        self.days_left = days_left
        self.status = status 
        self.priority_score = priority_score
        
    def __str__(self):
        """
        Returns a user-readable representation of a task. 
        """
        return (f"Name: {self.name}\n"
                f"Duration: {self.duration_minutes} mins\n"
                f"Difficulty: {self.difficulty}\n"
                f"Deadline: {self.deadline}\n"
                f"Days Left: {self.days_left}\n"
                f"Status: {self.status}")
    
    def update_status(self,new_status):
        """
        Initial status is pending. This method allows the user to update the status of the task 
        at the end of the day, by selecting one of the following new status; "completed", "skipped" or "postponed".
        """
        if new_status == "completed":
            self.status = "completed"
        elif new_status == "skipped":
            self.status = "skipped"
        elif new_status == "postponed":
            self.status = "postponed"

    def priority(self,behaviour_stadistics):
        """
        Computes the priority of a task as a tuple.

        Priority order: 
        1. Closer deadline 
        2. Higher task difficulty
        3. Task duration

        Behaviour adaptation is only applied on hard tasks, to avoid any noise that can be cause from easy and medium tasks.
        """
        difficulty_weight = self.difficulty

        if self.difficulty >= 4:
            avoided_task = behaviour_stadistics["skipped_hard"] + behaviour_stadistics["postponed_hard"]
            completed_task = behaviour_stadistics["completed_hard"]
            difference = avoided_task - completed_task
            # This if statement avoid extreme punishment/reward
            if -7 <= difference <= 7:
                # Punish only when a task has been skipped/postponed 2 or more times
                if difference >= 2:
                    difficulty_weight += 1
                # Reward, when tasks has been completed 2 or more times
                elif difference <= -2:
                    difficulty_weight -= 1
        
        return (self.days_left, -difficulty_weight, -self.duration_minutes)
