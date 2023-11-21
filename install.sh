go version &> /dev/null && echo "Go is installed. Proceeding with installation ..." || { echo "Go is not installed. Please install it and then proceed with the installation."; exit 1; }

echo "Installing Glow ..."
go install github.com/charmbracelet/glow@latest
echo "Glow installed!"

echo "\nInstalling CLI"
pip install pensieve_cli
echo "CLI installed"

mkdir -p $HOME/.pensieve/notes

echo "export PENSIEVE_ROOT=$HOME/.pensieve" >> $HOME/.zshrc
