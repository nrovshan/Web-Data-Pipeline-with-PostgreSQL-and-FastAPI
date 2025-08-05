import subprocess
from fastapi import APIRouter

router = APIRouter()

def dag_trigger(dag_id: str):
    result = subprocess.run(["docker", "exec", "-i", "auto_pipe_project-airflow-scheduler-1", "airflow", "dags", "trigger", dag_id],
                            capture_output=True, text=True)
    return result.stdout or result.stderr


@router.post("/run_dag/{dag_id}")
def run_dag(dag_id: str):
    output = dag_trigger(dag_id)

    return {"message": f"DAG {dag_id} triggered", "output": output}
    