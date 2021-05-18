class Route:

    vehicle = ""
    jobs = []

    def __init__(self):
        pass

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def __init__(self, vehicle, jobs):
        self.vehicle = vehicle

        for job in jobs:
            self.jobs.append(job)
