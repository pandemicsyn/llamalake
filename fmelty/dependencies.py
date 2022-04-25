from fastapi import Header, HTTPException


def get_trace_id(x_meltano_trace_id: str = Header(...)):
    """get_trace_id is similar to the grpc trace_id method, just exists to test what middleware feels like."""
    if not x_meltano_trace_id:
        raise HTTPException(status_code=400, detail="Missing trace_id header")


def get_env(x_meltano_env: str = Header(...)):
    if not x_meltano_env:
        raise HTTPException(status_code=400, detail="Missing env header")
    return x_meltano_env
