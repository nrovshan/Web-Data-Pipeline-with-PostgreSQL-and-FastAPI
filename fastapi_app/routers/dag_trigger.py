import subprocess

def dag_trigger(dag_id: str):
    result = subprocess.run(["docker", "exec", "-i", "auto_pipe_project-airflow-scheduler-1", "airflow", "dags", "trigger", dag_id],
                            capture_output=True, text=True)
    return result.stdout or result.stderr
    