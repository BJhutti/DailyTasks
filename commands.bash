wsl
eval "$(ssh-agent -s)"
ssh -T git@github.com
source .venv/bin/activate