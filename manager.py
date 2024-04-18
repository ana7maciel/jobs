from queue import Queue

class ContinuousIntegrationManager:
    def __init__(self, number_of_workers: int = 2, max_job_queue_size: int = 10, max_starvation_duration: int = 10):
        self.job_queue = Queue(maxsize=max_job_queue_size)
        self.priority_jobs = []  # Nova lista para os trabalhos prioritários
        self.number_of_workers = number_of_workers
        self.max_starvation_duration = max_starvation_duration
        self.workers = []
        self.finished_jobs = []
        self.starvation_count = 0

    def process_jobs(self):
        while not self.job_queue.empty() and len(self.workers) < self.number_of_workers:
            if self.priority_jobs:
                job = self.priority_jobs.pop(0)
            else:
                job = self.job_queue.get()
            
            print(f"Iniciando trabalho '{job['name']}'...")
            self.workers.append(job)
            self.finished_jobs.append(job)
            self.workers.remove(job)
            print(f"Trabalho '{job['name']}' concluído.")

    def add_job(self, project_name: str, job_duration: int, is_prioritized: bool):
        new_job = {'name': project_name, 'duration': job_duration, 'priority': is_prioritized}

        if is_prioritized:
            self.priority_jobs.append(new_job)
            print(f"Trabalho '{project_name}' adicionado à lista de prioridades.")
        elif self.job_queue.full():
            print("A fila de trabalhos está cheia. Não é possível adicionar mais trabalhos.")
        else:
            self.job_queue.put(new_job)
            print(f"Trabalho '{project_name}' adicionado à fila.")

    def print_final_report(self):
        print(f"Maximum job queue size reached: {len(self.finished_jobs)}")

    def print_current_status(self):
        print(f'Total workers busy/idle: {len(self.workers)}/{self.number_of_workers - len(self.workers)}')
        print(f'Pending jobs: {self.job_queue.qsize()}')
        print(f'Current job per worker: {len(self.workers)}')
        print(f'Priority jobs: {len(self.priority_jobs)}')
