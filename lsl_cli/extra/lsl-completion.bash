_lsl_completion()
{
    local cur prev shell_name
	
	cur=${COMP_WORDS[COMP_CWORD]}

	if [[ ! -n $(command -v lsl) ]]; then
		return 0 
	fi 

	local COMMANDS=(
		"list"
		"echo"
		"show"
		"find"
	)

	local command i
    for (( i=0; i < $COMP_CWORD; i++ )); do
        if [[ ${COMMANDS[@]} =~ ${COMP_WORDS[i]} ]]; then
            command=${COMP_WORDS[i]}
            break
        fi
    done

    if [[ "$cur" == -* ]]; then
    	case $command in
			list) 
				COMPREPLY=($(compgen -W '--all
				 	--list --timeout
				 	--name --type 
				 	--source_id --channel_count 
				 	--channel_format --nominal_srate 
				 	--hostname --uid 
				 	--version --session_id 
				 	--created_at' -- ${cur}))
				return 0
				;;
			echo) 
				COMPREPLY=($(compgen -W "--timeout" -- ${cur}))
				return 0
				;;
			show) 
				COMPREPLY=($(compgen -W "--timeout" -- ${cur}))
				return 0
				;;
			find) 
				COMPREPLY=($(compgen -W '
				 	--name --type 
				 	--source_id --channel_count 
				 	--channel_format --nominal_srate 
				 	--hostname --uid 
				 	--version --session_id 
				 	--created_at' -- ${cur}))
				return 0
				;;
		esac
    fi

    if [[ -n $command ]]; then
    	case $command in 
    		echo|show)
				COMPREPLY=( $( compgen -W "$( lsl list | xargs echo )" -- ${cur} ) )
		esac
	fi

	if [[ "$command" == "" ]]; then
		COMPREPLY=( $( compgen -W "$(echo ${COMMANDS[@]})" -- ${cur} ) )
	fi

	return 0
} &&


complete -F _lsl_completion lsl