from huggingface_hub import HfApi, HfFolder, Repository

from huggingface_hub import upload_folder

upload_folder(
    folder_path="./t5_coqa_final_model/t5_coqa_final_model",  # e.g. ./t5_finetuned_coqa
    path_in_repo="root",  # root
    repo_id="shumukhe/coqa-t5-bot",           # replace with your repo ID
    repo_type="model"
)