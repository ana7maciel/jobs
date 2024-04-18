from manager import ContinuousIntegrationManager

if __name__ == '__main__':
    manager = ContinuousIntegrationManager(2)

    cmd = -1
    while cmd != 0:
        cmd = int(input('Choose operation: 1=add job, 2=process jobs, 0=finish'))
        if cmd == 1:
            name = input('Project name:')
            duration = int(input('Job duration:'))
            priority = int(input('Has Priority (1=True, 0=False):')) == 1
            manager.add_job(name, duration, priority)
        if cmd == 2:
            manager.process_jobs()
        if cmd == 3:
            manager.print_final_report()
        manager.print_current_status()
    manager.print_final_report()
