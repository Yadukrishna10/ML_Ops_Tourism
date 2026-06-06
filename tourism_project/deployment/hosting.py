
from huggingface_hub import HfApi

api = HfApi()

api.upload_file(
    path_or_fileobj="tourism_project/deployment/app.py",
    path_in_repo="app.py",
    repo_id="Yadukrish10/tourism-package-space",
    repo_type="space"
)

api.upload_file(
    path_or_fileobj="tourism_project/deployment/requirements.txt",
    path_in_repo="requirements.txt",
    repo_id="Yadukrish10/tourism-package-space",
    repo_type="space"
)

print("Deployment files uploaded successfully.")
