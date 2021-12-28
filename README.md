# lsl-cli
Command-line tools for the [Lab Streaming Layer](https://labstreaminglayer.readthedocs.io/info/getting_started.html). 

# Installation
### Method 1: Using pip
```bash
pip install lsl-cli
```

### Method 2: From source
```bash
git clone https://github.com/yop0/lsl-cli.git
cd lsl-cli
pip install -e .
```

## Enabling autocompletion (bash/zsh users)
The package comes with autocompletion files for Bash and Zsh. 
To enable autocompletion, first get the path to the 
package sources (where you cloned the repo). If you installed with Method 1, you can get the source path using:  
```bash
pip show lsl-cli | grep Location
```

Then, if you use Bash add the following line to your `~/.bashrc`: 
```bash 
source path\to\lsl-cli/extra/lsl-completion.bash
```
Alternatively if you use Zsh, you need to put in `~/.zshrc`: 
```bash
source path\to\lsl-cli/extra/lsl-completion.zsh
```
